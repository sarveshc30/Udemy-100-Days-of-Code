import smtplib
import datetime as dt
import random
day = dt.datetime.now().weekday()

if day == 0:
    with open(r'F:\email.txt', 'r') as file:
        email = file.read()

    # An App Password must be generated from your account settings
    with open(r'F:\App Password.txt', 'r') as file:
        password = file.read()

    with open('quotes.txt', 'r') as file:
        quotes = file.readlines()

    quote = random.choice(quotes).strip()

    #This SMTP is specific to gmail, lookup the SMTP address for your provider
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

