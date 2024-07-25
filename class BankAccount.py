class BankAccount:
    def __init__(self, account_num, bal):
        self.account = account_num
        self.bal = bal
    
    def deposit(self, amount):
        self.bal = amount
        print(self.bal)
        
    def withdraw(self, amount):
        self.bal = amount
        print(self.bal)
        
    def chack_bal(self):
        print("your balance is " + str(self.bal))
        
my_account= BankAccount(12, 1000000000)
my_account.chack_bal()
my_account.deposit(1000000)
    
        
class ATM:
    def __init__(self, bankaccount):
        self.accounts = []
    
    def add_account(self, bank_acc):
        self.account.append(bank_acc)
        
    def view(self):
        for a in self.accounts:
            print(a.account_num)
    
atm= ATM()
atm.veiw()  
gabe = BankAccount("123", 30)
snikitha = BankAccount("456", 70000000)
atm.add_account(gabe)
atm.add_account(snikitha)
atm.veiw()






#class BankAccount
#1) constructor -->This is a fancy way of saying, make a def __int__()function
# *account num & bal 
#deposit func (self, amount )
#withdraw func(self, amount )
#check bal func(self)
