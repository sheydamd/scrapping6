# Instagram Login Automation with Selenium & Edge

This Python script automates the login process to Instagram using the Selenium library and Microsoft Edge WebDriver.  
It mimics human interaction: visiting Instagram, handling cookie prompts, entering credentials, submitting the form, and performing post-login actions like element inspection.

---

## Features

-  Opens Instagram in Edge browser
-  Handles the cookie policy prompt
- Automatically fills in username and password
-  Clicks the login button
-  Optional: inspects the page after login for verification or scraping
-  Sleeps for 100 seconds to allow manual interaction or debugging
## installation 
`bash`
- Make venv by using:
    - python -m venv .venv
- active it by using:
    - .venv\scripts\activate
- install selenium by using:
    - pip install selenium
- instagram account:
    - Create an account
and you should import:
```python
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
```


## Script Behavior

1. Launches Instagram login page


2. Accepts cookie prompt (if shown)


3. Fills in the username and password fields


4. Submits the login form


6. Waits 100 seconds before closing

## How to Run

1. Make sure you have Python 3 installed.

2. Run the script:

`bash`
python insta.py



