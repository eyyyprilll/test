# Define a function to print the formatted dream job information
def print_fancy(name, birthday, dream_job):
    # Define the header for the fancy output
    header = "*****************************"
    # Define the content with formatted strings for name, birthday, and dream_job
    content = [
        f"* Name: {name.ljust(26)} *",
        f"* Birthday: {birthday.ljust(22)} *",
        f"* Dream Job: {dream_job.ljust(19)} *"
    ]