import csv
from faker import Factory

generator = Factory.create()
data = [['first_name', 'last_name', 'email', 'date_of_birth', 'country_code', 'created_at', 'last_login_at']]

def generateRecentDateTime(datetime):
    if int(datetime.strftime('%Y')) < 2012:
        datetime = generateRecentDateTime(generator.date_time())

    return datetime

for i in range(0, 1000):
    data.append([
        generator.first_name(),
        generator.last_name(),
        generator.email(),
        generator.date(),
        generator.country_code(),
        generateRecentDateTime(generator.date_time()).strftime('%Y-%m-%d %H:%M:%S'),
        generateRecentDateTime(generator.date_time()).strftime('%Y-%m-%d %H:%M:%S')
    ])


with open('../data-set.csv', 'wb') as dataset:
    wr = csv.writer(dataset, quoting=csv.QUOTE_ALL)
    wr.writerows(data)
