# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 08:28:57 2021

@author: OLUWABUSUYI
"""

class budget:
    
    def __init__(self, name, dep_amt, with_amt, bal ):
        self.name = name
        self.dep_amt = dep_amt
        self.with_amt = with_amt
        self.bal  = bal
        
    def deposit(self):
        print (f'The {self.name} deposit is {self.dep_amt} ')
    
    def withdrawal(self):
        print (f'The {self.name} withdrawal is {self.with_amt}')
        
    def balance (self):
        print (f'The {self.name} balance is {self.bal}')
        
    def transfer (self):
        print (f'The maximum amount to be transferred from {self.name} to another category is {self.bal}')
        print (' ')
    


budget_1 = budget('food', 10000, 2000, 8000)
budget_1.deposit ()
budget_1.withdrawal()
budget_1.balance ()
budget_1.transfer()

budget_2 = budget('clothing', 5000, 2000, 3000)
budget_2.deposit ()
budget_2.withdrawal()
budget_2.balance ()
budget_2.transfer()

budget_3 = budget('entertainment', 1000, 500, 500)
budget_3.deposit ()
budget_3.withdrawal()
budget_3.balance ()
budget_3.transfer()
   