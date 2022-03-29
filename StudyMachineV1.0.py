import random as randy
priorities = []


istorija = ["istorija",]
biologija = ["biologija",]
geografija = ["geografija",]

#foo = { "name": "history",
#        "questions": [
#            [ "Question1", "Answer1", 4],
#            [ "Question2", "Answer2", 6]
#        ]
#    }

events = [["Matematika PISMENI", "APRIL 4"],]


highPriority = [istorija]
mediumPriority = [biologija,geografija]
lowPriority = []

priorities = [highPriority, mediumPriority,lowPriority]


print("Select a Priority: 1) 'high' 2) 'medium' 3) 'low'")
tezina = input()
tezinaBR = 0
print("Prioriteti:")
if tezina == "high":
    for i in range(len(highPriority)):
        print(highPriority[i][0])
    subject = input()
    tezinaBR = 3
if tezina == "medium":
    for i in range(len(mediumPriority)):
        print(mediumPriority[i][0])
    subject = input()
    tezinaBR = 2
if tezina == "low":
    for i in range(len(lowPriority)):
        print(lowPriority[i][0])
    subject = input()
    tezinaBR = 1
intSubject = 0
for i in range(len(priorities[tezinaBR])):
    if subject == priorities[tezinaBR][i][0]:
        intSubject = i

score = 0
questionCounter = 0

while True:
    pitanjeBR = randy.randint(1, len(priorities[tezinaBR][intSubject]))
    odgovorIgraca = input(priorities[tezinaBR][intSubject][pitanjeBR][0])
    if odgovorIgraca == "dosta":
        break
    if odgvorIgraca == priorities[tezinaBR][intSubject][pitanjeBR][1]:
        print("Tacno!")
    else:
        print("Netacno!")
        print("Tacno je", priorities[tezinaBR][intSubject][pitanjeBR][1])
score = score/questionCounter



if score >= 85:
    print("Pet")
    exit()
if score >= 65:
    print("Cetiri")
    exit()
if score >= 45:
    print("Tri")
    exit()
if score >= 20:
    print("Dva")
    exit()
if score < 20:
    print("Jedan")
    exit()
