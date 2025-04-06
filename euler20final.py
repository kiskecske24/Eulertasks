z=1
for x in range(1,100):
    z=z*x
print(z)

def getsum(z):
    sum=0
    for digit in str(z):
        sum= sum+int(digit)
    return sum
print(getsum(z))