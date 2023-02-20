from datetime import datetime

date1_string = input("Enter first date (YYYY-MM-DD HH:MM:SS): ")
date2_string = input("Enter second date (YYYY-MM-DD HH:MM:SS): ")

d1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
d2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

substracting_by_seconds = (d2 - d1).total_seconds()

print(
    f"The difference between the two dates is {substracting_by_seconds:.2f} seconds.")
