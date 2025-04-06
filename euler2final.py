i=1
j=2
even=[2]
print(i)
while j<4000000:
    i, j = j, i+j
    if j%2==0:
        even.append(j)
print(sum(even))
print(even)
