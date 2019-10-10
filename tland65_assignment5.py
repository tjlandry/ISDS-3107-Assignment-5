import sqlalchemy as sa
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
import csv

student_name = 'Todd Landry Jr'


def full_name(first, last):
    return first + ' ' + last


def age(dob):
    dob_format = dt.strptime(dob, '%Y-%m-%d')
    today = dt.today()
    age = relativedelta(today, dob_format)
    return age.years


def main():
    engine = sa.create_engine('sqlite:///customer.sqlite')
    connection = engine.connect()
    data = sa.MetaData()
    customer = sa.Table('customer', data, autoload=True, autoload_with=engine)
    query = sa.select([customer.columns.id,
                       customer.columns.first_name,
                       customer.columns.last_name,
                       customer.columns.dob])
    proxy = connection.execute(query)
    table_data = proxy.fetchall()
    connection.close()

    with open('tland65_assignment5.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Customer ID', 'Name', 'Age'])
        for x in table_data:
            writer.writerow([x[0], full_name(x[1], x[2]), age(x[3])])


if __name__ == '__main__':
    main()
