# subtracting five days from current date
from datetime import datetime, timedelta

current_time = datetime.now()
minus_five = current_time - timedelta(days=5)

print(minus_five)
