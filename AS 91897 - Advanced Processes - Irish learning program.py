##
# AS 91897 - Advanced Processes
# Jayani Bhula
# 30/07/2026

# Title
print("Haigh Gaeilge\n"
      "Irish learning program\n")

print("""Topics available:
  Basic Phrases""")
      

# Have a opening page ask kenisha about that

def learn():
    print("\nWelcome to Learn")


def dictionary(basic_phrases):
    """Prints dictionaries for chosen topic"""
    print("\nWelcome to the Dictionaries")

    #Ask user for topic
    topic = input("Enter dictionary topic: ").title()

    if topic == "Basic Phrases":
        print("\nDictionary  - Basic Phrases")
        # for loop print formatted dictionary
        for basic in basic_phrases:
            print("English: {:12} | Irish: {:20} |".format
              (basic['English'], basic['Irish']))


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
        print("\n---Dashboard---")
        print("1. Learn")
        print("2. Dictionary")
        print("3. Profile")
        print("0. Exit")

        # Ask for option choice
        decision = input("\nEnter number option: ")
        
        if decision == "1":
            learn()

        elif decision == "2":
            dictionary(basic_phrases)

        elif decision == "0":
            print("Session over.")
            break


if __name__ == "__main__":

    main()
