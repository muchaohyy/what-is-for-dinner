from datetime import datetime
from pytz import timezone

# Initialize global variables
def init():
    # Setup timezone as Sydney's time
    global tz_sydney
    tz_sydney = timezone('Australia/Sydney')
    
    # Define today's date
    global today
    today = datetime.now(tz_sydney).strftime("%Y-%m-%d")
