import openai
from dotenv import load_dotenv
import sys
import os
import smtplib
import random

load_dotenv()

emailKey = os.getenv("GMAIL_KEY")
player1 = os.getenv("PLAYER1_MAIL")
player2 = os.getenv("PLAYER2_MAIL")
player3 = os.getenv("PLAYER3_MAIL")
player4 = os.getenv("PLAYER4_MAIL")

emails = {
        1 : player1,
        2 : player2,
        3 : player3,
        4 : player4
    }

def main():
    theme = input("What's the theme? ")
    word = generate_word(theme)
    
    first, second, third = random_three()

    send_email(first, word)
    send_email(second, word)
    send_email(third, word)

    print("Emails have been sent to three random people")

def random_three():
    rand = random.randint(1, 4)
    first, second, third = tuple(key for key in emails.keys() if key != rand)

    listEmails = tuple([emails[first], emails[second], emails[third]])
    return listEmails

def send_email(reciever, word):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(player1, emailKey)
    server.sendmail(player1, reciever, word)
    print("An email has been sent")

def generate_word(theme):
    
    system = "You will be asked to generate a RANDOM word based on a theme provided by the user. Make sure to randomly pick from the theme. DO NOT pick the same option."

    message = f"Generate a word related to the theme. Respond ONLY with the word. For example if the theme is 'Pixar Movies', then a valid word would be 'Cars 2'. Make sure to make it random, don't just pick the most popular option. Dont provide words you've provided in the past"
    message += f"The theme is: {theme}."

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[ 
        {"role": "system", "content": system},
        {"role": "user", "content": message} ],
        temperature=1.5
    )

    resp = response.choices[0].message.content

    return resp

if __name__ == "__main__":
    main()