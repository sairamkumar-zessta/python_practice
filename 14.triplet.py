n = int(input("n:")) 

triplet_list = [(i,j,k) for i in range(5,n+1) for j in range(4,i) for k in range(3,j) if (i**2 ==( j**2 + k**2)) ]

print(triplet_list)


