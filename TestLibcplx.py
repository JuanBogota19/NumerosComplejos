import Libcplx as lc
import unittest

class TestCplxOperations(unittest.TestCase):

    def test_sumacplx(self):
        suma = lc.suma_cplx((3,2),(-5, 5.2))
        self.assertAlmostEqual(suma[0], -2)
        self.assertAlmostEqual(suma[1], 7.2)

    def test_sumacplx(self):
        suma = lc.suma_cplx((4,2),(4, 5))
        self.assertAlmostEqual(suma[0], 8)
        self.assertAlmostEqual(suma[1], 7)

    def test_multicplx(self):
        multip = lc.mult_cplx((3,2),(-5, 5.2))
        self.assertAlmostEqual(multip[0], -25.4)
        self.assertAlmostEqual(multip[1], 5.6)

    def test_multicplx(self):
        multip = lc.mult_cplx((4,3),(5, 5.2))
        self.assertAlmostEqual(multip[0], 4.4)
        self.assertAlmostEqual(multip[1], 35.8)

    def test_resta(self):
        resta = lc.rest_cplx((3,2),(-5, 5.2))
        self.assertAlmostEqual(resta[0], 8)
        self.assertAlmostEqual(resta[1], -3.2)

    def test_resta(self):
        resta = lc.rest_cplx((4,2),(5, 5.2))
        self.assertAlmostEqual(resta[0], -1)
        self.assertAlmostEqual(resta[1], -3.2)

    def test_div(self):
        div = lc.div_plx((2,-4),(4,-2))
        self.assertAlmostEqual(div[0], 0.8)
        self.assertAlmostEqual(div[1], -0.6)

    def test_div(self):
        div = lc.div_plx((2,-4),(-4,2))
        self.assertAlmostEqual(div[0], -0.8)
        self.assertAlmostEqual(div[1], 0.6)

    def test_modul(self):
        self.assertAlmostEqual(lc.modul_cplx((7,2)), 7.3)

    def test_modul(self):
        self.assertAlmostEqual(lc.modul_cplx((1,6)), 6.08276253)

    def test_conj(self):
        conj = lc.conj_cplx((2,-4))
        self.assertAlmostEqual(conj[0], 2)
        self.assertAlmostEqual(conj[1], 4)

    def test_conj(self):
        conj = lc.conj_cplx((4,5))
        self.assertAlmostEqual(conj[0], 4)
        self.assertAlmostEqual(conj[1], -5)

    def test_polar(self):
        self.assertAlmostEqual(lc.polar_cplx((4,5)), 9.0)

    def test_polar(self):
        self.assertAlmostEqual(lc.polar_cplx((5,5)), 10.0)

    def test_fase(self):
        self.assertAlmostEqual(lc.fase_cplx((1,9)), 1.46013911)

    def test_fase(self):
        self.assertAlmostEqual(lc.fase_cplx((4,9)), 1.15257200)


if __name__ == '__main__':
    unittest.main()
