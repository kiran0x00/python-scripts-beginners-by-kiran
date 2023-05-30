list =[10,13,14,16,18,19]

for i in list:
    if i%5==0:
        print("the 1st number divisible by 5 in list is : ", i)
        break
else:
    print("none is divisible by 5")