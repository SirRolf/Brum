import motor as MotorControl

class MoodMachine():
    def __init__(self):
        self._moodStatus = {
            "happy" : 0,
            "sad" : 0
        }
        # list of moods
        self._moods = {
            # null is only here for the first time you start the program
            "null",
            "happy",
            "sad"
        }
        self._currentMood = self._moods["null"]

    def ChangeMoodStatus(self, moodId, amount):
        if moodId in self._moodStatus:
            self.moodStatus[moodId] += amount

    def SetMood(self, moodId):
        if moodId in self._moods:
            self._currentMood = self._moods[moodId]

    def GetMood(self):
        # return current mood so you can useit in other script to know how to react
        return(self._currentMood)
