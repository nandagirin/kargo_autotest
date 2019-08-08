# Login Unit Test

This script is used to test Login functionality in Kargo Technologies website. This script is written in Python using Selenium webdriver.

### Stacks

This script uses a number of open source library to work properly:

* [Python 3] - Programming language <https://www.python.org/downloads/>
* [Selenium Webdriver] - Library to automate web browser <https://www.seleniumhq.org/download/>
* [geckodriver] - Driver to automate the testing (Firefox in this script) <https://github.com/mozilla/geckodriver/releases>

### Installation

This script needs the Stacks mentioned above.

#### Python
```sh
$ apt install python3
```
or
Install it manually via binary file provided in the website.

#### Selenium
```sh
$ pip3 install selenium
```
or
Install it manually via binary file provided in the website.

#### Geckodriver
Download Geckodriver from the link provided and place it wherever you want in your directory.
> self.driver = webdriver.Firefox(executable_path = '<your geckodriver directory>')

Place your geckodriver directory inside the above code in the script.

### How to Run It?
Use terminal:
```sh
$ python3 <name of script>.py
```

### What is being tested?
This scripts test the login functionality by inserting phone number and password and then either clicking login button or pressing enter. After that, the process continue to the logout process by navigating from the home page to profile page, then click logout button.