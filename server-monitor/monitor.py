# import libraries
import os
import time
from mailjet_rest import Client
import psutil
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

print(f"API_KEY: {API_KEY}\nSECRET: {API_SECRET}")

# define system metrics thresholds
CPU_THRESHOLD = 2
RAM_THRESHOLD = 10
DISK_THRESHOLD = 50

# mailjet setup
mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')

# define system time
current_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",current_time)

# get current system metrics
cpu_usage = psutil.cpu_percent(interval=1)
mem_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

# function to send alert
def send_alert(subject, message):
    data = {
        'Messages': [
            {
                'From': {
                    "Email": "aaron.djaba@amalitech.com",
                    "Name": "24/7 SysMon"
                },
                "To": [
                    {
                        "Email": "aaronwilldjaba@gmail.com",
                        "Name": "Admin"
                    }
                ],
                "Subject": subject,
                "HTMLPart": f"<h1>Server Alert</h1><p>{message}</p>",
            }
        ]
    }


    try:
        result = mailjet.send.create(data=data)
        print(result.status_code)
        pprint(result.json(), compact=True)
    except Exception as e:
        pprint(f"Error sending alert: {str(e)}")

# check system metrics
cpu_usage = psutil.cpu_percent(interval=1)
# print(cpu_usage)


ram_usage = psutil.virtual_memory().percent
# print(ram_usage)


disk_usage = psutil.disk_usage('/').percent
# print(disk_usage)

alert_message = ""


if cpu_usage > CPU_THRESHOLD:
    alert_message += f"CPU usage is high: {cpu_usage}% (Threshold: {CPU_THRESHOLD}%)\n"

if ram_usage > RAM_THRESHOLD:
    alert_message += f"RAM usage is high: {ram_usage}% (Threshold: {RAM_THRESHOLD}%)\n"


if disk_usage > DISK_THRESHOLD:
    alert_message += f"Disk space is low: {100 - disk_usage}% free (Threshold: {DISK_THRESHOLD}% free)\n"


if alert_message:
    send_alert(f"Python Monitoring Alert Alert-{formatted_time}", alert_message)
else:
    print("All system metrics are within normal limits.")
