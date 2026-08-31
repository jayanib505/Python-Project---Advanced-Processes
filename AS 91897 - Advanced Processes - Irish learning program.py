##
# AS 91897 - Advanced Processes
# Jayani Bhula
# 30/07/2026

import random

# Title
print("Haigh Gaeilge\n"
      "Irish learning program\n")

print("""\n\nTopics available:
  Basic Phrases""")
      

# Have a opening page ask kenisha about that

def learn(basic_phrases):
    print("\nWelcome to Learn")

    topic = input("Enter topic to learn: ").title()
    while True:

        # If Basic Phrases chosen set as dictionary
        if topic == "Basic Phrases":
            dictionary = basic_phrases

            # Welcome User
            print("\nLearn Basic Phrases")

            # Select Irish translation 
            print("\nSelect the correct translation for: Haigh")

            # English translation options
            print("1. Hello")
            print("2. Hi")
            print("3. Bye")

        # Get user answer selection
        user_selection = input("Enter number selection: ")

            # Check if selection correct
        if user_selection == "2":
            print("""Correct! 
            Congratulations on learning a new word!""")

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

        # Check if selection correct
        if user_selection == "3":
            print("""Correct! 
            Congratulations on learning a new word!""")

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

            # Check if selection correct
        if user_selection == "1":
            print("""Correct! 
            Congratulations on learning a new word!""")

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

            # Check if selection correct
        if user_selection == "3":
            print("""Correct! 
            Congratulations on learning a new word!""")

        else:
            print("Incorrect. Keep going!")



        # Select Irish translation 
        print("\nSelect the correct translation for: Go raibh maith agat")

        # English translation options
        print("1. Thank you")
        print("2. Welcome")
        print("3. Bye")

        # Get user answer selection
        user_selection = input("Enter number selection: ")

            # Check if selection correct
        if user_selection == "1":
            print("""Correct! 
            Congratulations on learning a new word!""")

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

            # Check if selection correct
        if user_selection == "2":
            print("""Correct! 
            Congratulations on learning a new word!""")

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

            # Check if selection correct
        if user_selection == "3":
            print("""Correct! 
            Congratulations on learning a new word!""")

        else:
            print("Incorrect. Keep going!")


        

def dictionary(basic_phrases):
    """Prints dictionaries for chosen topic"""
    print("\nWelcome to the Dictionaries")

    #Ask user for topic
    topic = input("Enter dictionary topic: ").title()

    if topic == "Basic Phrases":
        print("\nDictionary  - Basic Phrases")
        # For loop prints formatted dictionary
        for basic in basic_phrases:
            print(basic)

def profile():
    print("Profile")

    
def main():
    """Menu and holds word lists"""

    # List of dictionaries - Topic: Basic Phrases
    basic_phrases = [
        {"Hi" : "Haigh"},
        {"Hello" : "Dia duit"},
        {"Bye" : "Slán"},
        {"Please" : "Le do thoil"},
        {"Thank you" : "Go raibh maith agat"},
        {"Welcome" : "Fáilte"},
        {"Good Morning" : "Maidin mhaith"},
        {"With" : "le"},
        {"And" : "agus"},
        {"Or" : "no"},
        {"The" : "an"}
        ]

    
    # Loop
    while True:
        # Menu
        print("\n")
        print("\n---Dashboard---")
        print("1. Learn")
        print("2. Dictionary")
        print("3. Profile")
        print("0. Exit")

        # Ask for option choice
        decision = input("\nEnter number option: ")
        
        if decision == "1":
            learn(basic_phrases)

        elif decision == "2":
            dictionary(basic_phrases)

        elif decision == "3":
            profile()

        elif decision == "0":
            print("Session over.")
            break


if __name__ == "__main__":

    main()
