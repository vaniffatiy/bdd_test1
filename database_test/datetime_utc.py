from _datetime import datetime, timedelta


dates = ['05:42:00', '05:42:00']
dates_list = [datetime.strptime(time, '%H:%M:%S').time() for time in dates]

max_date = max(dates_list)
utc = datetime.utcnow()
target_time = utc - timedelta(minutes=5)
print(max_date > target_time.time())
