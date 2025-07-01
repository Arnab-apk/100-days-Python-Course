def is_leap_year(year):
    """function that has the logic for a leap year calculation"""
    is_leap=False
    # Write your code here. 
    # Don't change the function name.
    if (year%4==0 and year%100!=0) or year%400==0:
        is_leap=True
    return is_leap
year=int (input("Enter a year: "))
print(is_leap_year(year))