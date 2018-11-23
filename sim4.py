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
completed = [[0,0]]
hold = []
dropped = []


while len(calls) > 0:
    #if this current call is in a frame of time before the completion time of the last completed call
    if calls[0] < completed[-1[1]]:
        #and nothing is in hold
        if hold[0] > 0:
            #put this call on hold
            hold.append(calls.pop(0))
        else:
            #drop it like its hot
            dropped.append(calls.pop(0))
    else:
        #this job is not in the past and can be done if nothing is on hold
        currentJob.append(calls.pop(0))




    doJob(currentCall,currentServiceTime)
