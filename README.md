# SecurePassChecker
"SecurePassChecker: Enhance online security! Check password integrity via 'Have I Been Pwned' API. Proactively protect digital accounts."

**CheckMyPass README**

---

### Overview

CheckMyPass is a Python program designed to help users verify the security of their passwords by checking them against a database of known compromised passwords. The program utilizes the "Have I Been Pwned" API to query password hashes and determine if they have appeared in any data breaches.

### Prerequisites

Before using CheckMyPass, ensure that you have the following:

- Python 3.x installed on your system.
- Internet connectivity to fetch data from the "Have I Been Pwned" API.
- Necessary permissions to run Python scripts on your system.

### Installation

There is no explicit installation process for CheckMyPass. Simply download the provided Python script (`checkmypass.py`) and run it using Python from the command line or terminal.

### Usage

To use CheckMyPass, follow these steps:

1. Open your command line or terminal.
2. Navigate to the directory containing the `checkmypass.py` script.
3. Run the script with the command:
   ```
   python checkmypass.py <password1> <password2> ...
   ```
   Replace `<password1>`, `<password2>`, etc., with the passwords you want to check.
4. CheckMyPass will then query the "Have I Been Pwned" API to determine if any of the provided passwords have been compromised.
5. Review the output to see if any of your passwords were found in data breaches.
6. If a password is found to be compromised, it is advisable to change it immediately.

### Security Considerations

- CheckMyPass only sends the first five characters of a password hash to the "Have I Been Pwned" API, ensuring that the full password is never transmitted over the network.
- Passwords are hashed using the SHA-1 algorithm before being checked against the API, providing an additional layer of security.
- While CheckMyPass provides a useful tool for checking password security, it is essential to exercise caution and use strong, unique passwords for each online account.

### Disclaimer

CheckMyPass is provided as-is without any guarantees or warranties. The developers are not responsible for any misuse or consequences resulting from the use of this tool. Use at your own risk.

### Credits

CheckMyPass utilizes the "Have I Been Pwned" API, developed and maintained by Troy Hunt (@troyhunt). Special thanks to Troy and the "Have I Been Pwned" team for providing this valuable service.

### Feedback and Contributions

Feedback and contributions to CheckMyPass are welcome! If you encounter any issues, have suggestions for improvements, or would like to contribute to the project, please feel free to submit an issue or pull request on GitHub.

---

This README provides a brief overview of CheckMyPass and instructions for installation, usage, security considerations, and more. For further information or assistance, please refer to the project's documentation or contact the developers.

**Happy password checking!**
