def is_simple(n):
    for i in range (2,n):
        if n%i==0:
            return False
    return True

n= int(input())
flag=is_simple(n)
if(flag==True):
    print('yes')
else:
    print('no')        
            