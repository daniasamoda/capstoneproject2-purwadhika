# =========================
# WAREHOUSE STOCK SYSTEM
# =========================

warehouse = [
    {
        "item_id": "A001",
        "item_name": "Indomie",
        "category": "Food",
        "stock": 100,
        "price": 3000,
        "supplier": "Indofood"
    },
    {
        "item_id": "A002",
        "item_name": "Aqua",
        "category": "Drink",
        "stock": 50,
        "price": 5000,
        "supplier": "Danone"
    }
]

# =========================
# DISPLAY MENU
# =========================
def display_menu():
    print("\n=== WAREHOUSE STOCK SYSTEM ===")
    print("1. Display Data")
    print("2. Add Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Exit")


# =========================
# READ DATA
# =========================
def read_data():
    while True:
        print("\n--- READ MENU ---")
        print("1. Show All Data")
        print("2. Search by Item ID")
        print("3. Back to Main Menu")

        choice = input("Choose menu: ")

        if choice == "1":
            if len(warehouse) == 0:
                print("No data available")
            else:
                for item in warehouse:
                    print(item)

        elif choice == "2":
            item_id = input("Enter Item ID: ")
            found = False

            for item in warehouse:
                if item["item_id"] == item_id:
                    print(item)
                    found = True
                    break

            if not found:
                print("Data not found")

        elif choice == "3":
            break

        else:
            print("Invalid option!")


# =========================
# CREATE DATA
# =========================
def create_data():
    print("\n--- ADD DATA ---")

    item_id = input("Enter Item ID: ")

    # Check duplicate
    for item in warehouse:
        if item["item_id"] == item_id:
            print("Data already exists!")
            return

    item_name = input("Enter Item Name: ")
    category = input("Enter Category: ")
    
    try:
        stock = int(input("Enter Stock: "))
        price = int(input("Enter Price: "))
    except:
        print("Stock and Price must be numbers!")
        return

    supplier = input("Enter Supplier: ")

    confirm = input("Save data? (y/n): ")

    if confirm.lower() == "y":
        warehouse.append({
            "item_id": item_id,
            "item_name": item_name,
            "category": category,
            "stock": stock,
            "price": price,
            "supplier": supplier
        })
        print("Data successfully added!")
    else:
        print("Cancelled.")


# =========================
# UPDATE DATA
# =========================
def update_data():
    print("\n--- UPDATE DATA ---")

    item_id = input("Enter Item ID: ")
    found = False

    for item in warehouse:
        if item["item_id"] == item_id:
            found = True
            print("Current Data:", item)

            print("\nWhich field to update?")
            print("1. Name")
            print("2. Category")
            print("3. Stock")
            print("4. Price")
            print("5. Supplier")

            choice = input("Choose: ")

            if choice == "1":
                item["item_name"] = input("New Name: ")
            elif choice == "2":
                item["category"] = input("New Category: ")
            elif choice == "3":
                try:
                    item["stock"] = int(input("New Stock: "))
                except:
                    print("Must be number!")
                    return
            elif choice == "4":
                try:
                    item["price"] = int(input("New Price: "))
                except:
                    print("Must be number!")
                    return
            elif choice == "5":
                item["supplier"] = input("New Supplier: ")
            else:
                print("Invalid choice")
                return

            print("Data successfully updated!")
            break

    if not found:
        print("Data not found!")


# =========================
# DELETE DATA
# =========================
def delete_data():
    print("\n--- DELETE DATA ---")

    item_id = input("Enter Item ID: ")
    found = False

    for item in warehouse:
        if item["item_id"] == item_id:
            found = True

            confirm = input("Are you sure to delete? (y/n): ")

            if confirm.lower() == "y":
                warehouse.remove(item)
                print("Data successfully deleted!")
            else:
                print("Cancelled.")
            break

    if not found:
        print("Data not found!")


# =========================
# MAIN PROGRAM
# =========================
def main():
    while True:
        display_menu()
        choice = input("Choose menu: ")

        if choice == "1":
            read_data()
        elif choice == "2":
            create_data()
        elif choice == "3":
            update_data()
        elif choice == "4":
            delete_data()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid option!")


# RUN PROGRAM
main()


















