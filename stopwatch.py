#! python3
# stopwatch.py - A simple stopwatch program.
import time

# Display the program's instructions.
print('''Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.
Press Ctrl-C to quit.''')

input()   # press Enter to begin
print("started")
starttime = time.time() # get the first lap's start time
lasttime = starttime
lapnum = 1

# Start tracking the lap times.
try:
	while True:
		input()
		laptime = round(time.time() - lasttime, 2)
		totaltime = round(time.time() - starttime, 2)
		print('lap # %s: %s (%s)' % (lapnum,totaltime,laptime), end="")
		lapnum += 1
		lasttime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\n Done')
