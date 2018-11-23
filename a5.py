import numpy
import random



workDayMinutes = 480

def generateCallsIn(workDayMinutes):
    arrivals = [random.expovariate(0.5)]
    while arrivals[-1] < workDayMinutes:
        arrivals.append(random.expovariate(0.5) + arrivals[-1])


    if arrivals[-1] > 480:
        del arrivals[-1]

    return arrivals

def generateServiceTimes():
    service = []
    for i in range(500):
        service.append(numpy.random.exponential(3))
    return service


def testDist(n):
    testarray = []
    for i in range(n):
        test = generateCallsIn(480)
        test = len(test)
        testarray.append(test)
    avg = sum(testarray)/len(testarray)
    print(str(avg))


def doJob(job,time):
    return [job,job+time]



calls = generateCallsIn(workDayMinutes)
service = generateServiceTimes()

for i in range(len(calls)):
    currentCall = calls.pop(0)
    currentServiceTime = service.pop(0)
    doJob(currentCall,currentServiceTime)
    