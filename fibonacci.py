num = int(input("Enter the number: "))
first_num = 0
second_num = 1
count = 0
while count<num:
    print(first_num)
    fibo=first_num+second_num
    first_num = second_num
    second_num = fibo
    count+=1
print(second_num)
