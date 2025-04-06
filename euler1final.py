numbers=[]
i=0
for i in range(1000):
    if i%3==0:
        numbers.append(i)
    elif i%5==0:
        numbers.append(i)
    i=i+1
print(sum(numbers))
