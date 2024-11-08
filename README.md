# Selenium Automation Script for FreeCash Login

This script automates the process of interacting with the login modal on the [FreeCash](https://freecash.com/de) website. It uses **Selenium WebDriver** to navigate the website, handle cookie consent, fill in login credentials, and click the submit button in the login modal.

## Prerequisites

1. **Python 3.x**: Ensure Python 3.x is installed on your machine.
2. **Selenium**: Install the Selenium library.
3. **Chrome WebDriver**: Download the Chrome WebDriver compatible with your Chrome browser version. Ensure it is accessible in your system's PATH or specify the path to the driver in the script.

## Installation

1. Install the required Python packages:
   ```bash
   pip3 install selenium

## Usage
    
    
    python3 main.py

## Script Overview

The script performs the following tasks:

1. **Navigate to the FreeCash website**: Opens the [https://freecash.com/de](https://freecash.com/de) page.
2. **Handle Cookie Consent**: Looks for the cookie consent button with the text "Yes, I'm happy" and clicks it if found.
3. **Open Registration Modal**: Finds and clicks the **Anmelden** button to open the login modal.
4. **Enter Email and Password**: Waits for the modal, fills in the email and password fields, and clicks the submit button to submit the form.
5. **Error Handling**: Catches exceptions if elements are not found or not interactable and safely exits.

## Known Limitations

- **No reCAPTCHA Handling**: This script does not include functionality to bypass or handle reCAPTCHA challenges. FreeCash website requires reCAPTCHA verification, the script will be unable to proceed to the profile page.


## License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this software for any purpose, as long as the original copyright and license notice are included. This software is provided "as-is" without any warranties.

