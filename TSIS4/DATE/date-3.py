# dropping microseconds from datetime
from datetime import datetime
nowadays = datetime.now()
print(nowadays.replace(microsecond=0))

