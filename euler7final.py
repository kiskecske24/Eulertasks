numbers=[]
number=1
i=1
while len(numbers)<10002:
    isPrime=True
    for x in range(2,number-1):
        if number%x==0:
            isPrime=False    
    if isPrime==True:
        numbers.append(number)
    number=number+1
    print(number)
    print(len(numbers))
print(numbers[-1])