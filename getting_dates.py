import datetime
def working_out_date(date):
    combined_date = ''
    year = int(date[0:4])
    if date[4] == 0:
        month = int(date[5])
    else:
        month = int(date[4:6])
    if date[6] == 0:
        day = int(date[7])
    else:
        day = int(date[6:8])

    a_date = datetime.date(year, month , day)
    days = datetime.timedelta(7)
    new_date = a_date - days
    split_text_artist = str(new_date).split('-')
    for text in split_text_artist:
        combined_date += text
    return combined_date
def formated_date(date):
    combined_date = ''
    year = int(date[0:4])
    if date[4] == 0:
        month = int(date[5])
    else:
        month = int(date[4:6])
    if date[6] == 0:
        day = int(date[7])
    else:
        day = int(date[6:8])

    a_date = datetime.date(year, month, day)
    a_date = str(a_date).replace("-", "/")

    return a_date


#date = "20200626"
#print(formated_date(date))
#while int(date) > 20190000:
 #   date = working_out_date(date)
  #  print("https://www.officialcharts.com/charts/uk-top-40-singles-chart/" + date +"/750140/")