import openai
from dotenv import load_dotenv
import sys
import os

load_dotenv()

def main():
    theme = "Disney Characters"
    secret = generate_word(theme)



def send_email(reciever, word):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email, secret.GMAIL_KEY)
    server.sendmail(email, reciever, word)
    return("The weather report has been sent to " + reciever)

def generate_word(theme):
    
    message = f"Generate a word related to the theme. Respond ONLY with the word. For example if the theme is 'Pixar Movies', then a valid word would be 'Cars 2'. "
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