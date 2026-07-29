# Exam_Variant_D_Solution.py

# =============================================================================
# Question 1 – Login system with limited attempts
# =============================================================================

def question1():
    username = "admin"
    password = "secret"

    attempts = 3
    results = []

    for i in range(attempts):
        user = input(f"Attempt {i+1}/{attempts}: Username: ")
        pwd = input(f"Attempt {i+1}/{attempts}: Password: ")

        if user == username and pwd == password:
            print("Login successful!")
            results.append("success")
            break
        else:
            print("Login failed!")
            results.append("fail")
    else:
        print("Account locked! Too many failed attempts.")

    print("Attempt results:", results)


# =============================================================================
# Question 2 – Extended FizzBuzz
# =============================================================================

def question2():
    counts = {}

    for i in range(1, 61):
        label = ""
        if i % 3 == 0:
            label += "Fizz"
        if i % 5 == 0:
            label += "Buzz"
        if i % 7 == 0:
            label += "Pop"

        if label:
            output = label
        else:
            output = str(i)

        counts[output] = counts.get(output, 0) + 1
        print(output)

    print("\nFinal counts:")
    for label, count in sorted(counts.items()):
        print(f"  {label}: {count}")


# =============================================================================
# Question 3 – Data cleaning function
# =============================================================================

def clean_list(values: list) -> list:
    seen = set()
    cleaned = []

    for val in values:
        # Handle strings: strip whitespace
        if isinstance(val, str):
            val = val.strip()
            # Drop empty strings after stripping
            if val == "":
                continue
            # Convert numeric strings
            try:
                if '.' in val:
                    val = float(val)
                else:
                    val = int(val)
            except ValueError:
                pass  # Keep as string if not numeric
        elif isinstance(val, (int, float)):
            pass  # Keep numeric values
        elif val is None:
            continue  # Remove None

        # Remove duplicates while preserving order
        # Use a hashable representation for seen check
        if isinstance(val, float):
            key = ('float', val)
        elif isinstance(val, int):
            key = ('int', val)
        else:
            key = ('str', val)

        if key not in seen:
            seen.add(key)
            cleaned.append(val)

    return cleaned


def question3():
    mixed_input = [
        "  hello  ", "world", None, " 42 ", "3.5", "hello",
        "", "  ", 10, None, "10", 3.5, "python"
    ]

    print("Original:", mixed_input)
    cleaned = clean_list(mixed_input)
    print("Cleaned: ", cleaned)


# =============================================================================
# Question 4 – Student averages from nested dictionary
# =============================================================================

def question4():
    students = {
        "Anna": {"math": 1.7, "python": 1.3, "stats": 2.0},
        "Ben": {"math": 2.7, "python": 2.0, "stats": 2.3},
        "Lena": {"math": 1.0, "python": 1.3, "stats": 1.7},
        "Mark": {"math": 3.0, "python": 2.7, "stats": 2.3}
    }

    # 1. Compute and print each student average
    student_avgs = {}
    for name, grades in students.items():
        avg = sum(grades.values()) / len(grades)
        student_avgs[name] = avg
        print(f"{name}: {avg:.2f}")

    # 2. Compute and print subject averages
    subjects = ["math", "python", "stats"]
    subject_avgs = {}
    for subject in subjects:
        total = sum(s[subject] for s in students.values())
        subject_avgs[subject] = total / len(students)
        print(f"{subject} average: {subject_avgs[subject]:.2f}")

    # 3. Print the best student (lowest average)
    best = min(student_avgs, key=student_avgs.get)
    print(f"Best student: {best} (avg: {student_avgs[best]:.2f})")


# =============================================================================
# Question 5 – OOP: Inventory system
# =============================================================================

class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self) -> float:
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product):
        if product.name in self.products:
            self.products[product.name].quantity += product.quantity
        else:
            self.products[product.name] = product
        print(f"Added: {product.name} (qty: {product.quantity})")

    def sell(self, name: str, amount: int):
        if name not in self.products:
            print(f"Product '{name}' not found.")
            return
        product = self.products[name]
        if product.quantity < amount:
            print(f"Insufficient stock for '{name}'. Available: {product.quantity}")
            return
        product.quantity -= amount
        print(f"Sold {amount}x '{name}'. Remaining: {product.quantity}")

    def restock(self, name: str, amount: int):
        if name not in self.products:
            print(f"Product '{name}' not found.")
            return
        self.products[name].quantity += amount
        print(f"Restocked '{name}' by {amount}. New qty: {self.products[name].quantity}")

    def inventory_value(self) -> float:
        total = sum(p.total_value() for p in self.products.values())
        print(f"Total inventory value: ${total:.2f}")
        return total

    def low_stock(self, threshold: int = 5) -> list:
        low = [p for p in self.products.values() if p.quantity < threshold]
        if low:
            print(f"Low stock products (threshold={threshold}):")
            for p in low:
                print(f"  {p.name}: {p.quantity}")
        else:
            print("No low stock products.")
        return low


def question5():
    inventory = Inventory()

    # Add products
    p1 = Product("Laptop", 999.99, 10)
    p2 = Product("Mouse", 19.99, 50)
    p3 = Product("Keyboard", 49.99, 3)
    p4 = Product("Monitor", 299.99, 7)

    inventory.add_product(p1)
    inventory.add_product(p2)
    inventory.add_product(p3)
    inventory.add_product(p4)

    # Sell some items
    inventory.sell("Laptop", 3)
    inventory.sell("Mouse", 10)
    inventory.sell("Keyboard", 2)

    # Restock
    inventory.restock("Keyboard", 10)

    # Total value
    inventory.inventory_value()

    # Low stock check
    inventory.low_stock(threshold=5)


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("Question 1 – Login system")
    print("=" * 50)
    question1()

    print("\n" + "=" * 50)
    print("Question 2 – Extended FizzBuzz")
    print("=" * 50)
    question2()

    print("\n" + "=" * 50)
    print("Question 3 – Data cleaning")
    print("=" * 50)
    question3()

    print("\n" + "=" * 50)
    print("Question 4 – Student averages")
    print("=" * 50)
    question4()

    print("\n" + "=" * 50)
    print("Question 5 – Inventory system")
    print("=" * 50)
    question5()
