i=2
for x in range(3):
    z=i**1000
print(z)
def getsum(z):
    string=str(z)
    listofnumbers=list(map(int, string.strip()))
    return sum(listofnumbers)
print(getsum(z))