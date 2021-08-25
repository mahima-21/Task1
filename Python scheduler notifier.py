import time
import schedule
from plyer import notification
from playsound import playsound

def Wakeup():
    title = "Good Morning!"
    message = "Time to Wake Up!!"
    notification.notify(title=title, message=message, app_icon="Bell.ico", timeout=20, toast=False)
    playsound("Audio.mp3")
def Yoga():
    title="Yoga"
    message = "Just Breathe"
    notification.notify(title=title, message=message, app_icon="Bell.ico", timeout=20, toast=False)
    playsound("Audioyoga.mp3")
def Breakfast():
    title="Breakfast"
    message="All happiness depends on a leisurely breakfast"
    notification.notify(title=title, message=message, app_icon="Bell.ico", timeout=20, toast=False)
    playsound("Audiobreakfast.mp3")
def Lunch():
    title="Lunch"
    message="All you need is lunch"
    notification.notify(title=title, message=message, app_icon="Bell.ico", timeout=20, toast=False)
    playsound("audiolunch.mp3")
def Dinner():
    title="Dinner"
    message="Dinner is better when we eat together"
    notification.notify(title=title, message=message, app_icon="Bell.ico", timeout=30, toast=False)
    playsound("Audiodine.mp3")
def bedtime():

    title = "Bedtime"
    message = "Goodnight sleep tight don't let the bed bugs bite"
    notification.notify(title=title, message=message, app_icon="Bell.ico", timeout=30, toast=False)
    playsound("Audiosleep.mp3")
def internacademy():
    title = "The Intern Academy"
    message = "Summer Internship 2021: Python Project - TASK 1"
    notification.notify(title=title, message=message, app_icon="Bell.ico", timeout=30, toast=False)

schedule.every().day.at("06:00").do(Wakeup)
schedule.every().day.at("08:00").do(Breakfast)
schedule.every().day.at("01:00").do(Lunch)
schedule.every().day.at("20:00").do(Dinner)
schedule.every().day.at("07:00").do(Yoga)
schedule.every().day.at("18:16").do(bedtime)
schedule.every(1).minutes.do(internacademy)
while True:
    schedule.run_pending()
    time.sleep(3)
