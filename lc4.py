def happy(a):
    count = 0
    while (a != 1 and count < 100):
        s = 0
        while (a > 0):
            k = a % 10
            s += (k ** 2)
            a //= 10
        a = s
        count += 1
    return a == 1
def InRange(a, b):
    print("Happy numbers between "+ str(a) + " and " + str(b) + " = ")

    for i in range(a, b + 1):
        num = i
        if (happy(a)):
            print(i)
def first_n(n):
    count = 0
    a = 1
    print("First "+str(n)+" happy numbers = ")
    while (count < n):
        if (happy(a)):
            print(a)
            count += 1
        a += 1
n1 = int(input("Enter a number = "))
checking = happy(n1)
if (checking == 1):
    print(str(n1) + " is a happy number")
else:
    print(str(n1) + " is not a happy number")
n2 = int(input("Enter the starting number = "))
n3 = int(input("Enter the ending number = "))
range(n2, n3)
n4 = int(input("Happy numbers needed = "))
first_n(n4)