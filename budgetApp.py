##### CLASS INITIALIZATION FOR BUDGET APP #####
class Budget:
    def __init__(self, itemName, funds):
        self.itemName = itemName
        self.funds = funds

##### METHODS #####
    def deposits(self, deposit): #adds amount (*deposit) entered and updates the balance of category
        self.deposit = int(deposit)
        self.funds = int(self.funds) + self.deposit
        self.checkBalance()

    def withdrawals(self, withdraw): #deducts amount (*withdraw) entered and updates the balance of category
        self.withdraw = int(withdraw)
        self.funds = int(self.funds) - self.withdraw
        self.checkBalance()

    def transfers(self, amount, recipient): #deducts *amount entered from the category (*self) calling the function and adds to category (*recipient) passed as argument
        self.amount = int(amount)
        recipient.funds = int(recipient.funds) + self.amount
        self.funds = int(self.funds) - self.amount
        self.checkBalance()
        recipient.checkBalance()
        

    def checkBalance(self): #checks balance of category that calls the function
        print(f'Your budget balance for {self.itemName} is ${self.funds}')




####### INSTANTIATED OBJECTS #######
food1 = Budget('junk and beverages', '100')
food2 = Budget('bread, vegies and meat', '200')
clothing1 = Budget('casual wears', '500')
clothing2 = Budget('corprate wears', '500')
entertainment1 = Budget('parties', '150')
entertainment2 = Budget('netflix', '50')



##### RUNNING APP FUNCTIONS #####
entertainment2.checkBalance()
entertainment1.withdrawals(50)
clothing2.deposits(100)
clothing1.transfers(50, food1)
food2.checkBalance()
