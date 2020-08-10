def main():
    wordList = ["HAT", "RED PILL", "BLUE PILL", "NEO", "AGENT SMITH","MORPHEUS","HELLO WORD", "££HARD FOR NO REASON%%", "BENDING", "RED DRESS", "HIPPO"]
    number = int(input("Welcome, to the system. \nPlease select a number between 0 and 10: "))
    if number <= len(wordList):
        word = wordList[number]
        hangman(word)
        
    else:
        print("Number out of range, Restarting system")
        main()
        
def hangman(word):
    guessedLetters = []
    hashedWord = []
    realWord = []
    index = 0
    for index in range(0,len(word)):
        hashedWord.insert(index,"*")
        realWord.insert(index,word[index])
        index += 1
    print("Lets play hangman")
    ref = ''.join(realWord)
    hold = ''.join(hashedWord)
    while hold != ''.join(realWord):
        print("A",''.join(hashedWord))
        print("B",''.join(realWord))
        print(guessedLetters)
        letter = input("Guess a letter: ")
        letter = letter.upper()
        guessedLetters.append(letter)
        while ref.find(letter) != -1:
            match = ref.find(letter)
            hashedWord[match] = letter
            realWord[match] = "*"
            ref = ''.join(realWord)
        else:
            print("Not found in word")
        
    print("Congrats you completed the game")
      
if __name__ == "__main__":
    main()