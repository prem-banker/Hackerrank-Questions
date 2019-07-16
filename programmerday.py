year = raw_input()
year = int(year)

if 1700 <= year <= 1917 :
    if year%4 == 0:
        print("12.09."+ year)
    else:
        print("13.09."+ year)
elif 1919 <= year <= 2700:
    if year%400 == 0:
        print("12.09."+ year)
    elif year%4 == 0 and year%100 != 0:
        print("12.09."+ year)
    else:
        print("13.09."+ year)
else:
    print("26.09."+ year)
