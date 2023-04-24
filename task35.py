n=int(input('Введите число n: '))
flag=False
for i in range(2,n):
    if n%i==0:
        print('no')
        flag=True
if flag==False:
    print('yes')
            