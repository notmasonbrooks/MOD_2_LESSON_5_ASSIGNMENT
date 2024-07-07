
shopping_list = []

def option():
    while True:
        print("\nPlease select an option:")
        print("1. Add item to shopping list")
        print("2. Remove item from shopping list")
        print("3. View shopping list.")
        print("4. Quit.")
        choice = input("Enter your choice here: ")
        if choice == "1":
            user_input = input("\nPlease enter the name of the item you would like to add to the shopping list:")
            shopping_list.append(user_input)
            print(f"\n{user_input} added to the shopping list.")
        elif choice == "2":
            user_input = input("\nPlease enter the name of the item you would like to remove from the list: ")
            if user_input not in shopping_list:
                print(f"\n{user_input} was not found in the shopping list.")
            else:
                shopping_list.remove(user_input)
                print(f"\n{user_input} removed from the shopping list.")
        elif choice == "3":
            print("\nShopping List:")
            for item in shopping_list:
                print(f"- {item}")
        elif choice == "4":
            break
        else:
            print("Invalid input. Please select from '1'-'4' on the homepage.")
            
option()

