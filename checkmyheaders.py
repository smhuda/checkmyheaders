"""

HTTP Security Headers Checker (CHM)

This script checks a website URL input by the user for common security-related HTTP response headers
and allows the user to export the results to a CSV file.

Author: Syed Huda
Date: 2023-11-08
Version: 1.0
Contact: @global404
License: Specify your license (e.g., MIT, GPL, etc.)

Usage: Run this script and follow the on-screen prompts.

Requirements:
- Python 3.x
- requests library
- tqdm library

Installation of required libraries:
$ pip install -r requirements.txt

"""


import requests
from tqdm import tqdm
import csv
import os
import platform
import time  # Import the time module


# Function to set the terminal title
def set_terminal_title(title):
    if platform.system() == "Windows":
        os.system(f'title {title}')
    else:
        os.system(f'echo -ne "\033]0;{title}\007"')

# Function to export results to a CSV file
def export_to_csv(missing_headers, filename='missing_headers.csv'):
    with open(filename, 'w', newline='') as csvfile:
        header_writer = csv.writer(csvfile)
        header_writer.writerow(['Missing Headers'])
        for header in missing_headers:
            header_writer.writerow([header])
    print(f"Results have been exported to {filename}")

# Set the terminal title to "CMH"
set_terminal_title("CheckMyHeaders")

# Print the title in the console
print(r"""
█▀▀ █░█ █▀▀ █▀▀ █▄▀ █▀▄▀█ █▄█ █░█ █▀▀ ▄▀█ █▀▄ █▀▀ █▀█ █▀
█▄▄ █▀█ ██▄ █▄▄ █░█ █░▀░█ ░█░ █▀█ ██▄ █▀█ █▄▀ ██▄ █▀▄ ▄█

CheckMyHeaders (CMH) - HTTP Security Headers Checker
""")

# Define the list of security headers to check
SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Strict-Transport-Security",
    "Referrer-Policy",
    "Permissions-Policy",
    "X-XSS-Protection"
]

# Function to check security headers
def check_security_headers(url, follow_redirects, cookies, auth_token):
    headers = {}
    if cookies:
        headers['Cookie'] = cookies
    if auth_token:
        headers['Authorization'] = f"Bearer {auth_token}"

    try:
        response = requests.head(url, allow_redirects=follow_redirects, headers=headers)
        headers = response.headers

        missing_headers = [header for header in SECURITY_HEADERS if header not in headers]
        return missing_headers

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Take inputs from the user
input_url = input("Enter the URL of the website to check: ")
follow_redirects_input = input("Follow redirects? (yes/no): ")
cookies_input = input("Enter cookie if needed (name=value; name2=value2; ...): ").strip()
auth_token_input = input("Enter Authorization bearer token if needed: ").strip()

follow_redirects = follow_redirects_input.lower() == 'yes'

# Validate and process the URL
if not input_url.startswith(('http://', 'https://')):
    print("Please include the protocol (http:// or https://) in your URL.")
else:
    print("Checking headers, please wait...")
    # Simulate a loading bar for terminal output
    for _ in tqdm(range(10), desc="Analyzing", ascii=False, ncols=75):
        time.sleep(0.1)  # Sleep is just for demonstration

    missing_headers = check_security_headers(input_url, follow_redirects, cookies_input, auth_token_input)
    if missing_headers is not None:
        if missing_headers:
            print("\nThe following security headers are missing:")
            for header in missing_headers:
                print(f"- {header}")
            
            # Ask user if they want to export the results
            export_choice = input("\nDo you want to export the results to a CSV file? (yes/no): ").strip().lower()
            if export_choice == 'yes':
                filename = input("Enter the desired CSV filename (or press enter for 'missing_headers.csv'): ").strip()
                filename = filename if filename else 'missing_headers.csv'
                export_to_csv(missing_headers, filename)
        else:
            print("\nAll common security headers are present.")
