i=1
y=1
list1=[]
list2=[]
while i<101:
    list1.append(i)
    y=i*i
    list2.append(y)
    i=i+1
sumlist1=sum(list1)*sum(list1)
sumlist2=sum(list2)
diff=sumlist1-sumlist2
print(diff)

