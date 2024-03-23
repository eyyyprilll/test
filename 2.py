# Print the header in bold and magenta color
    print("\033[1m\033[95m" + header)
    # Iterate over each line in the content and print it
    for line in content:
        print(line)
    # Print the footer of the fancy output
    print(header + "\033[0m")
