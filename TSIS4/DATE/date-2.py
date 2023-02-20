# printing yesterday, today, tomorrow.

from datetime import datetime, timedelta

today = datetime.now()
tomor = today + timedelta(days=1)
yest = today - timedelta(days=1)

print("Yesterday:", yest.strftime("%c"))
print("Today:", today.strftime("%c"))
print("Tomorrow:", tomor.strftime("%c"))
