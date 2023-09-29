import requests
import csv

def startGame():
    # Loop through 3 questions, get answer, compare answer with question and keep score
    print("Let's start {} ".format(username))
    score = 0
    for eachResult in getResults:
        oneStatement = eachResult["question"]
        correctAnswer = eachResult["correct_answer"].lower()
        oneStatement = oneStatement.replace('&quot;', '"')
        print(oneStatement)
        answer = input("Is this statement true or false?").lower()

        while answer != "true" and answer != "false" and answer != "t" and answer != "f":
            print("That is not an acceptable answer, please try again")
            answer = input("Is this statement true or false?").lower()

        if correctAnswer == answer or correctAnswer[0] == answer[0]:
            print("You scored one point")
            score += 1

        else:
            print("Sorry your answer is incorrect, now you know for next time")

    print("Your score this time is {} and your score has been added to the scoreboard".format(score))


    # Save player and score to CSV
    results = [{"player": username, "score": score}]

    with open('scoreboard.csv', 'a') as scoreboard:
        spreadsheet = csv.DictWriter(scoreboard, fieldnames=["player", "score"])
        spreadsheet.writerows(results)

# Get data from API
getData = requests.get("https://opentdb.com/api.php?amount=3&category=18&difficulty=easy&type=boolean")
convertData = getData.json()
getResults = convertData["results"]

# Display welcome message
print("Welcome to Trivia")

# Ask for name, display welcome message, then slice the name for the scoreboard
name = input("What is your first name?")
username = name[0:3].lower()
startGame()

#Gives the option to play again
playAgain = input("Do you want to play again?").lower()
while playAgain == "yes" or playAgain == "y":
    startGame()
    playAgain = input("Do you want to play again?")

print("Thanks for playing")