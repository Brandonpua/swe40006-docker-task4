import json
import os

DATA_FILE = os.environ.get("DATA_FILE", "/data/expenses.json")


def load():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return []


def save(items):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(items, f, indent=2)


def main():
    items = load()
    print("=== Docker Expense Tracker (SWE40006 Task 4.4) ===")
    while True:
        print("\n1) Add expense  2) List expenses  3) Show total  4) Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            name = input("Description: ").strip()
            try:
                amount = float(input("Amount (RM): "))
            except ValueError:
                print("Invalid amount.")
                continue
            items.append({"name": name, "amount": amount})
            save(items)
            print("Saved.")
        elif choice == "2":
            if not items:
                print("No expenses yet.")
            for i, item in enumerate(items, 1):
                print(f"{i}. {item['name']} - RM{item['amount']:.2f}")
        elif choice == "3":
            print(f"Total: RM{sum(i['amount'] for i in items):.2f}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()