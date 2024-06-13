import time

# Showing current time
current_time = time.strftime('%H:%M:%S')
print('Current time: ', current_time)

# 5 seconds delay
print('Waiting for 5 seconds...')
time.sleep(5)

# Showing time after delay
delayed_time = time.strftime('%H:%M:%S')
print('Time after delay: ', delayed_time)
