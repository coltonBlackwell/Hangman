import random

from yaml import FlowSequenceEndToken


def askLetter(letter):

    if(letter.isalpha() == False and len(letter) != 1):
        letter = input("You need to input a letter")
        askLetter(letter)
    elif(letter.isalpha() == False or len(letter) != 1):
        letter = input("You need to input a letter")
        askLetter(letter)
    else:
        return letter

def changeLetter(numberList, correctLetter, revisedHiddenWord):


    hiddenWordList = list(revisedHiddenWord)

    for number in numberList:

        hiddenWordList[number] = correctLetter

    revisedHiddenWord = "".join(hiddenWordList)

    return revisedHiddenWord
    

def checkResponse(response, hangmanStage):

    validReponse = False

    letterPositions = []

    for letter in range(len(chosenWord)):
        if response == chosenWord[letter]:
            validReponse = True

            letterPositions.append(letter)
            

    if(validReponse == True):
        return letterPositions, response, validReponse
    else:
        hangmanStage = hangmanStage + 1
        return letter, hangmanStage, validReponse

            
#--------------------HANGMAN PICTURES-------------------

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#--------------------HANGMAN PICTURES-------------------


words = ["apple", "matrix", "zebra"]

print("\n************** NEW GAME ***************")

print("\nWelcome to Hangman!!\n")

hangmanStage = 0

print(HANGMANPICS[hangmanStage], "\n")

numberInWordList = random.randint(0,2)


chosenWord = words[numberInWordList]

hiddenWord = chosenWord

hiddenWordList = list(hiddenWord)

for element in range(len(hiddenWordList)):
    hiddenWordList[element] = '-'


revisedHiddenWord = "".join(hiddenWordList)


print("Your Word To Solve Is:", revisedHiddenWord, "\n")

userLetterList = []




while(hangmanStage < 6):

    print("*********NEW GUESS*********\n")

    userLetter = input("Please input a letter: ")

    print(userLetterList)

    response = askLetter(userLetter)

    pair = checkResponse(response, hangmanStage)

    if(pair[2] == True):

        letterChange = changeLetter(pair[0], pair[1], revisedHiddenWord)

        revisedHiddenWord = letterChange

    else:

        hangmanStage = hangmanStage + 1

        userLetterList.append(userLetter)

    print(HANGMANPICS[hangmanStage])

    #----------THE CHOSEN WORD----------
    print("--------------------------")
    print("||       CHOSEN WORD     ||")
    print("||                       ||")
    print("||        ", revisedHiddenWord, "       ||")
    print("||                       ||")
    print("--------------------------")

    print("\n")

    #---------INVALID LETTERS----------
    print("--------------------------")
    print("||    INVALID LETTERS    ||")
    print("||                       ||")

    print(userLetterList )
    print("||                       ||")
    print("--------------------------")


    if(revisedHiddenWord == chosenWord):

        print("Congratulations! You have solved the word!")
        break

print("Sorry! You did not solve the word!")
print("\nThe Word to solve was:", chosenWord)


exit()