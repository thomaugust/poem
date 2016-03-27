import random

lineNum = 0

noun = ['night','door','gateway','myriad','museum','horseman']
verb = ['thought','acted','drank','asphyxiated','prayed','died']
conjunction = ['but','however','yet','also','although','and']
adjective = ['pretentious','amazing','deadly','fatal','beautiful','great']
adverb = ['quickly','sorrowfully','delightfully','willfully','dreamily','maliciously']
particle = ['the','a','this','that','no','of']

def line():
    line = conjunction[random.randint(0,5)] + " " + particle[random.randint(0,5)] + " " + adjective[random.randint(0,5)] + " " + noun[random.randint(0,5)] + " " + adverb[random.randint(0,5)] + ' ' + verb[random.randint(0,5)]
    print line

while lineNum < 3:
    line()
    lineNum += 1
