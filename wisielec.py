import random
phrases = ["Wolny Tybet","Grzegorz Brzęczyszczykiewicz","Król Zygmunt Stary","Być czy nie być oto jest pytanie","Konstantynopolitańczykowianeczka","Polska Gurom"]
phrase = phrases[random.randint(0,len(phrases)-1)]
phrase = phrase.lower()
newPhrase = ""
chances = 10
alreadyGuessed = []
for i in phrase:
    if i==" ":
        newPhrase+=" "
    else:
        newPhrase+="_"
newPhraseList = list(newPhrase)
game = True
win = False
print("Guess the phrase (polish language, polish letters included)")
while game:
    alg = False
    isSub = False
    print("\n"+"".join(newPhraseList))
    found = False
    cheat = True
    #zgadywanie
    while cheat:
        guess = input("Podaj literę: ")
        guess = guess.lower()
        if len(guess)==1:
            cheat = False
    
    for i in alreadyGuessed:
        if guess==i:
            print("You already guessed it!")
            alg = True
            break
        
    for i in range(len(phrase)):
        if phrase[i] == guess:
            newPhraseList[i] = guess
            found=True
            alreadyGuessed+=guess
    if found == True and alg==False:
        print("You found it!")        
    elif found == False and alg==False:
        chances-=1
        print("There is no such letter\nChances left:",chances)
    if chances == 0:
        game = False
    else:
        for i in newPhraseList:
            if i=="_":
                isSub = True
        if isSub == False:
            game = False
            win = True
    alreadyGuessed+=guess
if win:
    print("You win!")
else:
    print("You lose")
print("The phrase was:",phrase)