import openai
from dotenv import load_dotenv
import sys
import os
import smtplib
import random

load_dotenv()

emailKey = os.getenv("GMAIL_KEY")
Sam = os.getenv("SAMARTH_MAIL")
Abhiram = os.getenv("ABHIRAM_MAIL")
Pavan = os.getenv("PAVAN_MAIL")
Anay = os.getenv("ANAY_MAIL")

emails = {
        1 : Sam,
        2 : Abhiram,
        3 : Pavan,
        4 : Anay
    }

def main():
    theme = input("What's the theme? ")
    secret = generate_word(theme)
    
    first, second, third = random_three()

    send_email(first, secret)
    send_email(second, secret)
    send_email(third, secret)

    print("Emails have been sent to three random people")

def random_three():
    rand = random.randint(1, 4)
    first, second, third = tuple(key for key in emails.keys() if key != rand)

    listEmails = tuple([emails[first], emails[second], emails[third]])
    return listEmails

def send_email(reciever, word):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(Sam, emailKey)
    server.sendmail(Sam, reciever, word)
    print("An email has been sent")

def generate_word(theme):
    
    message = f"Generate a word related to the theme. Respond ONLY with the word. For example if the theme is 'Pixar Movies', then a valid word would be 'Cars 2'. Make sure to make it random, don't just pick the most popular option."
    message += f"The theme is: {theme}."

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[ 
        {"role": "user", "content": message} ]
    )

    resp = response.choices[0].message.content

    return resp

if __name__ == "__main__":
    main()