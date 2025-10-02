# Function to check if a year is a leap year
def is_leap_year(year):
    # Check if the year is divisible by 4 but not by 100,
    # unless it is also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Test the function
years = [1900, 2000, 2012, 2021]
for y in years:
    if is_leap_year(y):
        print(f"{y} is a leap year.")
    else:
        print(f"{y} is not a leap year.")