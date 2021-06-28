list=[]
for i in range(123,568):
    if i%5==0 or i%6==0:
        list.append(i)
print(list)
print(len(list))
print("sum= ",sum(list))
