#num=int(input("Enter a number"))
x=int(input("enter 1st number"))
y=int(input("enter 2nd number"))
prime_list=[]
for i in range(x,y):
    if i==0 or i==1:
        continue
    else:
        for j in range(2,int(i/2)+1):
            if i%j==0:
                break
        else:
            prime_list.append(i)

print(prime_list)

