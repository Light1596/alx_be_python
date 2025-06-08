def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    number = 1
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            name = input("Enter item to add: ")
            shopping_list.append(name)
            print(f"{name} added")
        elif choice == '2':
            # Prompt for and remove an item
            item_to_remove = input("Enter the item to remove: ")
            print(f'{item_to_remove} successfully removed from the cart')
        elif choice == '3':
            # Display the shopping list
            print("Here are the items on your list   ")
            for item in shopping_list:
                print(f" {number} . {item}  ")
                number += 1
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()