list_a = [1,2,3,4,5,6,7,9]

#map: for mapping each element in list
list_square = list(map(lambda x:x**2,list_a))
print(list_square)

#filter => To filter elements in a list
list_odd = list(filter(lambda x:x%2!=0, list_a))
print(list_odd)

# def prime(x):
#     if x< 2:
#         return False
#     elif x==2:
#         return True
#     else:
#         for i in range(2,int(x**0.5+1)):
#             if (x%i == 0):
#                 return False
#         return True
is_prime = lambda x : x>=2 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))
list_prime = list(filter(is_prime,list_a))
print(list_prime)