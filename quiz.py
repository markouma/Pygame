def personality_quiz():
    print("Welcome to the Personality Quiz!")

    questions = [
        "What is your favorite color? (a) Red (b) Blue (c) Green",
        "What is your favorite animal? (a) Dog (b) Cat (c) Bird",
        "What is your favorite hobby? (a) Reading (b) Cooking (c) Sports"
    ]

    answers = []

    # Ask questions and store answers
    for question in questions:
        answer = input(question + " ")
        answers.append(answer.lower())

    # Calculate result based on answers
    result = calculate_result(answers)

    # Display result
    print("Based on your answers, your personality type is:", result)

def calculate_result(answers):
    # Calculate a result based on the user's answers
    # This is just a simple example, you can define your own logic here
    score = 0
    for answer in answers:
        if 'a' in answer:
            score += 1
        elif 'b' in answer:
            score += 2
        elif 'c' in answer:
            score += 3

    if score <= 5:
        return "Introvert"
    elif score <= 8:
        return "Ambivert"
    else:
        return "Extrovert"

if __name__ == "__main__":
    personality_quiz()
