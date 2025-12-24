import datetime
import time

def countdown_to_new_year():
    today = datetime.datetime.now()
    new_year = datetime.datetime(today.year + 1, 1, 1)

    while True:
        current_time = datetime.datetime.now()
        time_left = new_year - current_time
        total_seconds = time_left.total_seconds()

        if total_seconds <= 0:
            print("\n Happy New Year!")
            break

        days = int(total_seconds // 86400)
        hours = int((total_seconds % 86400) // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)

        print(f"Time until New Year: {days} day(s) {hours:02} hour(s) {minutes:02} minute(s) {seconds:02} second(s)", end="\r")
        time.sleep(1)

countdown_to_new_year()
