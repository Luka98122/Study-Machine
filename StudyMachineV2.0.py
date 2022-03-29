import random as randy
from numpy.random import choice

priorities = []

spanski = [
    "spanski",
    ["ropa", "odeca", 1],
    ["blusa", "bluza", 1],
    ["vestido", "haljina", 1],
    ["pantalones corto", "sorc", 1],
    ["pantalones", "pantalone", 1],
    ["falda", "suknja", 1],
    ["kamisa", "kosulja", 1],
    ["kamaseta", "majica", 1],
    ["bolso", "novcanik", 1],
    ["vaqueros", "farmerke", 1],
    ["traje", "odelo", 1],
    ["mallas deportivas", "helanke", 1],
    ["abrigo", "kaput", 1],
    ["chaqueta", "jakna", 1],
    ["sueter", "dzemper", 1],
    ["bufanda", "sal", 1],
    ["guantes", "rukavice", 1],
    ["gorra", "kapa", 1],
    ["sombrero", "sesir", 1],
    ["zapatos", "cipele", 1],
    ["sandalias", "sandale", 1],
    ["paraguas", "kisobran", 1],
    ["botas", "cizme", 1],
    ["zapatillas", "papuce", 1],
    ["calcetinas", "carape", 1],
    ["camiseta interior", "podkosulja", 1],
    ["bata", "bademantil", 1],
    ["cortinas", "zavese", 1],
    ["alfombra", "tepih", 1],
    ["reloj", "sat", 1],
    ["almohada", "jastuk", 1],
    # ["p","o",1],
    # ["p","o",1],
    # ["p","o",1],
    # ["p","o",1],
    # ["p","o",1],
    # ["p","o",1],
    # ["p","o",1],
    # ["p","o",1],
    # ["p","o",1],
    # ["p","o",1],
    # ["p", "o", 1],
    # ["p", "o", 1],
]


istorija = [
    "istorija",
    ["Koliko dugo je trajala kosovska bitka?", "1 dan", 1],
    [
        "Kada se dogodila kosovska bitka? ( ceo datum, dan oba kalendara)",
        "15/28 6 1389",
        0.001,
    ],
    [
        "Ko je bio prvi sin Stefana Prvovencanog? Kada je vladao?",
        "Stefan Vladoslav, 1228 do 1234",
        0.001,
    ],
    [
        "Ko je bio drugi sin Stefana Prvovencanog? Kada je vladao?",
        "Stefan Vladislav, 1234 do 1243",
        0.001,
    ],
    [
        "Ko je bio treci sin Stefana Prvovencanog? Kada je vladao?",
        "Stefan Uros I, 1243 do 1276",
        0.001,
    ],
    # ["Ko je vladao Srbijom od 1228 do 1234 godine?", "", 0.2],
    # ["Ko je vladao Srbijom od 1234 do 1243 godine?", "", 0.2],
    # ["Ko je vladao Srbijom od 1243 do 1276 godine?", "", 0.2],
    # ["", "", 1],
    # ["", "", 1],
    # ["", "", 1],
    # ["", "", 1],
    # ["", "", 1],
    # ["", "", 1],
]
biologija = [
    "biologija",
]

geografija = [
    "geografija",
]

# foo = { "name": "history",
#        "questions": [
#            [ "Question1", "Answer1", 4],
#            [ "Question2", "Answer2", 6]
#        ]
#    }

events = [
    ["Matematika PISMENI", "APRIL 4"],
]


highPriority = [istorija]
mediumPriority = [biologija, geografija, spanski]
lowPriority = []

priorities = [highPriority, mediumPriority, lowPriority]


print("Select a Priority: 1) 'high' 2) 'medium' 3) 'low'")
tezina = input()
tezinaBR = 0
print("Prioriteti:")
if tezina == "high":
    for i in range(len(highPriority)):
        print(highPriority[i][0])
    subject = input()
    tezinaBR = 0
if tezina == "medium":
    for i in range(len(mediumPriority)):
        print(mediumPriority[i][0])
    subject = input()
    tezinaBR = 1
if tezina == "low":
    for i in range(len(lowPriority)):
        print(lowPriority[i][0])
    subject = input()
    tezinaBR = 2
intSubject = 0
for i in range(len(priorities[tezinaBR])):
    if subject == priorities[tezinaBR][i][0]:
        intSubject = i

score = 0
questionCounter = 0

numList = []
numList2 = []
for i in range(1, len(priorities[tezinaBR][intSubject])):
    numList.append(i)
    numList2.append(priorities[tezinaBR][intSubject][i][2])
while True:
    pitanjeBR = randy.randint(1, len(priorities[tezinaBR][intSubject]) - 1)
    pitanjeBR = choice(numList, 1, numList2)
    pitanjeBR = int(pitanjeBR[0])
    odgovorIgraca = input(priorities[tezinaBR][intSubject][pitanjeBR][0] + " ")
    if odgovorIgraca == "dosta":
        break
    if odgovorIgraca == "skip":
        continue
    if odgovorIgraca == priorities[tezinaBR][intSubject][pitanjeBR][1]:
        print("Tacno!")
        score = score + 1
    else:
        print("Netacno!")
        print("Tacno je", priorities[tezinaBR][intSubject][pitanjeBR][1])
    questionCounter += 1
score = (score / questionCounter) * 100


if score >= 90:
    print("Pet", score, "%")
    exit()
if score >= 65:
    print("Cetiri", score, "%")
    exit()
if score >= 45:
    print("Tri", score, "%")
    exit()
if score >= 25:
    print("Dva", score, "%")
    exit()
if score < 25:
    print("Jedan", score, "%")
    exit()
