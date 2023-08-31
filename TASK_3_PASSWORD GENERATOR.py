import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=[]{}|;:,.<>?`~"
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Password Generator")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError("Password length should be a positive integer.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
