import pyautogui
import time
import random
import string
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === Config ===
CREDENTIALS_FILE = "BotAccountCredentials.txt"
WAIT_TIME = 20
OTP_WAIT_ATTEMPTS = 30
RANDOM_DELAY = (2, 4)

# === Helper Functions ===
def generate_unique_username(base="News"):
    return f"{base}_{''.join(random.choices(string.ascii_lowercase, k=3))}{''.join(random.choices(string.digits, k=6))}"

def human_delay():
    time.sleep(random.uniform(*RANDOM_DELAY))

# === Stealth Browser Setup ===
options = uc.ChromeOptions()
options.add_argument("--no-first-run")
options.add_argument("--no-default-browser-check")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-extensions")
options.add_argument("--start-maximized")
options.add_argument("--disable-popup-blocking")
options.add_argument("--incognito")
#driver = uc.Chrome(version_main=137, options=options, use_subprocess=True)
driver = uc.Chrome(version_main=137, options=options)
wait = WebDriverWait(driver, WAIT_TIME)

try:
    # =============== TEMP MAIL ===============
    print("🌐 Navigating to temp-mail.org...")
    driver.get("https://temp-mail.org")
    time.sleep(7)  # Wait for the page to load completely

    human_delay()

    email_elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mail")))
    temp_email = email_elem.get_attribute("value")
    print(f"📨 Temp Email: {temp_email}")

    # =============== INSTAGRAM ===============
    print("🌐 Opening Instagram in new tab...")
    
    driver.execute_script("window.open('https://www.instagram.com/accounts/emailsignup/', '_blank');")

# Wait up to 5 seconds for the tab to open
    for _ in range(10):
        if len(driver.window_handles) > 1:
            break
        time.sleep(1)

    if len(driver.window_handles) < 2:
        raise Exception("❌ Instagram tab failed to open. Possible popup block or browser crash.")

    driver.switch_to.window(driver.window_handles[1])

    print("✔️ Switched to Instagram tab.")
    time.sleep(1)

    human_delay()


    print("✍️ Filling the signup form...")
    driver.save_screenshot("instagram_signup_debug.png")

    email_input = wait.until(EC.element_to_be_clickable((By.NAME, "emailOrPhone")))
    email_input.clear()
    email_input.send_keys(temp_email)
    human_delay()

# Make sure each field is ready before interacting
    wait.until(EC.presence_of_element_located((By.NAME, "fullName"))).send_keys("News Channel XYZ")
    human_delay()

    username = generate_unique_username()
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
    human_delay()

    password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)
    human_delay()

# Click Sign Up
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
    print("🎂 Selecting birthdate...")
    wait.until(EC.presence_of_element_located((By.XPATH, "//select[@title='Month:']"))).send_keys("Jan")
    driver.find_element(By.XPATH, "//select[@title='Day:']").send_keys("1")
    driver.find_element(By.XPATH, "//select[@title='Year:']").send_keys("2000")
    human_delay()
    driver.find_element(By.XPATH, "//button[text()='Next']").click()
    
    # =============== OTP HANDLING ===============
    
    import re

    print("⏳ Waiting for OTP (regex from page source)...")
    driver.switch_to.window(driver.window_handles[0])
    otp = None

    for attempt in range(OTP_WAIT_ATTEMPTS):
        print(f"🔄 Attempt {attempt + 1}/{OTP_WAIT_ATTEMPTS}")
        human_delay()
        time.sleep(7)  # Wait for a bit before refreshing
        #driver.refresh()

        try:
            page_source = driver.page_source

        # Match 6-digit code followed by Instagram phrase
            match = re.search(r'(\d{6})\s+is your Instagram code', page_source)
            if match:
                otp = match.group(1)
                print(f"✅ OTP Found via Regex: {otp}")
                break
            else:
                print("❌ No match found this time.")

        except Exception as e:
            print(f"⚠️ Regex OTP attempt failed: {e}")
            continue

    if otp:
        print(f"📢 OTP Received: {otp}")
        driver.switch_to.window(driver.window_handles[1])
        
        wait.until(EC.presence_of_element_located((By.NAME, "email_confirmation_code"))).send_keys(otp)
        time.sleep(2)  # allow Instagram to auto-verify

        try:
            next_button_xpath = "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div/div[2]/form/div/div[2]/div"
            wait.until(EC.element_to_be_clickable((By.XPATH, next_button_xpath))).click()
            print("➡️ Clicked 'Next' after entering OTP.")
            time.sleep(5)
        except Exception as e:
            print(f"⚠️ Failed to click 'Next' button: {e}")
        
        # Save credentials to file        
        with open(CREDENTIALS_FILE, 'a') as file:
            file.write(f"{username},{password}\n")
        print("💾 Credentials saved.")
    else:
        print("❌ OTP not received in time.")
    time.sleep(12)

except Exception as e:
    print(f"❌ Exception: {e}")
finally:
    print("🤝 Script complete. Keeping browser open so you can verify manually.")
    input("🔍 Press ENTER to close the browser manually...")
    driver.quit()