from questions import QUESTIONS


def isAnswerCorrect(question, answer):
    return True if QUESTIONS[question]["answer"] == answer else False


def lifeLine(i):
    from random import choice

    print(f'\tQuestion {i+1}: {QUESTIONS[i]["name"]}')
    print(f"\t\tOptions:")
    correct = QUESTIONS[i]["answer"]
    l = [1, 2, 3, 4]
    l.remove(correct)
    x = choice(l)
    if correct > x:
        print(f'\t\t\tOption {x}: {QUESTIONS[i]["option"+str(x)]}')
        print(f'\t\t\tOption {correct}: {QUESTIONS[i]["option"+str(correct)]}')
    else:

        print(f'\t\t\tOption {correct}: {QUESTIONS[i]["option"+str(correct)]}')
        print(f'\t\t\tOption {x}: {QUESTIONS[i]["option"+str(x)]}')


def kbc():
    print("Welcome to KBC")
    lifeline_valid = True
    game_play = True
    i = 0
    while game_play and i < 15:

        print(f'\tQuestion {i + 1}: {QUESTIONS[i]["name"]}')
        print(f"\t\tOptions:")
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
        ans = input("Your choice ( 1-4 ) : ")

        if ans.lower() == "quit":
            if i == 0:
                print("Total amount won 0")
                return
            print("Rotal amount won", QUESTIONS[i - 1]["money"])
            return
            game_play = False

        if ans.lower() == "lifeline" and lifeline_valid and i != 14:
            lifeline_valid = False
            lifeLine(i)
            ans = input("your choice (1 - 4):")
            if ans.lower() == "quit":
                game_play = False

        if isAnswerCorrect(i, int(ans)):
            # print the total money won.
            print("Total amount won", QUESTIONS[i]["money"])
            # See if the user has crossed a level, print that if yes
            print("\nCorrect !")
            i += 1

        else:
            print(
                "OOPS! YOUR ANSWER IS INCORRECT, THE CORRECT ANS IS",
                QUESTIONS[i]["answer"],
            ),

            print("\nIncorrect !")

            if i >= 5 and i < 10:
                print("Total amount won 10,000")
            elif i >= 10 and i < 10:
                print("Total amount won 3,20,000")
            else:
                print("Total amount won 0")

            break


kbc()