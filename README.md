# Password-Generator
Here's the README in Markdown format suitable for GitHub:

---

# PASS_KING 🔐🔥

Welcome to **PASS_KING** - a versatile and secure password generation tool with customizable options for creating strong passwords or generating password lists for brute force testing. With a colorful, flame-styled banner and easy-to-use interface, PASS_KING makes it easy to generate secure passwords based on your specific requirements.

![PASS_KING Demo Banner](banner_image_url) <!-- Replace with an actual link to an image if needed -->

## Features ✨
- **Generate Strong Passwords**: Customize a strong password by providing a name, numbers, special characters, and length.
- **Password List for Brute Force**: Generate multiple passwords for testing by customizing the target name, numbers, special characters, and desired length.
- **Stylish Interface**: The flame-bordered banner makes using PASS_KING a visually engaging experience.

## Installation 🛠️

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/PASS_KING.git
   ```
2. **Navigate to the Directory**:
   ```bash
   cd PASS_KING
   ```
3. **Run the Script**:
   Ensure you have Python 3 installed, then run:
   ```bash
   python3 pass_king.py
   ```

> **Note**: This script uses emojis and ANSI color codes, which are compatible with most modern terminals.

## Usage 📋

### Menu Options
When you run the script, you’ll be greeted with two options:

1. **Generate a Strong Password**: Create a customized, secure password based on the inputs you provide.
2. **Create a Password List for Brute Force**: Generate a list of passwords for brute force testing with specified parameters.

### Option 1: Generate a Strong Password
You can create a strong password by following these prompts:
- **Enter any name** to include in your password.
- **Enter up to 5 numbers** (minimum of 2) for added security.
- **Enter 2 special characters**, one at a time.
- **Specify password length** between 8 and 16 characters.

PASS_KING will then generate a password that includes at least two uppercase letters for enhanced security.

#### Example
```plaintext
Enter any name to include in your password: John
Enter up to 5 numbers (min 2): 123
Enter special character 1: !
Enter special character 2: @
Enter password length (min 8, max 16): 12
Generated Password: 🔐 Ab!123JohnQ@
```

### Option 2: Create a Password List for Brute Force
In this mode, you can generate multiple passwords and save them in a file called `Special_password_list.txt`. Here’s what the tool will ask:
- **Enter the target name** for the password list.
- **Include numbers** and additional numbers if desired.
- **Include special characters** and specify the count if needed.
- **Specify minimum and maximum password lengths**.
- **Set the number of passwords** you want to generate.

#### Example
```plaintext
Enter the target name for password list: Alice
Enter numbers to include in passwords: 456
Would you like to add additional numbers? (y/n): y
How many additional numbers do you want to add? 78
Do you want to include special characters? (y/n): y
How many special characters do you want to add? 2
Enter special character: $
Enter special character: %
Enter minimum password length: 8
Enter maximum password length: 12
How many passwords do you want to generate? 5

Passwords saved in 'Special_password_list.txt'.
Generated Passwords:
🔐 Alice45678$%B
🔐 Alice78%$456C
🔐 B456%$Alice78
...
```

### Output File
When generating a password list, all passwords will be saved in `Special_password_list.txt` in your current directory.

## Requirements ⚙️

- **Python 3**: Make sure Python 3 is installed on your machine.
- **Unicode and Emoji Support**: This tool uses emojis for the flame effect in the banner. Ensure your terminal supports emojis and ANSI colors.

## Contributing 🤝
Contributions are welcome! Feel free to open an issue or submit a pull request if you have ideas for improving PASS_KING. You can help by:
- Adding new password generation methods.
- Enhancing the interface.
- Improving the README or documentation.

## License 📄
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author 💼
Developed by **[Your Name](https://github.com/yourusername)**.

## Acknowledgments 🙏
Special thanks to the open-source community and anyone who has contributed ideas or code.

---

This README provides a comprehensive overview of PASS_KING. Replace `"https://github.com/yourusername/PASS_KING.git"` and `"banner_image_url"` with the actual repository link and banner image link if you upload an image to the repository. It includes installation, usage instructions, and example outputs, making it a great README for GitHub.
