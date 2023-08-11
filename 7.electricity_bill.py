units = int(input())
if units > 250:
    total = (units - 250) * 8 + 100 * 5 + 100 * 3 + 50 * 2
elif units > 150:
    total = (units - 150) * 5  + 100 * 3 + 50 * 2
elif units > 100:
    total = (units - 100) * 3  + 50 * 2
print(total*1.2)

