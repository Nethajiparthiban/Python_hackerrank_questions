url="https://www.hackerrank.com/challenges/ctci-ransom-note/problem"
from collections import Counter
def checkMagazine(magazine,note):
    mag={}
    notes={}
    mag=Counter(magazine)
    notes=Counter(note)
    result=notes-mag
    if result == {}:
        print("Yes")
        return
    print("No")
magazine="give me one grand today night"
note="give one grand today"
checkMagazine(magazine,note)