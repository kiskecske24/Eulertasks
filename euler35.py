primes=[]
def rotateNumber(number):
    number[0]=number[-1]
    for i in range(0,len(number)):
        number[i]=number[i+1]
        return number
    
def isItPrime(number):  
    convertedNumber=int(number) 
    check=True
    for x in range(2, convertedNumber):
        if convertedNumber%x==0:
            check=False
    return check

for x in range(1, 1000000):
    number=str(x) 
    isCircularPrime=True
    for num in range(len(number)-1):
        rotateNumber(number)
        if isItPrime(number)==False:
            isCircularPrime==False        
    if isCircularPrime==True:
        primes.append(number)
print(len(primes))

    


        

    
