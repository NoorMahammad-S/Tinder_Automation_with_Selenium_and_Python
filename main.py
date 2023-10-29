from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Update with your Facebook login email and password
FB_EMAIL = "YOUR FACEBOOK LOGIN EMAIL"
FB_PASSWORD = "YOUR FACEBOOK PASSWORD"

# Provide the path to your chromedriver executable
chrome_driver_path = "chromedriver.exe"  #chromdriver.exe file location
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Open Tinder website
driver.get("https://tinder.com/")

sleep(2)

# Find and click the login button
login_button = driver.find_element(By.XPATH, '//*[@id="s-1432688076"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_button.click()

sleep(2)

# Find and click the Facebook login button
fb_login = driver.find_element(By.XPATH, '//*[@id="s-1211347640"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div')
fb_login.click()

#Switch to Facebook login window
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# Print the title of the Facebook login window
print(driver.title)


# Find and fill in the email and password fields, then press ENTER
email = driver.find_element(By.XPATH, '//*[@id="email"]')
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

# Switch back to the Tinder window
driver.switch_to.window(base_window)
print(driver.title)

#Allow location
allow_location_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

#Disallow notifications
notifications_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

#Allow cookies
cookies = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()


#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):
    #Add a 1 second delay between likes.
    sleep(1)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH,
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            # Handle cases where there is a "Matched" pop-up in front of the "Like" button
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            # Handle cases where the "Like" button has not yet loaded, wait 2 seconds before retrying.
            sleep(2)

driver.quit()