def is_lunatic(year):
    if (year % 400 == 0):
        return True
    elif (year % 100 == 0):
        return False
    elif (year % 4 == 0):
        return True
    else:
        return False

print(is_lunatic(300))
print(is_lunatic(400))
print(is_lunatic(2004))
print(is_lunatic(303))

def is_lunatic2(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

print(is_lunatic2(300))
print(is_lunatic2(400))
print(is_lunatic2(2004))
print(is_lunatic2(303))
