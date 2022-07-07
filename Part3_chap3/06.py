import Rank as rm
import random

midSco = random.sample(range(50, 101), 20)
endSco = random.sample(range(50, 101), 20)

rd = rm.RankDeviation(midSco, endSco)
rd.setMidRank()

print(f'midSco : {midSco}')
print(f'midRank : {rd.getMidRank()}')

rd.setEndRank()
print(f'endSco : {endSco}')
print(f'endRank : {rd.getEndRank()}')

rd.printDeviation()

