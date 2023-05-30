# program to check if the given number is prime or not
p=40
for i in range(2,p):
    if p%i==0:
        print("p is not prime number : ",p)
        break
else:
    print("p is prime number :",p)