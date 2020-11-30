import datetime
now = datetime.datetime.now()
key1 = now.year - 18
try:
    birthday = input("When is your birthday?")
    birthday = datetime.datetime.strptime(birthday,"%d/%m/%Y",).date()
    key2 = birthday.year+18
    if birthday <= datetime.date.today() and key2 <= now.year:
        print("Your birthday is in "+ birthday.strftime('%d, %B %Y'))
    else:
        print("You Are under 18")
except:
    print("date or format is invalid")
