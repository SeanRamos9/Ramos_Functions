# Basic Food Ordering System

def display_menu():
    print("\nWelcome to Bahala na!!")
    print("\nMenu:")
    print("Foods:")
    print("1. Crispy Kare-Kare: ₱75")
    print("2. Hotsilog: ₱65")
    print("3. Liempo with rice: ₱94")
    print("Drinks:")
    print("4. Coke 1.5: ₱82")
    print("5. Sprite 1.5: ₱80")
    print("6. Royal 1.5: ₱87")
    print("7. Rice: ₱15")

def get_user_input(prompt, cast_type):
    
    while True:
        user_input = input(prompt).strip()
        if cast_type == int:
            if user_input.isdigit():
                return int(user_input)
            else:
                print("Invalid input. Please enter a valid number.")
        elif cast_type == float:
            if user_input.replace('.', '', 1).isdigit():  
                return float(user_input)
            else:
                print("Invalid input. Please enter a valid number.")

def main():
    # Menu prices
    prices = {
        1: 75,
        2: 65,
        3: 94,
        4: 82,
        5: 80,
        6: 87,
        7: 15,
    }

    # Display the menu
    display_menu()

    # Initialize total cost
    total_cost = 0

    # Take user input for the order
    while True:
        choice = get_user_input("\nEnter the number of the item you'd like to order (or 0 to finish): ", int)
        if choice == 0:
            break
        elif choice in prices:
            total_cost += prices[choice]
            print(f"Added item {choice} to your order. Current total: ₱{total_cost:.2f}")
        else:
            print("Invalid choice. Please select a valid menu item.")

    # Ensure at least one item was ordered
    if total_cost == 0:
        print("\nYou did not order anything. Goodbye!")
        return

    # Process payment
    while True:
        cash = get_user_input(f"\nYour total is ₱{total_cost:.2f}. Enter the amount of cash rendered: ", float)
        if cash >= total_cost:
            change = cash - total_cost
            print(f"\nThank you! Your change is ₱{change:.2f}. Enjoy!")
            break
        else:
            print("Insufficient cash.")








