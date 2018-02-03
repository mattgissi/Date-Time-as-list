def dt():
    import datetime
    datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    datelist = []
    datelist.append(datetime.datetime.now().strftime("%I"))
    datelist.append(datetime.datetime.now().strftime("%M"))
    datelist.append(datetime.datetime.now().strftime("%p"))
    datelist.append(datetime.datetime.now().strftime("%B"))
    datelist.append(datetime.datetime.now().strftime("%d"))
    datelist.append(datetime.datetime.now().strftime("%Y"))

    return datelist

print (dt())










