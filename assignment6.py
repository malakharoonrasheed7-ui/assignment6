# Initial state
pin = 1234
balance = 50000

# Step 1: Pin authentication
entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:
    print("\nWelcome to Bank ATM")
    
    while True:
        print("\nChoose an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")
        
        choice = input("\nEnter choice: ")
        
        if choice == '1':
            print(f"Your balance is: {balance}")
            
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"Successfully deposited {amount}. New balance: {balance}")
            else:
                print("❌ Invalid amount.")
                
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("❌ Insufficient Balance")
            elif amount <= 0:
                print("❌ Invalid amount.")
            else:
                balance -= amount
                print(f"Please collect your cash. New balance: {balance}")
                
        elif choice == '4':
            old_pin = int(input("Enter old PIN: "))
            if old_pin == pin:
                new_pin = int(input("Enter new 4-digit PIN: "))
                if new_pin != pin and 1000 <= new_pin <= 9999:
                    pin = new_pin
                    print("✅ PIN changed successfully.")
                else:
                    print("❌ Invalid new PIN (must be 4 digits and different from old PIN).")
            else:
                print("❌ Wrong old PIN.")
                
        elif choice == '5':
            print("Thank you for using our ATM. Goodbye!")
            break
            
        else:
            print("❌ Invalid option. Please try again.")
else:
    print("❌ Access Denied: Incorrect PIN.")
