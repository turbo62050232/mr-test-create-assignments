# import schedule
# import time
import datetime
# def job():
#     print("I'm working...")

# schedule.every(1).second.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("22:07").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
# schedule.every().minute.at(":17").do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
thst = datetime.timezone(datetime.timedelta(hours=7))
dateNow = datetime.datetime.now(tz=thst)
print("Current date and time:", dateNow)

# Add 3 days to the current date
dateAfter = dateNow + datetime.timedelta(days=3)
print("Date and time 3 days later year:", dateAfter.year," month:", dateAfter.month," day:", dateAfter.day," hour:", dateAfter.hour," minute:",dateAfter.minute)