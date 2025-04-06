numbers=[]
dividers=[]
sum=0
for x in range(1, 1000000):
    if len(dividers)<500:
        dividers.clear()
        sum=sum+x
        numbers.append(sum)
        for z in range(1, sum+1):
            if sum%z==0:
                dividers.append(z)
                print(len(dividers))
    else:
        print(numbers[len(numbers)-1])
        break
print(numbers)
print(dividers)
    
        
    


