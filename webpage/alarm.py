from spotipy import Spotify
import schedule
import time
import threading

def play_track(track_uri):
    sp = Spotify()
    sp.start()
    sp.play(uris=[track_uri])


def run_alarm():
    # Set the alarm time here
    alarm_time = "06:00"

    # Schedule the play_track function to run at the alarm time
    schedule.every().day.at(alarm_time).do(play_track, "alarm/alarm.mp3")

    # Run the scheduler in a loop
    while True:
        schedule.run_pending()
        time.sleep(1)

t = threading.Thread(target=run_alarm)
t.start()