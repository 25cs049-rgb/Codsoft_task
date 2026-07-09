import random
import string

print("=" * 40)
print("      PASSWORD GENERATOR")
print("=" * 40)

# Get password length
while True:
    try:
        length = int(input("Enter the password length: "))
        if length < 4:
            print("Password length should be at least 4.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

# Character sets
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

# Ensure at least one character from each category
password = [
    random.choice(lowercase),
    random.choice(uppercase),
    random.choice(digits),
    random.choice(symbols)
]

# Remaining characters
all_characters = lowercase + uppercase + digits + symbols

for _ in range(length - 4):
    password.append(random.choice(all_characters))

# Shuffle password
random.shuffle(password)

# Convert list to string
final_password = "".join(password)

print("\nGenerated Password:")
print(final_password)
print("\nThank you for using Password Generator!")