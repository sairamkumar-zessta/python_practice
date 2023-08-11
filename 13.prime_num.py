def fact_num(num):
    fact = 0 
    for i in range(2,num):
        if num%i == 0:
            fact+=1 
    return fact


prime_list = []
n = int(input("num:"))

for i in range(2,n):
    if fact_num(i) == 0:
        prime_list.append(i)
print(prime_list)