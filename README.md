# 🤖 Instagram Account Automation Bot using Temp-Mail

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Automation](https://img.shields.io/badge/Automation-Selenium-lightgrey)](https://selenium.dev/)

Automate the process of creating Instagram accounts using disposable emails from [Temp-Mail.org](https://temp-mail.org).  
This bot mimics human behavior to bypass bot detection using stealth techniques and browser automation.

---
## ✨ Features

- 🔐 Random username and strong password generation.
- 📧 Temporary email fetching from [temp-mail.org](https://temp-mail.org).
- 📝 Auto-filling Instagram sign-up forms.
- 📆 Automatic date of birth selection.
- 📤 OTP retrieval and submission via inbox scraping (regex-based).
- 💾 Stores created credentials in `BotAccountCredentials.txt`.
- 🕵️ Undetected browser session using `undetected-chromedriver`.

---

## 🛠️ Tech Stack

- **Language:** Python 3.x  
- **Libraries:**  
  - `selenium` – browser automation  
  - `undetected-chromedriver` – stealth browsing  
  - `pyautogui` – optional GUI interactions  
  - `re` – regex for OTP parsing

---

## 📁 Project Structure

```

InstagramRedTeamInternship/
│
├── bot.py           # Main automation script
├── BotAccountCredentials.txt         # Stores account credentials
├── instagram\_signup\_debug.png        # Screenshot (optional)
├── README.md                         # Project documentation
└── requirements.txt                  # Python dependencies

````

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/abhishree007/Instagram-account-automation.git
cd Instagram-account-automation
````

### 2. Install Requirements

Make sure Python 3.x is installed, then install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the Bot

```bash
python BotAccountAutomation.py
```

---

## 📋 Notes

* Ensure you have Google Chrome installed (compatible version with `undetected-chromedriver`).
* This is for **educational/research purposes only**. Do not misuse or violate Instagram’s Terms of Service.

---

## 🙋‍♀️ Author

**Abhishree Raj**
🔗 [GitHub Profile](https://github.com/abhishree007)

---