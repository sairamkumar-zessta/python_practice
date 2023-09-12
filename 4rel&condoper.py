
a = int(input("FirstNo:"))
b = int(input("SecondNo:"))
c = int(input("ThirdNo:"))
d = int(input("FourthNo:"))
if (a>b and a>c):
    print("a is greater number that is {}".format(a))
elif (b>c and b>d):
    print("b is greater number that is {}".format(b))
elif (c>d):
    print("c is greater number that is {}".format(c)) 
else:
    print("d is greater number that is {}".format(d))

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# max_value = lambda x, y, z, w: max(x, y, z, w)

# result = max_value(a, b, c, d)
# print(result)
