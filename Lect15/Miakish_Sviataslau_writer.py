import csv


with open('exported_contacts.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)

    writer.writerow(['Name', 'Phone', 'YOUYOUYOU'])
    writer.writerow(['mother', '234-987', 'No not you'])
    writer.writerow(["grandmother, grandfather", '234-987', 'No not you'])

    writer2 = csv.writer(csvfile, delimiter=',', quotechar='"',
                         quoting=csv.QUOTE_NONNUMERIC)

with open('exported_contacts1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)

    writer.writerow(['Name', 'Phone', 'YOUYOUYOU'])
    writer.writerow(['mother', 234_987, 'No not you'])
    writer.writerow(["grandmother, grandfather", 234987, 'No not you'])

with open('exported_contacts2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"',
                        quoting=csv.QUOTE_NONE)
try:
    writer.writerow(['Name', 'Phone', 'YOUYOUYOU'])
    writer.writerow(['mother', 234_987, 'No not you'])
    writer.writerow(["grandmother, grandfather", 234987, 'No not you'])
except:
    print("need to escape, but no escapechar set")

with open('exported_contacts3.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Phone']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Name': 'mother', 'Phone': '222-555-101'})
    writer.writerow({'Name': 'father', 'Phone': '222-555-102'})
    writer.writerow({'Name': 'wife', 'Phone': '222-555-103'})

if __name__ == '__main__':
    print('csv_writter запущена сама по себе')
else:
    print('csv_writter  импортирована')
