import datetime

thst = datetime.timezone(datetime.timedelta(hours=7 ))

# Set the due date to December 19, 2021 at 8:00 PM THST
due_date = datetime.datetime(2022, 12, 19, 20, 0, 0, tzinfo=thst)
cvt = datetime.timezone(datetime.timedelta(hours=0))
datetime = due_date.astimezone(cvt)
print(str(datetime.day)+'$'+str(datetime.hour))