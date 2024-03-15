# SecurePassChecker

SecurePassChecker is a Python tool designed to enhance online security by allowing users to verify the integrity of their passwords. It leverages the "Have I Been Pwned" API to check whether passwords have been compromised in data breaches. This README provides an overview of the tool, installation instructions, usage guidelines, security considerations, acknowledgments, and information on using the GUI version.

## Overview

SecurePassChecker is a Python program that assists users in verifying the security of their passwords by checking them against a database of known compromised passwords. It utilizes the "Have I Been Pwned" API to query password hashes and determine if they have appeared in any data breaches.

## Prerequisites

Before using SecurePassChecker, ensure that you have the following:

- Python 3.x installed on your system.
- Internet connectivity to fetch data from the "Have I Been Pwned" API.
- Necessary permissions to run Python scripts on your system.

## Installation

There is no explicit installation process for SecurePassChecker. Simply download the provided Python script (`checkmypass.py`) and run it using Python from the command line or terminal.

## Usage

To use SecurePassChecker from the command line, follow these steps:

1. Open your command line or terminal.
2. Navigate to the directory containing the `checkmypass.py` script.
3. Run the script with the command:

python checkmypass.py <password1> <password2>

Replace `<password1>`, `<password2>`, etc., with the passwords you want to check.
4. SecurePassChecker will then query the "Have I Been Pwned" API to determine if any of the provided passwords have been compromised.
5. Review the output to see if any of your passwords were found in data breaches.
6. If a password is found to be compromised, it is advisable to change it immediately.

Alternatively, users can use the GUI version of SecurePassChecker by running the `gui.py` script.

## Security Considerations

- SecurePassChecker only sends the first five characters of a password hash to the "Have I Been Pwned" API, ensuring that the full password is never transmitted over the network.
- Passwords are hashed using the SHA-1 algorithm before being checked against the API, providing an additional layer of security.
- While SecurePassChecker provides a useful tool for checking password security, it is essential to exercise caution and use strong, unique passwords for each online account.

## Disclaimer

SecurePassChecker is provided as-is without any guarantees or warranties. The developers are not responsible for any misuse or consequences resulting from the use of this tool. Use at your own risk.

## Credits

SecurePassChecker utilizes the "Have I Been Pwned" API, developed and maintained by Troy Hunt (@troyhunt). Special thanks to Troy and the "Have I Been Pwned" team for providing this valuable service.

## Feedback and Contributions

Feedback and contributions to SecurePassChecker are welcome! If you encounter any issues, have suggestions for improvements, or would like to contribute to the project, please feel free to submit an issue or pull request on GitHub.

---

This README provides a comprehensive overview of SecurePassChecker, including information on usage from the command line and using the GUI version. For further information or assistance, please refer to the project's documentation or contact the developers.

**Happy password checking!**
