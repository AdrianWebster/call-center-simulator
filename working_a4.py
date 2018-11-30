import numpy


def generateCallsIn(workDayMinutes):
    arrivals = [np.random.exponential(2)]
    while sum(arrivals) < workDayMinutes:
        arrivals.append(np.random.exponential(2))

    if arrivals[-1] > 480:
        del arrivals[-1]

    return arrivals


def generateServiceTimes(m):
    service = []
    for i in range(m):
        service.append(numpy.random.exponential(3))
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


def main():
    workDayMinutes = 480
    callArray = generateCallsIn(workDayMinutes)
    serviceArray = generateServiceTimes(len(callArray))

    dropped = []
    completed = []

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
                    print("Completitng the call at time " + str(call) + " on hold line")
                    completedCallCall = [call, (completed[-1][1]) + service]
                    completed.append(completedCall)
            else:
                print("Completitng the call at time " + str(call) + " on line 2")
                completedCall = completeCall(service, call)
                completed.append(completedCall)
        else:
            print("Completitng the call at time " + str(call) + " on line 1")
            completedCall = completeCall(service, call)
            completed.append(completedCall)

    return completed,dropped,callArray,serviceArray

