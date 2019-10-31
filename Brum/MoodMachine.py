import motor as MotorControl
from mood_wander import *

class MoodMachine():
    def __init__(self):
        # list of moods
        self._moods = {
            # null is only here for the first time you start the program
            "null",
            "happy",
            "sad"
        }
        self._currentMood = self._moods["null"]

    def SetMood(self, moodId):
        if moodId in self._moods:
            self._currentMood = self._moods[moodId]

    def GetMood(self):
        # return current mood so you can useit in other script to know how to react
        return(self._currentMood)
