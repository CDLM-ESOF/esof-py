#! python3

import time 
import datetime

dataFile = open('stopWatchData.txt','a')
dt = datetime.datetime.now()
timeStamp = dt.strftime('\n%d/%m/%Y  %H:%M\n')
dataFile.write(timeStamp)

print('Pressoine ENTER para começar. Depois, pressione ENTER para o stopwatch. Pressione Ctrl-C para parar.')
input()
print('Comecou...')
startTime = time.time()    # get the first lap's start time
lastTime = startTime
lapNum = 1

try:
  while True:
    input()
    lapTime = round(time.time() - lastTime, 2)
    totalTime = round(time.time() - startTime, 2)
    print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
    lapNum += 1
    lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
# Handle the Ctrl-C exception to keep its error message from displaying.
  print('\nDone.')

dataFile.close()
