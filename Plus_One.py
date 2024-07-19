digits =[8,9,9,9]
sum=''
for n in digits:
    sum+=str(n)

num=int(sum)+1
new_list=[]
for j in str(num):
    new_list.append(int(j))
print(new_list)