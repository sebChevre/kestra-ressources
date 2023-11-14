from datetime import datetime
import pytz
datetime_str = '11/13/2023 01:22:41 PM'
datetime_object = datetime.strptime(datetime_str, '%m/%d/%Y %H:%M:%S %p')



print(datetime_str)
print(datetime_object)
print(datetime_object.astimezone().isoformat())
print(datetime.now().astimezone().isoformat())

print('Timezones')
for timeZone in pytz.all_timezones:
    print(timeZone)