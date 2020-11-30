import datetime
try:
    birthday = input("When is your birthday?")
    birthday = datetime.datetime.strptime(birthday,"%d/%m/%Y").date()
    if birthday <= datetime.date.today():
        print("Your birthday is in "+ birthday.strftime('%d, %B %Y'))
    else:
        print("Date Should be less than current date")
except:
    print("date or format is invalid")
