import random
# pre defined menu
menu = [['chicken',500],['mutton',1000 ],['fish',500],['panner',800],['coffee',100],['beer',800],['fish tikka',500]]
orders = [] #empty list

#FUNCTION TO DISPLAY THE LIST
def display_menu():
    print('MENU\n')
    index = 0
    while index < len(menu):
        print(index,'-',menu[index])
        index += 1
#FUNCTION TO PLACE THE ORDER 
def place_order():

    r1 = str(random.randint(0,9))
    r2 = str(random.randint(0,9))
    r3 = str(random.randint(0,9))
    r4 = str(random.randint(0,9))
    r5 = str(random.randint(0,9))
    orderid = r1+r2+r3+r4+r5 #RANDOM ORDER ID

    order_items = [] #EMPTY LIST

    while True:
            
            select = input('Choose the item no. to place order for,(E to End the order): ')
        
            if select.isalpha() == True:
                if select == 'e' or select == 'E':
                    break
                else:
                    print('Invalid selection!!')
            else:
                item_no = int(select)
                if item_no in range(len(menu)):
                    qty = int(input('Enter the quantity: '))
                    if qty > 0:
                        order_items.append({'Itemnumber': item_no, 'Quantity': qty})
                    else:
                        print('Quantity should be greater than 0.')
                else:
                    print('Check the item number selected!!.')
            
    
    order = {
        'Orderid': orderid,
        'Items': order_items,
    }
    orders.append(order)
    print('\nOrder',orderid,'placed successfully!')
    print('Order Details:',order,'\n')    
    print('Total Order Details:',orders,'\n')  

def display_orders():

    if not orders:
        print('No orders placed yet!')
        return
    
    for order in orders:
        print('Order ID:',order['Orderid'])
        for item in order['Items']:
            item_no = item['Itemnumber']
            qty = item['Quantity']
            item_name = menu[item_no][0]
            item_price = menu[item_no][1]
            print(item_name, '-', qty, 'x Rs',item_price, '= Rs',qty * item_price)
        total = 0
        for item in order['Items']:
            item_no = item['Itemnumber']
            qty = item['Quantity']
            total += menu[item_no][1] * qty
        print('Total: Rs',total)
        print()

def save_to_file():
    with open('TotalOrder.txt','w') as file:
        for order in orders:
            file.write("Order ID: " + str(order['Orderid']) + "\n")
            for item in order['Items']:
                item_no = item['Itemnumber']
                qty = item['Quantity']
                item_name = menu[item_no][0]
                item_price = menu[item_no][1]
                file.write(item_name + " - " + str(qty) + " x Rs" + str(item_price) + " = Rs" + str(qty * item_price) + "\n")
                total = 0
            for item in order['Items']:
                item_no = item['Itemnumber']
                qty = item['Quantity']
                total += menu[item_no][1] * qty
            file.write("Total: Rs" + str(total) + "\n\n")
    print("Orders saved to 'TotalOrder.txt' successfully.")

    print('*'*30)
print('Welcome To The Enchanted Fork!!')

while True:
    print('*'*30)
    print('1. Place Orders')
    print('2. Display orders + Bill')
    print('3. Save Order Details to .txt file')
    print('4. Exit')
    print('*'*30)

    choice = input('Enter your choice')
    print('Your choice is:',choice,'\n')

    if int(choice) == 1:
        display_menu()
        place_order()
    elif int(choice) == 2:
        display_orders()
    elif int(choice) == 3:
        # display_orders()
        save_to_file()
    elif int(choice) == 4:
        break
    else:
        print('Invalid Selection')