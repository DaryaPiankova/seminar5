size=int(input('введите размер массива '))
my_list=[size]
my_list = [int(i) for i in input().split()]
print(my_list)
max_elem=my_list[0]
min_elem=my_list[0]
for i in my_list:
    if i>max_elem:
        max_elem=i
    if i<min_elem:
        min_elem=i

for j in my_list:
    if j==max_elem:
        my_list[j]=min_elem
print(my_list)