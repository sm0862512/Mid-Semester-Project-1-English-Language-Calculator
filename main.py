Number1 = 0
Number2 = 0
Operators = 0
test = 0
test2 = 0

test2 = input("test2")

test = input("test")

test4 = input("test4")
test3 = (test2, test, test4)
print(test3)


Number1 = float(input("Enter number 1: "))

print(" + Sum.")
print(" - Difference.")
print(" * Product.")
print(" ^ Quotient.")
print(" / Divided by. ")

choice = int(input("Enter one of the Operators: "))
def menus(menu):
    choose = {
        1: 'Sum',
        2: 'Difference',
        3: 'Product',
        4: 'Quotient',
        5: 'Divide'
    }

    return choose.get(menu, "You entered an invalid number.")

Number2 = int(input("Enter number 2: "))

if choice == 1:
    sum = Number1 + Number2
    print(sum)
if choice == 2:
    difference = Number1 - Number2
    print(difference)
if choice == 3:
    Product = Number1 * Number2
    print(Product)
if choice == 4:
    Quotient = Number1 ^ Number2
    print(Quotient)
if choice == 5:
    Divide = Number1 / Number2
    print(Divide)