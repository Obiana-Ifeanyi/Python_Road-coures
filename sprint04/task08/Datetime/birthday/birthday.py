def birthday(dayy):
    import datetime

    try:
        today = datetime.datetime.today()

        # strftime - datetime to string
        # strptime - string to datetime
        # function arg is converted from string to datetime type
        dt = datetime.datetime.strptime(dayy, '%B %d, %Y')
        bday_month = dt.strftime("%B")

        if dt.year < today.year:
            print ('your birthday was in', dt.year)


        elif dt < today:
            time_to_birthday = abs(dt - today)
            print (f"your birthday was {time_to_birthday.days} days ago")


        elif dt > today:
            time_to_birthday = abs(dt - today)
            print (f"your birthday is in the month {bday_month} in the next {time_to_birthday.days} days")


        '''
        # add interval to date using timedelta
        tdelta = datetime.timedelta(days= time_to_birthday.days + 1)
        date_to_bday = today + tdelta
        print (date_to_bday.date())
        '''

    except ValueError as val:
        print ("invalid input,", val)
        print ("format should be in '[month date, year]' ")


dayy = input("Enter your birthday date: ")
birthday(dayy)
