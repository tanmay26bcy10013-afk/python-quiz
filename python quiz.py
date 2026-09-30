import random

questions = [
    {
        "question": "which language is used to create this program?",
        "options": ["A. Java", "B. Python", "C. C++", "D. HTML"],
        "answer": "B"
    },
    {   "question": " Core OOP pillars count?",
        "options":  ["A. 1", "B. 2", "C. 3", "D. 4"],
        "answer": "D"
    },
    {   "question": "Data hiding improves?",
        "options":  ["A. Security", "B. Choise", "C. Display", "D. HTML"],
        "answer": "A"
    },
    {
        "question": "which symbol is used for comments in Python?",
        "options": ["A. #", "B. -", "C. $","D. ="],
        "answer": "A"
    },
    {
        "question": "\ which function is used to display output in Python?",
        "options": ["A. input()", "B. print()", "C. output()", "D. display()"],
        "answer": "B"
    },
    {
        "question": " which data type is used to store True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. Float"],
        "answer": "C"
    },
    {
        "question": "which symbol is used to create a list in Python?",
        "options": ["A. ()", "B. {}", "C. <>", "D. []"],
        "answer": "D"
    },
    {
        "question": "str() used for?",
        "options": ["A. String repersentation", "B. limit ", "C. input", "D. stright"],
        "answer": "A"
    },
    {
        "question": "Inheritance provides?",
        "options": ["A. code reduce", "B. codex ", "C. input", "D. stright"],
        "answer": "A"
    },
    {
        "question": " Private members prefixed by",
        "options": ["A. -", "B. _", "C. =", "D. =="],
        "answer": "B"
    },
    {
        "question": "Python supports multiple inheritance?",
        "options": ["A. YES", "B. NO", "C. BOTH", "D. none of the above"],
        "answer": "A"
    },
]

def start_quiz(student_name, roll_no):
    scores = 0
    quiz_questions = random.sample(questions, len(questions))
    print("\n                                  ")
    print("               QUIZ                 ")
    print("                                    ")
    print("Student Name :", student_name)
    print("Roll Number  :", roll_no)
    print("Total Questions :", len(quiz_questions))

    for number, question in enumerate(quiz_questions, 1):

        print("\nQuestion", number)
        print(question["question"])

        for option in question["options"]:
            print(option)

        while True:
            answer = input("Enter the option (A/B/C/D): ").strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break
            else:
                print("sorry=> incorrect answer=> Please enter only A, B, C, or D.")
        if answer == question["answer"]:
            print("Correct!")
            scores = scores + 1
        else:
            print("Wrong!")
            print("Correct answer:", question["answer"])

    total_questions = len(quiz_questions)
    percentage = (scores / total_questions) * 100

    if percentage >= 90:
        grade = "S"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    elif percentage >= 40:
        grade = "E"
    else:
        grade = "N"

    if percentage >= 40:
        result = "PASS"
    else:
        result = "try again"
    print("\n                                  ")
    print("            QUIZ RESULT             ")
    print("                                    ")
    print("Student Name :", student_name)
    print("Roll Number  :", roll_no)
    print("Scores       :", scores, "/", total_questions)
    print("Percentage   :", round(percentage, 2), "%")
    print("Grade        :", grade)
    print("Result       :", result)

while True:
    print("\n      QUIZ              ")
    print("1. Start Quiz")
    print("2. Exits")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        student_name = input("\nEnter Student Name: ").strip()

        while not student_name:
            print("Student name is mendatory")
            student_name = input("Enter Student Name: ").strip()

        roll_no = input("Enter Roll Number: ").strip()

        while not roll_no.isdigit():
            print("Invalid Roll Number - Please enter numbers only.")
            roll_no = input("Enter Roll Number: ").strip()

        start_quiz(student_name, roll_no)
    elif choice == "2":
        print("\nThank you for giving quiz ")
        print("have a good day")
        break
    else:
        print("Incorrect choice -> Please enter 1 or 2.")
