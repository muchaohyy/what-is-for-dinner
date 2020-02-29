from datetime import datetime
from pytz import timezone

# Initialize global variables
def init():
    global tz_sydney
    tz_sydney = timezone('Australia/Sydney')
    
    global today
    today = datetime.now(tz_sydney).strftime("%Y-%m-%d")
