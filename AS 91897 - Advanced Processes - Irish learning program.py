
##
# AS 91897 - Advanced Processes
# Jayani Bhula
# 30/07/2026


# Welcome user
print("\nDia duit Kenish8")


print("""\nTopics:
  Everyday greetings (Eg)
  Filler Words (Fw)""")


def learn(topic, everyday_greetings, points):
    """Ask multiple choice questions for selected topic"""

    eg_questions = [
        {"Word" : "Haigh", "Answer" : "hi", "Options" : ["hello", "bye"]},
        {"Word" : "Dia duit", "Answer" : "hello", "Options" : ["bye", "please"]},
        {"Word" : "Slán", "Answer" : "bye", "Options" : ["thankyou", "please"]},
        {"Word" : "Le do thoil", "Answer" : "please", "Options" : ["welcome", "hi"]},
        {"Word" : "Go raibh maith agat", "Answer" : "thank you", "Options" : ["welcome", "bye"]},
        {"Word" : "Maidin mhaith", "Answer" : "good morning", "Options" : ["hello", "welcome"]},
        {"Word" : "Fáilte", "Answer" : "welcome", "Options" : ["bye", "please"]},
        ]

    for questions in eg_questions:
        print("Select the correct translation for: {} \n Options: \n1.{} \n2.{} \n3.{}"
              .format(eg_questions['Word'], eg_questions['Options'], eg_questions['Options']))
    
    # If Everyday greetings chosen set as vocabulary
    if topic == "Eg":
 
       # Welcome User
        print("\nLearn Everyday greetings")

        # Select Irish translation
        print("\nSelect the correct translation for: Haigh")

        # English translation options
        print("1. Hello")
        print("2. Hi")
        print("3. Bye")

        # Get user answer selection
        user_selection = input("Enter number selection: ")
        # User write translation in English
        english_word = input("Write the translation for Haigh: ").strip().lower()

        # Check if selection correct
        if user_selection == "2" and english_word == "hi":
            print("""Correct!
            Congratulations on learning a new word!""")
            points += 10

        else:
            print("Incorrect. Keep going!")

        # Select Irish translation
        print("\nSelect the correct translation for: Dia duit")

        # English translation options
        print("1. Bye")
        print("2. Please")
        print("3. Hello")

        # Get user answer selection
        user_selection = input("Enter number selection: ")
        # User write translation in English
        english_word = input("Write the translation for Dia duit: ").strip().lower()   

        # Check if selection correct
        if user_selection == "3" and english_word == "hello":
            print("""Correct!
            Congratulations on learning a new word!""")
            points += 10

        else:
            print("Incorrect. Keep going!")

        # Select Irish translation
        print("\nSelect the correct translation for: Slán")

        # English translation options
        print("1. Bye")
        print("2. Thank you")
        print("3. Please")

        # Get user answer selection
        user_selection = input("Enter number selection: ")
        # User write translation in English
        english_word = input("Write the translation for Slán: ").strip().lower()

        # Check if selection correct
        if user_selection == "1" and english_word == "bye":
            print("""Correct!
            Congratulations on learning a new word!""")
            points += 10

        else:
            print("Incorrect. Keep going!")

        # Select Irish translation
        print("\nSelect the correct translation for: Le do thoil")

        # English translation options
        print("1. Hi")
        print("2. Welcome")
        print("3. Please")

        # Get user answer selection
        user_selection = input("Enter number selection: ")
        # User write translation in English
        english_word = input("Write the translation for Le do thoil: ").strip().lower()

        # Check if selection correct
        if user_selection == "3" and english_word == "please":
            print("""Correct!
            Congratulations on learning a new word!""")
            points += 10


        else:
            print("Incorrect. Keep going!")

        # Select Irish translation
        print("\nSelect the correct translation for: Go raibh maith agat")

        # English translation options
        print("1. Thankyou")
        print("2. Welcome")
        print("3. Bye")

        # Get user answer selection
        user_selection = input("Enter number selection: ")
        # User write translation in English
        english_word = input("Write the translation for Go raibh maith agat: ").strip().lower()

        # Check if selection correct
        if user_selection == "1" and english_word == "thankyou":
            print("""Correct!
            Congratulations on learning a new word!""")
            points += 10


        else:
            print("Incorrect. Keep going!")

        # Select Irish translation
        print("\nSelect the correct translation for: Maidin mhaith")

        # English translation options
        print("1. Hello")
        print("2. Good Morning")
        print("3. Welcome")

        # Get user answer selection
        user_selection = input("Enter number selection: ")
        # User write translation in English
        english_word = input("Write the translation for Maidin mhaith: ").strip().lower()
        print(english_word)

        # Check if selection correct
        if user_selection == "2" and english_word == "good morning":
            print("""Correct!
            Congratulations on learning a new word!""")
            points += 10


        else:
            print("Incorrect. Keep going!")

        # Select Irish translation
        print("\nSelect the correct translation for: Fáilte")

        # English translation options
        print("1. Bye")
        print("2. Please")
        print("3. Welcome")

        # Get user answer selection
        user_selection = input("Enter number selection: ")
        english_word = input("Write the translation for Fáilte: ").strip().lower()

        # Check if selection correct
        if user_selection == "3" and english_word == "welcome":
            print("""Correct!
            Congratulations on learning a new word!""")
            points += 10

        else:
            print("Incorrect. Keep going!")
        
    return points


