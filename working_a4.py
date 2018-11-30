import numpy as np
import statsmodels.stats.api as sms


np.random.seed(7717679)


def generateCallsIn(workDayMinutes):
    arrivals = [np.random.exponential(2)]
    while arrivals[-1] < workDayMinutes:
        arrivals.append(arrivals[-1]+np.random.exponential(2))

    if arrivals[-1] > 480:
        del arrivals[-1]

    return arrivals


def generateServiceTimes(m,speed):
    service = []
    for i in range(m):
        service.append(np.random.exponential(speed))
    return service


def completeCall(serviceT, call):
    completedCall = [call, call + serviceT]
    return completedCall

def lineBusy(call,array):
    for i in range(len(array)):
        #for every item in array

        if array[i][0] <= call <= array[i][1]:
            # if the call occurs during another call
            print("The call at time "+ str(call)+ " occurs between times "+ str(array[i][0]) + ' and ' + str(array[i][1]))
            return True, i

    return False, len(array)


def main(speed):
    workDayMinutes = 480
    callArray = generateCallsIn(workDayMinutes)
    serviceArray = generateServiceTimes(len(callArray),speed)

    dropped = []
    completed = []
    timeOnHold = []

    for x in range(len(callArray)):
        call = callArray[x]
        service = serviceArray[x]

        line1 = lineBusy(call,completed)
        if line1[0]:
            newArray = completed[line1[1]+1:]
            line2 = lineBusy(call, newArray)
            if line2[0]:
                newArray2 = newArray[line2[1]+1:]
                line3 = lineBusy(call, newArray2)
                if line3[0]:
                    dropped.append(call)
                else:
                    print("Completing the call at time " + str(call) + " on hold line")
                    completionTime = (completed[-1][1]) + service
                    timeOnHold.append(completionTime-call)
                    completedCall = [call,completionTime]
                    completed.append(completedCall)

            else:
                print("Completing the call at time " + str(call) + " on line 2")
                completedCall = completeCall(service, call)
                completed.append(completedCall)
        else:
            print("Completing the call at time " + str(call) + " on line 1")
            completedCall = completeCall(service, call)
            completed.append(completedCall)

    return completed,dropped,callArray,serviceArray, timeOnHold


def replications(n,speed):
    results = []
    for i in range(n):
        temp = main(speed)
        results.append(temp)
    return results

def percentLost(results):
    total = 0
    lost =  0
    averages = []
    for i in range(len(results)):
        instTotal = len(results[i][2])
        instLost = len(results[i][1])
        total = total + instTotal
        lost = lost + instLost
        averages.append(instTotal/instLost)

    print('Average Percent Lost: ' + str(total/lost))
    print('C.I at 95%: ' + str(sms.DescrStatsW(averages).tconfint_mean(.05)))
    print('C.I at 99%: ' + str(sms.DescrStatsW(averages).tconfint_mean(.01)))


def avgHoldingTime(results):
    holdingTimesTotal = []

    for i in range(len(results)): # for every replication
        holdingTimes =  results[i][4]
        holdingTimesTotal += holdingTimes

    print('Average Holding time: '+ str(np.mean(holdingTimesTotal)))
    print('C.I at 95%: '+ str(sms.DescrStatsW(holdingTimesTotal).tconfint_mean(.05)))
    print('C.I at 99%: ' + str(sms.DescrStatsW(holdingTimesTotal).tconfint_mean(.01)))
