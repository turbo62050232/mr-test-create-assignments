import schedule
import time
import datetime
def job():
    print("I'm working...")

schedule.every(1).second.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("22:07").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)