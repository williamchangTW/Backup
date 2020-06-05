import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = int(battery.percent)

if plugged == False:
	plugged = "Not Plugged In"
# TODO: do something when charger wasnt plugged
else:
	plugged = "Plugged In"
# TODO: do something when charger was plugged

print(str(percent) + "% | " + plugged)
