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
        dictionary = basic_phrases
        print("\nLearn Basic Phrases")

        answer = random.choice(basic_phrases)
        
        print("Select correct meaning: {}".format(answer))

        random.shuffle(basic_phrases)
        print(basic_phrases)

        selection = input("Enter selection: ")
        if selection == answer:
              print("Correct")

        else:
            print("Incorrect")



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
        {"Hello" : "Dia Duit"},
        {"Bye" : "Slán"},
        {"Please" : "Le do thoil"},
        {"Thankyou" : "Go raibh maith agat"},
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
