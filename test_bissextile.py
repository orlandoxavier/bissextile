import unittest
import bissextile


class BissextileYearTest(unittest.TestCase):
    def test_2000_is_bissextile(self):
        self.assertTrue(bissextile.is_bissextile(2000))

    def test_2004_is_bissextile(self):
        self.assertTrue(bissextile.is_bissextile(2004))

    def test_2016_is_bissextile(self):
        self.assertTrue(bissextile.is_bissextile(2016))

    def test_1998_is_bissextile(self):
        self.assertFalse(bissextile.is_bissextile(1998))

    def test_2014_is_bissextile(self):
        self.assertFalse(bissextile.is_bissextile(2014))

    def test_2015_is_bissextile(self):
        self.assertFalse(bissextile.is_bissextile(2015))


class NumberDivisibleByParamaterTest(unittest.TestCase):
    """Testa a divisão igualitária de um número por outro"""

    # Divisões por 4
    def test_4_divisivel_por_4(self):
        self.assertTrue(bissextile.are_divisible(4, 4))

    def test_16_divisivel_por_4(self):
        self.assertTrue(bissextile.are_divisible(16, 4))

    def test_20_divisivel_por_4(self):
        self.assertTrue(bissextile.are_divisible(20, 4))

    def test_10_divisivel_por_4(self):
        self.assertFalse(bissextile.are_divisible(10, 4))

    def test_30_divisivel_por_4(self):
        self.assertFalse(bissextile.are_divisible(30, 4))

    def test_70_divisivel_por_4(self):
        self.assertFalse(bissextile.are_divisible(70, 4))

    # Divisões por 100
    def test_100_divisivel_por_100(self):
        return self.assertTrue(bissextile.are_divisible(100, 100))

    def test_1000_divisivel_por_100(self):
        return self.assertTrue(bissextile.are_divisible(1000, 100))

    def test_15600_divisivel_por_100(self):
        return self.assertTrue(bissextile.are_divisible(15600, 100))

    def test_240_divisivel_por_100(self):
        return self.assertFalse(bissextile.are_divisible(240, 100))

    def test_15650_divisivel_por_100(self):
        return self.assertFalse(bissextile.are_divisible(15650, 100))

    def test_201150_divisivel_por_100(self):
        return self.assertFalse(bissextile.are_divisible(201150, 100))

    # Divisões por 400
    def test_400_divisivel_por_400(self):
        return self.assertTrue(bissextile.are_divisible(400, 400))

    def test_1600_divisivel_por_400(self):
        return self.assertTrue(bissextile.are_divisible(1600, 400))

    def test_20000_divisivel_por_400(self):
        return self.assertTrue(bissextile.are_divisible(20000, 400))

    def test_1000_divisivel_por_400(self):
        return self.assertFalse(bissextile.are_divisible(1000, 400))

    def test_3400_divisivel_por_400(self):
        return self.assertFalse(bissextile.are_divisible(3400, 400))

        return self.assertFalse(bissextile.are_divisible(21400, 400))


if __name__ == '__main__':
    unittest.main()