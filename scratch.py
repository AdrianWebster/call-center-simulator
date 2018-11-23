import random as r
import numpy as np

class entity:
    def __init__(self):
        self.id = str(id(self))
        self.active = False
    def toggleActive(self):
        self.active = not self.active


class caller(entity):
    def call(self):
        ''' places a call to the call center'''

    def talking(self):
        '''participates in the call'''

class phoneLine():

    def __init__(self):
        self.line = []
        self.id = str(id(self))
        self.active = False

    def toggleActive(self):
        self.active = not self.active

    def resolveCall(self,call):
        # get time it takes to complete

        # wait that amount of time

        # move the call to the completed pile
        completedCalls.append(self.line.pop(0))

        # set self as not active
        self.toggleActive()

    def hold(self,call):
        self.toggleActive()
        self.line.append(call)

    def transferIn(self,phoneLine):
        self.hold(phoneLine.line.pop(0))
        phoneLine.toggleActive()



def CallIn(call):
    # check if line 1 is busy
    if phoneLine1.active:
        #check if line 2 is busy
        if phoneLine2.active:
            #check if hold line is busy
            if holdLine.active:
                #drop call
                print('No available lines, dropping call')
                droppedCalls.append(call)
            else: #put onto hold
                print('Placing call on hold')
                holdLine.hold(call)
        else: #put call onto line 2
            print('Placing call on line 2')
            phoneLine2.hold(call)
    else: #put call onto line 1
        print('Placing call on line 1')
        phoneLine1.hold(call)



phoneLine1 = phoneLine()
phoneLine2 = phoneLine()
holdLine = phoneLine()
completedCalls = []
droppedCalls = []



calls = []
for i in range(10):
    calls.append(caller())

for i in calls:
    CallIn(i)





