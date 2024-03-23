# Define the main function to interact with the user
def main():
    # Ask the user to input their name
    name = input("\033[94mEnter your name: \033[0m")
    # Ask the user to input their birthday
    birthday = input("\033[94mEnter your birthday (YYYY-MM-DD): \033[0m")
    # Ask the user to input their dream job
    dream_job = input("\033[94mEnter your dream job: \033[0m")
    # Call the print_fancy function with the provided name, birthday, and dream job
    print_fancy(name, birthday, dream_job)
