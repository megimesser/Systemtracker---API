import re

teststring = "temp=50.1'C"
print(teststring[5:])



teststring_2 = "journalctl | tail -20"

match = re.search("\|", teststring_2)

if match:
    davor = teststring_2[:match.start()]
    danach = teststring_2[match.end():]
    print(davor)
    print(danach)

