# core/utils/time.py

from datetime import datetime

# Returns first day of current month (season marker)
def get_current_season():
    now = datetime.utcnow()
    return now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
