# You live 4 miles from university. The bus drives at 25mph but spends 2 min at of the 10 stops on the way. How long
# the bus journey take? Alternatively, you could run to university. You jog the first mile  at 7mph: then run next 2 at
# 15mph; before jogging back at 7mph again. Will this be slower or quicker than bus.

dist_to_uni = 4

# for bus

busSpeed = 25
busStops = 10
timePerStops = 2

timeTakenByBus = dist_to_uni / (busSpeed / 60)

for i in range(busStops):
    timeTakenByBus += timePerStops

print('it takes', timeTakenByBus, 'minutes to reach university by bus')

# for running

speed_1 = 7
speed_2 = 15

timeTakenByRunning = 0

for i in range(dist_to_uni):
    timeTakenByRunning += 1 / (speed_1 / 60 if i == 0 or i == 3 else speed_2 / 60)

print('it takes', timeTakenByRunning, 'minutes to reach university by walking')
print('its faster to run' if timeTakenByRunning < timeTakenByBus else 'its faster by bus')

