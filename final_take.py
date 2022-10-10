class Property:
    def __init__(self):
        self.rentIncome = {}
        self.expenses = {}
        self.investment = {}
        self.cashflow = 0
    
    def incoming(self):
        response = input("How much are/will you charge for rent on this property?: ")
        self.rentIncome['Rental Income'] = float(response)
    def theExpenses(self):
        mortgage = input("How much is your mortgage?: ")
        self.expenses["Mortgage"] = float(mortgage)
        tax_value = input("Please enter the property's monthly tax: ")
        self.expenses["Property Taxes"] = float(tax_value)
        insur_value = input("How much is your monthly insurance on the property?: ")
        self.expenses["Insurance"] = float(insur_value)
        # vacancy = (self.rentIncome * 0.05)
        # self.expenses["Vacancy"] = float(vacancy)
        # repairs = (self.rentIncome * 0.025)
        # self.expenses["Repairs"] = float(repairs)
        # capEx = (self.rentIncome * 0.05)
        # self.expenses["Capital Expenses"] = float(capEx)
        # propMGMT = (self.rentIncome * 0.1)
        # self.expenses["Property Manager"] = float(propMGMT)
        # print("\n5 percent of your Rental Income will be set aside for vacancy.")
        # print("\n2.5 percent will be taken out for monthly repairs.")
        # print("\n5 percent is taken out for Capital Expendature.")
        # print("\n10 percent has been set aside for Property Management")
        # print("\nIf you wish to ammend these numbers, find another ROI calculator")
        utilities_response = input("\nAre renters paying for utilities? Yes[y]|No[n]: ").lower()
        if utilities_response == 'n':
            electricity = input("How much is your electricity every month?: ")
            self.expenses["Electrity"] = float(electricity)
            water = input("Enter in your monthly water bill: ")
            self.expenses["water"] = float(water)
            sewer = input("Monthly sewer bill?: ")
            self.expenses["Sewer"] = float(sewer)
            garbage = input("Enter you monthly waste bill: ")
            self.expenses["Garbage"] = float(garbage)
            gas = input("How much is your gas bill per month?: ")
            self.expenses["Gas"] = float(gas)
        else:
            print("Good call")
    def theInvestment(self):
        dp_value = input("How much was your down payment?: ")
        self.investment["Down Payment"] = float(dp_value)
        cc_value = input("Please enter the amount of your Closing Cost: ")
        self.investment["Closing Cost"] = float(cc_value)
        rh_value = input("Please provide any Rehab cost you spent/planning to spend on the property: ")
        self.investment["Rehab"] = float(rh_value)
    def ROI(self):
        self.calcCflow()
        annualCflow = self.cashflow * 12
        total_investment = 0
        for num in self.investment.values():
            total_investment += num
        roi = (annualCflow/total_investment) * 100
        self.result(roi)
    def Cashflow(self):
        rental_income = 0
        expenses = 0
        for total in self.rentIncome.values():
            rental_income += total
        for total in self.expenses.values():
            expenses += total
        self.cashflow = rental_income - expenses
    def result(self,roi):
        print(f"Your Return on Investment percentage is: {roi}%")


ROI = Property()

def runnit():
    ROI.incoming()
    ROI.theExpenses()
    ROI.theInvestment()
    ROI.calcROI()
runnit()