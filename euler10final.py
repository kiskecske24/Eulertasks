numbers=[]
number=1
while number<2000000:
    isPrime=True
    for x in range(2, number-1):
        if number%x==0:
            isPrime=False
    if isPrime==True:
        numbers.append(number)
    number=number+1
    print(number)
print(numbers)
print(sum(numbers))
