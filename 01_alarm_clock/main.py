import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm time set for {alarm_time}")
    sound_file = "01 AIZO.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("Wake Up!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
                stop_music = input("Enter q to stop: ").lower()
                if stop_music == "q":
                    pygame.mixer.music.stop()
            is_running = False

        time.sleep(1)



if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)