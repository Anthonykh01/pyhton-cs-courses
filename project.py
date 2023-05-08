import requests
from bs4 import BeautifulSoup

url = 'https://myportal.lau.edu.lb/'
login_url = 'https://myportal.lau.edu.lb/pkmslogin.form'
credentials = {
    'username': 'anthony.khoury03',
    'password': 'A.K71919769',
    'login-form-type': 'pwd'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

# Create a session
session = requests.Session()
session.headers.update(headers)

# Get the login page
response = session.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Get the login form
login_form = soup.find("form", {"id": "loginfrm"})

# Submit the login form
response = session.post(login_url, data=credentials)

# Wait for 10 seconds before checking if we are redirected
import time
time.sleep(10)

# Check if we are redirected to the student portal page
while True:
    if response.url == 'https://myportal.lau.edu.lb/Pages/studentPortal.aspx':
        print("Login successful, redirected to the student portal page.")
        break
    elif response.url.startswith('https://myportal.lau.edu.lb/pkmslogin.form'):
        print("Login failed or not redirected. Current URL:", response.url)
        break
    else:
        # Follow the temporary redirect
        response = session.get(response.url)
        time.sleep(2)

# Get the student portal page
student_portal_url = 'https://myportal.lau.edu.lb/Pages/studentPortal.aspx'
response = session.get(student_portal_url)

# Print the page content
print(response.text)
