import random
import string

# ANSI color codes for formatting
GREEN = '\033[92m'
RESET = '\033[0m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'

def pass_king_banner():
    print(f"""
    {CYAN}#######################################################
    #                                                     #
    #            {MAGENTA}██████  █████  ███████ ███████           {CYAN}#
    #           ██      ██   ██ ██      ██                #
    #           ██      ███████ █████   ███████           #
    #           ██      ██   ██ ██           ██           #
    #            ██████ ██   ██ ███████ ███████           #
    #                                                     #
    #                  {MAGENTA}Welcome to {CYAN}PASS_KING               #
    #                       {MAGENTA}@{CYAN}Anand7758                    #
    ####################################################### {RESET}
    """)

def generate_strong_password():
    print("\n### Strong Password Generator ###")
    name = input("Enter any name to include in your password: ")
    numbers = input("Enter up to 5 numbers (min 2): ")
    
    if len(numbers) < 2 or len(numbers) > 5:
        print("Invalid input. Please enter between 2 and 5 numbers.")
        return
    
    special_chars = []
    for i in range(2):
        char = input(f"Enter special character {i+1}: ")
        special_chars.append(char)
    
    try:
        strength = int(input("Enter password length (min 8, max 16): "))
        if strength < 8 or strength > 16:
            print("Invalid input. Password length must be between 8 and 16.")
            return
    except ValueError:
        print("Please enter a valid number for password length.")
        return
    
    # Ensure the password includes at least 2 uppercase letters
    uppercase_chars = random.choices(string.ascii_uppercase, k=2)
    base_components = name + numbers + ''.join(special_chars) + ''.join(uppercase_chars)
    additional_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=strength-len(base_components)))
    
    all_chars = list(base_components + additional_chars)
    random.shuffle(all_chars)
    password = ''.join(all_chars[:strength])
    
    print(f"{GREEN}Generated Password: {password}{RESET}\n")

def generate_password_list():
    print("\n### Password List Generator for Brute Force ###")
    target_name = input("Enter the target name for password list: ")
    numbers = input("Enter numbers to include in passwords: ")
    
    include_more_numbers = input("Would you like to add additional numbers? (y/n): ").strip().lower()
    if include_more_numbers == 'y':
        additional_numbers = input("How many additional numbers do you want to add? ")
        numbers += additional_numbers
    
    add_special = input("Do you want to include special characters? (y/n): ").strip().lower()
    if add_special == 'y':
        special_char_count = int(input("How many special characters do you want to add? "))
        special_chars = [input("Enter special character: ") for _ in range(special_char_count)]
    else:
        special_chars = []
    
    try:
        min_strength = int(input("Enter minimum password length: "))
        max_strength = int(input("Enter maximum password length: "))
        if min_strength < 1 or max_strength < min_strength:
            print("Invalid input for password strength range.")
            return
    except ValueError:
        print("Please enter valid numbers for password strength.")
        return
    
    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
    except ValueError:
        print("Invalid input. Enter a number.")
        return
    
    passwords = []
    for _ in range(num_passwords):
        length = random.randint(min_strength, max_strength)
        base = target_name + numbers + ''.join(special_chars)
        
        # Ensure each password has at least two uppercase characters
        uppercase_chars = random.choices(string.ascii_uppercase, k=2)
        additional_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=length - len(base) - 2))
        all_chars = list(base + ''.join(uppercase_chars) + additional_chars)
        
        random.shuffle(all_chars)
        password = ''.join(all_chars[:length])
        passwords.append(password)
    
    with open("Special_password_list.txt", "w") as file:
        for password in passwords:
            file.write(password + "\n")
    
    print(f"{GREEN}Passwords saved in 'Special_password_list.txt'.{RESET}")
    print(f"{GREEN}Generated Passwords:{RESET}\n")
    for password in passwords:
        print(f"{GREEN}{password}{RESET}")

def main():
    pass_king_banner()
    while True:
        print("\nOptions:")
        print("1. Generate a Strong Password")
        print("2. Create a Password List for Brute Force")
        choice = input("Choose an option (1 or 2, or 'q' to quit): ")
        
        if choice == '1':
            generate_strong_password()
        elif choice == '2':
            generate_password_list()
        elif choice.lower() == 'q':
            print("Exiting PASS_KING. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
