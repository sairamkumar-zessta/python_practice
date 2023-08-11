n=int(input("n:"))
out=""
for i in range(n):
    out=" "*i+"* "*(n-i)
    print(out)
i=n-2
for j in range(n-1):
    out=" "*i+"* "*(n-i)
    print(out)
    i-=1