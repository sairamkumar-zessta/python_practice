first_day = input("day:")
date = int(input())


list_days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
req = (date+list_days.index(first_day)-1)%7
print(list_days[req])


    