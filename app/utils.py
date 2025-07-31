from datetime import datetime
import pytz

def convert_to_timezone(dt: datetime, tz: str):
    local_tz = pytz.timezone(tz)
    return dt.astimezone(local_tz)
