first_day = input("first day:")
req_date = int(input("req date:"))
days_dict = {"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
req_digit = (req_date-1+days_dict[first_day]) % 7
for key,value in days_dict.items():
    if (value == req_digit):
        print(key)


# first_day = input("day:")
# date = int(input())


# list_days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
# req = (date+list_days.index(first_day)-1)%7
# print(list_days[req])


    