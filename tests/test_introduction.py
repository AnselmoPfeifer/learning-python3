def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 100 == 0:
        leap = True
    return leap


print(is_leap(1999))