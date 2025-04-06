from num2words import num2words
numbers=[]
sum=0
for x in range(1000):
    string=str(num2words(x))
    numbers.append(string)
    length=len(string)
    sum=sum+length
    if numbers[x].find('-')==True:
        sum=sum-1
print(sum)
    



