import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_rahamaara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myytyjen_lounaiden_maara_oikea(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)
    
    def test_kateisosto_toimii_edullisilla_kun_tarpeeksi_rahaa(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_toimii_edullisilla_kun_ei_tarpeeksi_rahaa(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_toimii_maukkailla_kun_tarpeeksi_rahaa(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_toimii_maukkailla_kun_ei_tarpeeksi_rahaa(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 300)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_toimii_edullisilla_kun_tarpeeksi_rahaa(self):
        kortti = Maksukortti(300)
        lapi = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(kortti.saldo, 60)
        self.assertEqual(lapi, True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_toimii_edullisilla_kun_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(200)
        lapi = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(lapi, False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_toimii_maukkailla_kun_tarpeeksi_rahaa(self):
        kortti = Maksukortti(500)
        lapi = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(lapi, True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_toimii_maukkailla_kun_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(300)
        lapi = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(kortti.saldo, 300)
        self.assertEqual(lapi, False)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_ladattaessa_saldo_muuttuu_ja_kassa_kasvaa(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, 500)

        self.assertEqual(kortti.saldo, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_kortin_saldo_ja_kassa_ei_muutu_jos_liian_vahan_rahaa(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, -1)

        self.assertEqual(kortti.saldo, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)