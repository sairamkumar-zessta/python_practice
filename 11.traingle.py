n = int(input("int:"))

for i in range(1,n+1):
    if (i==n):
        print(" "*(n-i)+"/"+"_"*(i-1)+"|")
    else:
        print(" "*(n-i)+"/"+" "*(i-1)+"|")