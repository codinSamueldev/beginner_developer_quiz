"""
    A quiz contains questions and answers. Someone need to validate the answers of the questions. Then, give a calification based on the answers.
    Questions and answers should be written in the questions.txt

    Show to users the question, possible answers and the options to type.
    Validate user answers. Then, based on the score, print how many answers were right and some text.
    Each valid answers gives one point, invalid answer zero.
"""

def get_txt(path):
    with open(path, 'r') as txtfile:
        reading = txtfile.readlines()

    return reading


def quiz_content(content, correct_answers):
    user_score = 0
    questions = []
    options = []

    for line in content:
        #Separate each line of the .txt file.
        parts = line.strip().split(',')
        #Store question since questions comes before the first comma (,) in the .txt file.
        question = parts[0]
        #Store answer options since answers comes after the first comma (,) in the .txt file.
        option = parts[1:]
        #Store either questions and answer options for each given list.
        questions.append(question)
        options.append(option)

    for i in range(len(questions)):
        #Show to user the question and answer options.
        print(f'\n{questions[i]}\n{options[i]}')

        #This loop could get infinite if the break statement is placed wrong.
        while True:
            user_answer = input("Type you answer fella: ").lower()

            if user_answer in ['a', 'b']:
                break
            else:
                print("\nDude seriously, select either a or b no more no less.")

        #Validating user's answers.
        if user_answer == correct_answers[i]:
            user_score += 1
            print("\nOk.")
        else:
            print("\nHmmm.")

    #Time to give our user the calification.
    if user_score >= 7:
        print(f"\n{user_score}/10\nGreat! Suit up and let's beat some robots.\n")
    else:
        print(f"\n{user_score}/10\nWe are done, AI will run the world.\n")

    return user_score


if __name__ == '__main__':
    path = './content.txt'
    correct_answers = ['a', 'a', 'b', 'b', 'a', 'a', 'b', 'a', 'b', 'b']
    extract_txt = get_txt(path)
    user_score = quiz_content(extract_txt, correct_answers)
