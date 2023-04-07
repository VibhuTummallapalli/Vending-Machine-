#entry message
Balance = 0j
Price = 0
item = ''
A1 = 0.50
A2 = 0.50
A3 = 0.50
A4 = 0.50
A5 = 0.50
B1 = 1.00
B2 = 1.00
B3 = 1.00
B4 = 1.00
B5 = 1.00
C1 = 1.50
C2 = 1.50
C3 = 1.50
C4 = 1.50
C5 = 1.50
D1 = 2.00
D2 = 2.00
D3 = 2.00
D4 = 2.00
D5 = 2.00
E1 = 2.50
E2 = 2.50
E3 = 2.50
E4 = 2.50
E5 = 2.50

Balance = float(input(("Welcome! Please put your bills and/or coins into the machine!")))

def entry(item):
   item = input('Enter the item')
   
def give_money(new_money):
    new_money= float(input('Enter money'))
    Balance = Balance + new_money

   
if Balance < 0.50:
    print("Insufficient funds")
    give_money(new_money)
else:
    entry(item)



#list of items
RowA = [A1, A2, A3, A4, A5]
RowB = [B1, B2, B3, B4, B5]
RowC = [C1, C2, C3, C4, C5]
RowD = [D1, D2, D3, D4, D5]
RowE = [E1, E2, E3, E4, E5]

#finding if balance is enough
if Balance < Price:
    print('Insufficient funds')
    entry(item)
else :
    print('Thankyou, enjoy your item')
    
