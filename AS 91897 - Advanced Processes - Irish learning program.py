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

    if topic == "Basic Phrases":
        print("\nLearn Basic Phrases")

        chosen_word = random.choice(basic_phrases)
        incorrect_option = random.choice(basic_phrases)
        correct_answer = random.choice(basic_phrases)

        print(chosen_word)
        print(incorrect_option['Irish'])
        print(correct_answer)

        
        
        #answer = input("\nEnter the correct translation: ").strip().title()
        #if answer == "":
         #   print("Correct!")

        #else:
         #   print("Incorrect. The correct answer was {}".format)

        
def dictionary(basic_phrases):
    """Prints dictionaries for chosen topic"""
    print("\nWelcome to the Dictionaries")

    #Ask user for topic
    topic = input("Enter dictionary topic: ").title()

    if topic == "Basic Phrases":
        print("\nDictionary  - Basic Phrases")
        # For loop prints formatted dictionary
        for basic in basic_phrases:
            print("English: {:12} | Irish: {:20} |".format
              (basic['English'], basic['Irish']))


def profile():
    print("Profile")

    
def main():
    """Menu and holds word lists"""

    # List of dictionaries - Topic: Basic Phrases
    basic_phrases = [
        {"English" : "Hi", "Irish" : "Haigh"},
        {"English" : "Hello", "Irish" : "Dia Duit"},
        {"English" : "Bye", "Irish" : "Slán"},
        {"English" : "Please", "Irish" : "Le do thoil"},
        {"English" : "Thankyou", "Irish" : "Go raibh maith agat"},
        {"English" : "Welcome", "Irish" : "Fáilte"},
        {"English" : "Good Morning", "Irish" : "Maidin mhaith"}
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
