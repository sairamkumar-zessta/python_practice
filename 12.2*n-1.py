n = int(input("num:"))

k=1
for i in range(1,2*n):
    if i<n+1:
        print(" "*(n-i)+(str(i)+" ")*i) 
    else:
        print(" "*k+(str(n-k)+" ")*(n-k)) 
        k+=1


