print ("\t\tHello")
print ("lolo\\\123456\\\78910")
print ("\b hello \b hello")

def add(a, b):
    print ("Your answer is:")
    print (a, "+", b, "=",a + b)
    return 

def sub(c, d):
    print ("Your answer is:")
    print (c, "-", d, "=",c - d)
    return

def multi(e, f):
    print ("Your answer is:")
    print (e, "x", f, "=",e * f)
    return

def div(g: int, h: int):
    if (h == 0):
        print ("You cannot divide by zero.")
    else: 
        print ("Your answer is:")
        z = (int) (g / h)
        y = (int) (g % h)
        print (g, "/", h, "=",z, " R ",y)
    return
def menu():
    choices = ['1', '2', '3', '4', '5']
    choice = '0'
    readytoquit = False
    while not readytoquit:
        while not readytoquit and choice not in choices:
            print('What would you like to do?')
            print(' 1. Add')
            print(' 2. Subtract')
            print(' 3. Multiply')
            print(' 4. Divide')
            print(' 5. Quit')
            choice = input('Please type 1, 2, 3, 4, or 5 and press Enter. ')
            if choice == '1':
                a = float(input('Please type the first number you want to add: '))
                z = float(input('Please type the second number you want to add: '))
                add(a, z)
            elif choice == '2':
                b = float(input('Please type the number you want to subtract from: '))
                c = float(input('Please type the number you want to subtract: '))
                sub(b, c)
            elif choice == '3':
                numa = float(input('Please type the first factor: '))
                numb = float(input('Please type the second factor: '))
                multi(numa, numb)
            elif choice == '4':
                num1 = float(input('Please type the dividend: '))
                num2 = float(input('Please type the divisor: '))
                div(num1, num2)
            elif choice == '5':
                readytoquit = True
            choice = '0'
    return

menu()
            

