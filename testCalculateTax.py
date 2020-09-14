import unittest
import calculateTax as ct


class testCalculateTax(unittest.TestCase):

    def setUp(self):
        self.calculateTaxes = ct.calculateTax(30000)

    def test_calculatePersonalAllowance(self):
        self.assertEqual(self.calculateTaxes.setPersonalAllowance(5000), 12500)
        self.assertEqual(self.calculateTaxes.setPersonalAllowance(30000), 12500)
        self.assertEqual(self.calculateTaxes.setPersonalAllowance(100000), 12500)
        self.assertEqual(self.calculateTaxes.setPersonalAllowance(125000), 0)

    def test_calculateTaxableAmount(self):
        taxBracketIncome = [150000, 50000, 12500]
        taxPercentageIncome = [0.45, 0.4, 0.2]
        self.assertEqual(self.calculateTaxes.calculateTaxableAmount(5000, taxBracketIncome, taxPercentageIncome),
                         0)
        self.assertEqual(self.calculateTaxes.calculateTaxableAmount(30000, taxBracketIncome, taxPercentageIncome),
                         3500)
        self.assertEqual(self.calculateTaxes.calculateTaxableAmount(70000, taxBracketIncome, taxPercentageIncome),
                         15500)

    def test_getTax(self):
        self.newTax = ct.calculateTax(0)
        self.assertEqual(self.newTax.getGrossPay(), 0)


if __name__ == '__main__':
    unittest.main()
