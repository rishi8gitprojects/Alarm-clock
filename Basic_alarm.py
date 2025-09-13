import datetime
import time
import pygame
import csv


def Alarm_clock(args):  
    reminder_times = [(datetime.datetime.strptime(r["DateTime"], "%Y-%m-%d %H:%M:%S"), r["Message"]) for r in args]


    while reminder_times:
        now = datetime.datetime.now()
        for remindertime, message in reminder_times[:]:
            if now >= remindertime:
                print(f"{message}")
                pygame.mixer.init()
                pygame.mixer.music.load(R"path_to_your_audio_file.mp3") #update your path
                pygame.mixer.music.play()
                reminder_times.remove((remindertime, message))
        time.sleep(1)


path = r"C:\Users\Rishi Roychowdhury\Downloads\reminders.csv"
with open(path, mode='r') as file:
    csvread = csv.DictReader(file)
    reminder = list(csvread)
Alarm_clock(reminder)
