Number1 = 0
Number2 = 0
Operators = 0
test = 0
test2 = 0

test2 = int(input("test2"))

test = input("test")

test4 = int(input("test4"))
test3 = (test2, test, test4)
print(test3)


Number1 = float(input("Enter number 1: "))

print(" + Sum.")
print(" - Difference.")
print(" * Product.")
print(" ^ Quotient.")
print(" / Divided by. ")

choice = (input("Enter one of the Operators: "))
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

if Number1 == 0:
  print("Cant devide by 0 ERROR")
if Number2 == 0:
  print("Cant devide by 0 ERROR")

if choice == 1:
    sum = Number1 + Number2
    print (Number1, "Plus", Number2, "is")
    print(sum)
if choice == 2:
    difference = Number1 - Number2
    print (Number1, "Minus", Number2, "is")
    print(difference)
if choice == 3:
    Product = Number1 * Number2
    print (Number1, "Muktiplied by", Number2, "is")
    print(Product)
if choice == 4:
    Quotient = Number1 ^ Number2
    print (Number1, "To the power of", Number2, "is")
    print(Quotient)
if choice == 5:
    Divide = Number1 / Number2
    print(Divide)