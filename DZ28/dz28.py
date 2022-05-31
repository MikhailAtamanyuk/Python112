import csv
data = [['hostname', 'vendor', 'model', 'location'],
['sw1',  'Cisco',  '3750',  'London'],
['sw2',  'Cisco',  '3850',  'Liverpool'],
['sw3',  'Cisco',  '3650',  'Liverpool'],
['sw4',  'Cisco',  '3650',  'London']]

with open('data2.csv', 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in data:
        writer.writerow(row)

with open('data2.csv') as f:
    print(f.read())