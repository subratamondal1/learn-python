# Ask user for their name
name:str = input("What is your name? ")

# Remove whitespace and capitalize
name = name.strip().title()

# Split String
firstname, lastname = name.split()

# Say hello to user
print(f"hello, {firstname}")