#Final Project for Programming 112 class at Seton Hall, simple and clean design to keep track of bank totals.
#Nothing too fancy compared to the Ray Tracer and other projects I have recently built.
class Bankaccount:
    total_accounts=0
    
    def __init__ (self):
        Bankaccount.total_accounts+=1
        self.accountnumber=Bankaccount.total_accounts #make a use of the number
    
       
class Savingsaccount(Bankaccount):
    
    
    def __init__ (self,money):
        super().__init__()
        self.startbalance(money)
        
    def startbalance(self,money):
        try:
            self.savingsbalance=int(money) #check that there is no string
        except:
            print('\n\nPlease enter a number for starting balance.')
            temp=input('How much would you like to deposit? ')
            self.startbalance(temp) #allow the user to try again until they enter a number
                  
    def deposit(self,money):
        try:
            self.savingsbalance+=money #no need to check for int will fail if its anything but
            print(self.savingsbalance)
        except:
            print('Deposit Failed\nPlease enter a number')
            temp=input('How much would you like to deposit? ')
            self.deposit(temp) #same idea as in __init__
        
    def withdraw(self,money):
        try:
            self.savingsbalance-=money
            if self.savingsbalance<=0:
                print('Overdraft Warning - a 25$ fee has been charged') #I could have made it fail instead but I am a bank so gotta squeeze that money out
                self.savingsbalance-=25
            print(self.savingsbalance)
        except:
            print('Withdraw Failed\nPlease enter a number')
            temp=input('How much would you like to withdraw? ')
            self.withdraw(temp)
    def get_balance(self):
        print(self.savingsbalance)
  
class Checkingaccount(Bankaccount):
    
    
    def __init__ (self,money):
        super().__init__()
        self.startbalance(money)
        
    def startbalance(self,money): #if I did this in the init function it upped the account numbers each time there was an error
        try:
            self.checkingbalance=int(money) #check that there is no string
        except:
            print('\n\nPlease enter a number for starting balance.')
            temp=input('How much would you like to deposit? ')
            self.startbalance(temp) #allow the user to try again until they enter a number
            
        
    def deposit(self,money):
        try:
            self.checkingbalance+=money #no need to check for int will fail if its anything but
            print(self.checkingbalance)
        except:
            print('Deposit Failed\nPlease enter a number')
            temp=input('How much would you like to deposit? ')
            self.deposit(temp) #same idea as in __init__
        
    def withdraw(self,money):
        try:
            self.checkingbalance-=money
            if self.checkingbalance<=0:
                print('Overdraft Warning - a 25$ fee has been charged') #I could have made it fail instead but I am a bank so gotta squeeze that money out
                self.checkingbalance-=25
            print(self.checkingbalance)
        except:
            print('Withdraw Failed\nPlease enter a number')
            temp=input('How much would you like to withdraw? ')
            self.withdraw(temp)
    def get_balance(self):
        print(self.checkingbalance)
     
Tim = Savingsaccount(2136)
Tim.deposit(20)
Tim.withdraw(453)
Tim.get_balance()

bob = Checkingaccount(8923)
bob.deposit(123)
bob.withdraw(78943)
bob.get_balance()
