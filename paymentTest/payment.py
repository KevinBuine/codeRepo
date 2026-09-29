# expense tracker

print('*****************************')
print('')
print('Expense tracker pro')
print('')
print ('')

expenses = []

def show_expenses():
            print('Expenses list:')
            for index, expense_record in enumerate (expenses, start =1):
                print(f"{index}. {expense_record['expense']} - ${expense_record['cost']}")
                

while True:

    choice = input('welcome to expense tracker pro. what operation do you want to perform? \n1. Add expense \n2. view all expenses \n3. view total spending \n4. searcch expenses \n 5. delete an expense \n6. exit \n')

    if choice == '6':
        break

    elif choice == '1':
        
        while True:
        
            print('Enter your expenses')
            expense = input('Expense: ')
            expense.upper()
            cost = float(input('Cost: '))
            expense_record = {
            "expense": expense, 
            "cost": cost
            }
            expenses.append(expense_record)
            print(f'added {expense}')

            response = input('Do you want to add another expense? 1. Yes  2. No')
            if response == '2':
                break

#view expenses

    elif choice == '2':
         show_expenses()
         
       
#view total expenses


    elif choice == '3':
        total = 0
        for expense_record in expenses:
            total += expense_record["cost"]
        print(f'Total expenses is: $ {total}')

    #search expensess

    elif choice == '4':
        while True:    
            show_expenses()
            query = input('enter the expense you want to search for: ')
            query = query.lower()
            found_expense = []

            for expense_record in expenses:
                if query == expense_record['expense'].lower():
                    found_expense.append(expense_record)

            if found_expense:
                print('found....')
                print(found_expense)
            else:
                print('Not found......')

            option = input('Do you want to search again? 1. yes 2. no')
            if option == '2':
                break

    # delete an expense
    # elif choice == '5':
    #     pick = input('enter an expense to delete: ')
    #     pick.upper()
    #     for expense_record in expenses:
    #         if pick == expense_record['expenses']:
    #             expenses.remove(expense_record)
    #             break
    
    elif choice == '5':
        show_expenses()
        pick = int(input('Enter the number of the expense you want to delete: '))
        del expenses[pick - 1]
        print('deleted...')

    else:
        print("invalid selection. try again")



print('Thank you. Goodbye')  
