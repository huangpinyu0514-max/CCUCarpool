import smtplib
from email.message import EmailMessage
from text import password
import random

msg = EmailMessage()
msg["From"] = "ccucarpoolboot@gmail.com"


def send_vertification_code(email: str):
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        # server.set_debuglevel(1)
        server.starttls()
        server.login(msg["From"], password)
        msg["To"] = email
        msg["Subject"] = "【CCU Carpool】驗證碼通知"
        
        code = random.randint(100000, 999999)
        msg.set_content(f"您好:\n\n驗證碼為: {code}\n\n謝謝")
        server.send_message(msg)
        return code