def vocabulary(everyday_greetings, filler_words):
    """Print vocabulary for chosen topic"""
    print("\nWelcome to the Vocabulary")

    print("""\nTopics:
  Everyday greetings (Eg)
  Filler Words (Fw) """)

    # Ask user for topic
    topic = input("Enter vocab topic: ").strip().title()

    if topic == "Eg":
        print("\nVocab  -  Everyday greetings")
        # For loop prints formatted vocabulary
        for basic in everyday_greetings:
            print("{:13} | {:15}".format(basic['English'], basic['Irish']))

    elif topic == "Fw":
        print("\nVocab  -  Filler Words")
        # For loop prints formatted vocabulary
        for filler in filler_words:
            print("{:5} | {:15}".format(filler['English'], filler['Irish']))


def profile(points):
    """Display user learning stats"""
    print("\nWelcome to Profile")
    print("Username: Kenish8")
    print("Rank: ")
    print("Points: {}".format(points))


def main():
    """Menu and holds word lists"""
    # List of dictionaries - Topic: Everyday greetings
    everyday_greetings = [
        {"English" : "Hi", "Irish" : "Haigh"},
        {"English" : "Hello", "Irish" : "Dia Duit"},
        {"English" : "Bye", "Irish" : "Slán"},
        {"English" : "Please", "Irish" : "Le do thoil"},
        {"English" : "Thankyou", "Irish" : "Go raibh maith agat"},
        {"English" : "Welcome", "Irish" : "Fáilte"},
        {"English" : "Good Morning", "Irish" : "Maidin mhaith"}
        ]

    filler_words = [
        {"English" : "With", "Irish" : "le"},
        {"English" :"And", "Irish" : "agus"},
        {"English" : "Or", "Irish" : "no"},
        {"English" : "The", "Irish" : "an"}
        ]

    points = 0

    # Loop
    while True:
        # Menu
        print("\n")
        print("\n---Dashboard---")
        print("1. Learn")
        print("2. Vocabulary")
        print("3. Profile")
        print("0. Exit")

        # Ask for option choice
        decision = input("\nEnter number option: ")

        if decision == "1":
            print("\nWelcome to Learn")
            
            print("""\nTopics:
        Everyday greetings (Eg)\n
        Filler Words (Fw)\n""")

            topic = input("Enter topic to learn: ").strip().title()
            if topic == "Eg":
                points = learn(topic, everyday_greetings, points)
   
        elif decision == "2":
            vocabulary(everyday_greetings, filler_words)

        elif decision == "3":
            profile(points)

        elif decision == "0":
            print("Session over.")
            break


if __name__ == "__main__":

    main()
