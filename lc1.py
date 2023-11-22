a = int(input("Enter a 4-digit number = "))
sum = 0
for i in str(a):
    sum = sum+(int(i))

odd = 1
for j in range(1, len(str(a)), 2):
    odd = odd * (int(str(a)[j]))
even = 1
for j in range(0, len(str(a)), 2):
    even = even * (int(str(a)[j]))

dif = odd - even

rev = 0
while a > 0:
    digit = a % 10
    rev = rev * 10 + digit
    a = a//10

print(" Sum of digits = "+str(sum))
print(" Reverse = "+str(rev))
print(" Difference between the product = "+str(dif))