HoursBefore = int(input("How many hours is your video? "))
MinsBefore = int(input("How many minutes is your video? "))
SecsBefore = int(input("How many seconds is your video? "))
PlaybackSpeed = float(input("What is the playback speed? "))
# All the information needed to calculate the playback time has been collected by the user

# Now I am going to start doing the calculations by first converting all the times to seconds which will make it easier
TotalSecsBefore = (HoursBefore * 3600) + (MinsBefore * 60) + SecsBefore

# To calculate the total seconds after, I have to divide the total seconds before by the playback speed
TotalSecsAfter = TotalSecsBefore / PlaybackSpeed

# Now I will start to convert everything back into hours, minutes and seconds
HoursAfter =  round(TotalSecsAfter // 3600)
MinsAfter = round((TotalSecsAfter // 60) - (HoursAfter * 60))
SecsAfter = round(TotalSecsAfter - ((HoursAfter * 3600) + (MinsAfter * 60)))

# This next section is to make the results more "human-like". This is by not mentioning a variable if it doesn't have a value.
# E.g. If the result is of (in format HH:MM:SS), 00:16:06. it will say 16 minutes and 6 seconds instead of 0 hours, 16 minutes and 06 seconds. 
if HoursAfter > 0 and MinsAfter > 0 and SecsAfter > 0:
    print(f"Your video playback time after changing the speed is {HoursAfter} hours, {MinsAfter} minutes and {SecsAfter} seconds.")
elif HoursAfter == 0 and MinsAfter > 0 and SecsAfter > 0:
    print(f"Your video playback time after changing the speed is {MinsAfter} minutes and {SecsAfter} seconds.")
elif HoursAfter > 0 and MinsAfter == 0 and SecsAfter > 0:
    print(f"Your video playback time after changing the speed is {HoursAfter} hours and {SecsAfter} seconds.")
elif HoursAfter > 0 and MinsAfter > 0 and SecsAfter == 0:
    print(f"Your video playback time after changing the speed is {HoursAfter} hours and {MinsAfter} minutes.")
elif HoursAfter == 0 and MinsAfter == 0 and SecsAfter > 0:
    print(f"Your video playback time after changing the speed is {SecsAfter} seconds.")
elif HoursAfter == 0 and MinsAfter > 0 and SecsAfter == 0:
    print(f"Your video playback time after changing the speed is {MinsAfter} minutes.")
elif HoursAfter > 0 and MinsAfter == 0 and SecsAfter == 0:
    print(f"Your video playback time after changing the speed is {HoursAfter} hours.")
else:
    print("Invalid values. Please try again.")