from faker import Factory
import csv

with open('../data/data.csv', 'w+') as f:
    csv_writer = csv.writer(f)
    fake = Factory.create()

    for i in range(5000000):
        l = [fake.md5(), fake.random_number(10)]
        l.extend(fake.words(10))
        csv_writer.writerow(l)