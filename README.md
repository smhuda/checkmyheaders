# CheckMyHeaders - HTTP Security Headers Checker

This Python script checks for common security-related HTTP response headers that are missing from a given website URL. It's a simple tool to help web developers and security researchers ensure that their websites implement these headers, which can provide an added layer of security.

## Features

- Check for missing HTTP security headers.
- Follow redirects to see the final headers.
- Input cookies for sessions if needed.
- Input Authorization bearer token for authenticated pages.

## Installation

First, clone this repository:

```bash
git clone https://github.com/smhuda/checkmyheaders.git
cd checkmyheaders
```

## Pre-Requisites

Then, install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the script with the following command:

```bash
python check_headers.py <url>
```

1. When prompted, enter the URL of the website you want to check. Make sure to include `http://` or `https://`.
2. Enter yes or no when asked if you want to follow redirects.
3. If needed, input the session cookie and/or Authorization bearer token when prompted. This is necessary for authenticated pages that require login.
4. The script will output the missing HTTP security headers if there are any.
5. You can choose to save the results output as a CSV.

## Contributing
Contributions are welcome! If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

## License

This project is licensed under the MIT License.

## Contact

**Syed Huda**

- <https://www.smhuda.com/>
- 𝕏 <https://twitter.com/global404>
- <irongeek404@proton.me>

## Project Link: 
https://github.com/smhuda/checkmyheaders
