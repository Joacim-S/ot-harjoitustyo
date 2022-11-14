import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)

    #Luontitesteja
    def test_kassapaate_luonti_toimii_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)


    #Kateismaksutesteja
    def test_syo_maukkaasti_kateisella_maksu_riittaa_kassaraha_ja_maukkaiden_maara_kasvaa_oikein(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
    
    def test_syo_maukkaasti_kateisella_vaihtoraha_oikeini_kun_maksu_riittaa(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500), 100)

    def test_syo_maukkaasti_kateisella_maksu_ei_riita_kassaraha_tai_maukkaat_ei_kasva(self):
        self.kassa.syo_maukkaasti_kateisella(350)

        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kateisella_maksu_ei_riita_palauttaa_koko_maksun(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(350), 350)

    def test_syo_edullisesti_kateisella_kassaraha_ja_edulliset_kasvaa_oikein_kun_summa_riittaa(self):
        self.kassa.syo_edullisesti_kateisella(500)
        
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    def test_syo_edullisesti_kateisella_vaihtoraha_oikein_kun_summa_rittaa(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(500), 260)

    def test_syo_edullisesti_kateisella_maksu_ei_riita_kassaraha_tai_maukkaat_ei_kasva(self):
        self.kassa.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kateisella_maksu_ei_riita_palauttaa_koko_maksun(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(200), 200)

    
    #Korttimaksutesteja
    def test_syo_maukkaasti_kortilla_saldo_riittaa(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_saldo_ei_riita(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(Maksukortti(10)), False)
        self.assertEqual(self.kassa.maukkaat, 0) 

    def test_syo_edullisesti_kortilla_saldo_riittaa(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_syo_edullisesti_kortilla_saldo_ei_riita(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(Maksukortti(10)), False)
        self.assertEqual(self.kassa.edulliset, 0)

    #Lataustesteja
    def test_lataa_rahaa_kortille_lataa_positiivisen_summan_oikein_ja_lisaa_kassaan_oikean_summan(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kortti.saldo, 1100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100100)

    def test_lataa_rahaa_kortille_lataa_negatiivisella_summalla_ei_tehda_mitaan(self):
            self.kassa.lataa_rahaa_kortille(self.kortti, -100)
            self.assertEqual(self.kortti.saldo, 1000)
            self.assertEqual(self.kassa.kassassa_rahaa, 100000)
