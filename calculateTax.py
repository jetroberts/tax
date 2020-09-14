import matplotlib.pyplot as plt


class calculateTax:
    def __init__(self, income):
        self.income = income
        self.personalAllowance = 0
        self.tax = 0
        self.taxBracketIncome = [150000, 50000, self.personalAllowance]
        self.taxPercentageIncome = [0.45, 0.4, 0.2]
        self.taxBracketNationalInsurance = [50024, 2196]
        self.taxPercentageNationalInsurance = [0.02, 0.12]

    def getGrossPay(self):
        self.getTax()
        return self.income - self.tax

    def getTax(self):
        self.personalAllowance = self.setPersonalAllowance(self.income)
        self.tax = self.calculateTaxableAmount(self.income, self.taxBracketIncome, self.taxPercentageIncome)
        self.tax += self.calculateTaxableAmount(self.income, self.taxBracketNationalInsurance,
                                                self.taxPercentageNationalInsurance)

    @staticmethod
    def setPersonalAllowance(income):
        PERSONAL_ALLOWANCE_LIMIT_LOWER = 100000
        PERSONAL_ALLOWANCE_LIMIT_UPPER = 125000
        PERSONAL_ALLOWANCE = 12500

        if income < PERSONAL_ALLOWANCE_LIMIT_LOWER:
            return PERSONAL_ALLOWANCE
        elif PERSONAL_ALLOWANCE_LIMIT_LOWER <= income < PERSONAL_ALLOWANCE_LIMIT_UPPER:
            newPersonalAllowance = (PERSONAL_ALLOWANCE_LIMIT_UPPER - income) / 2
            return newPersonalAllowance
        else:
            return 0

    @staticmethod
    def calculateTaxableAmount(INCOME, TAXBRACKET, TAXPERCENTAGE):
        remainingIncome = INCOME
        tax = 0
        for index in range(len(TAXBRACKET)):
            if remainingIncome > TAXBRACKET[index]:
                taxAmount = remainingIncome - TAXBRACKET[index]
                tax += taxAmount * TAXPERCENTAGE[index]
                remainingIncome = TAXBRACKET[index]
        return tax


def createGraph(grossIncome, netIncome):
    plt.plot(grossIncome, netIncome)
    plt.show()


if __name__ == '__main__':
    UPPER_LIMIT = 100000
    STEP_SIZE = 100
    grossIncome = range(0, UPPER_LIMIT, STEP_SIZE)
    netIncome = []
    for i in grossIncome:
        grossIncomeAfterTax = calculateTax(i)
        netIncome.append(grossIncomeAfterTax.getGrossPay())

    createGraph(grossIncome, netIncome)
