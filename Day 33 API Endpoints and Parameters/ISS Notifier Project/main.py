import requests
import datetime
import smtplib

def send_mail():
    with open(r'F:\email.txt', 'r') as file:
        email = file.read()
    # An App Password must be generated from your account settings
    with open(r'F:\App Password.txt', 'r') as file:
        password = file.read()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:Look Up\n\nLook up! the ISS is floating above your head."
        )

LATITUDE = 18.516726
LONGITUDE = 73.856255
parameters = {
    "lat": 18.516726,
    "lng": 73.856255,
    "formatted": 0,
    "tzid": "UTC"
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
print(response.json())
sunset24 = response.json()["results"]['sunset']
sunrise24 = response.json()["results"]['sunrise']
print('sunset: ', sunset24)
print('sunrise: ', sunrise24)
sunset_hour = sunset24.split('T')[1].split(':')[0]
sunrise_hour = sunrise24.split('T')[1].split(':')[0]

print(sunrise_hour, sunset_hour)
# parameters = {
#     "lat": 18.516726,
#     "lng": 73.856255,
#     "formatted": 1
# }
# response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
# sunrise12 = response.json()['results']['sunset']
# print(sunrise12)
#
time_now = datetime.datetime.utcnow()
print(time_now)
print(time_now.hour)

iss_api = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_location = (float(iss_api.json()['iss_position']['latitude']), float(iss_api.json()['iss_position']['longitude']))
print(iss_location)
if (abs(iss_location[0] - LATITUDE) <= 5) and (abs(iss_location[1] - LONGITUDE)<= 5):
    send_mail()
    print("Mail Sent")
else:
    print("Mail Not Sent")