class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        databaseS = {}
        databaseT = {}
        for letter in s:
            if letter in databaseS.keys():
                 databaseS.update({letter: databaseS.get(letter) + 1})
            else:
                databaseS.update({letter: 1})
        for letter in t:
            if letter in databaseT.keys():
                databaseT.update({letter: databaseT.get(letter) + 1})
            else:
                databaseT.update({letter: 1})
        for item in databaseS:
            if item not in databaseT.keys() or len(databaseS) != len(databaseT) or databaseS.get(item) != databaseT.get(item):
                return False
        return True