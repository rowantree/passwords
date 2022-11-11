import csv

with open(r"C:\Users\stephen\Documents\passwords.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    with open(r"C:\Users\stephen\Documents\secrets.csv", mode='w', newline='') as csv_file_out:
        fieldNames = ['type', 'folder', 'title', 'username', 'password', 'domain', 'url', 'account', 'pin', 'domain', 'registration', 'reg nbr', 'additional', 'old password', 'license', 'vin', 'year', 'notes']
        writer = csv.DictWriter(csv_file_out, dialect='excel', fieldnames=fieldNames);
        writer.writeheader()
        for row in csv_reader:
            recType = row[1]
            if recType == 'Account':
                writer.writerow({'type': recType, 'folder': row[0], 'title': row[2], 'username': row[4], 'domain': row[5], 'password': row[6], 'notes': row[3]})
            elif recType == 'Credit Cards':
                writer.writerow({'type': recType, 'folder': row[0], 'title': row[2], 'username': row[4], 'domain': row[5], 'password': row[6], 'notes': row[3]})
            elif recType == 'Web Logins':
                writer.writerow({'type': recType, 'folder': row[0], 'title': row[2], 'username': row[4], 'password': row[5], 'url': row[6], 'additional': row[7], 'old password': row[8], 'notes': row[3]})
            elif recType == 'Passwords':
                writer.writerow({'type': recType, 'folder': row[0], 'title': row[2], 'password': row[4], 'domain': row[5], 'notes': row[3]})
            elif recType == 'Vehicle Info':
                writer.writerow({'type': recType, 'folder': row[0], 'title': row[2], 'license': row[4], 'vin': row[5], 'year': row[6], 'notes': row[3]})
            elif recType == 'Software':
                writer.writerow({'type': recType, 'folder': row[0], 'title': row[2], 'password': row[8], 'registration': row[4], 'reg nbr': row[5], 'url': row[6], 'notes': row[3]})
            elif recType == 'Email Accts':
                writer.writerow({'type': recType, 'folder': row[0], 'title': row[2], 'username': row[4], 'password': row[5], 'notes': row[3]})
            elif recType == 'mySQL':
                writer.writerow({'type': recType, 'folder': row[0], 'title': row[2], 'username': row[4], 'password': row[5], 'url': row[6], 'notes': row[3]})
            elif recType == 'Bank Accts':
                writer.writerow({'type': recType, 'folder': row[0], 'title': row[2], 'account': row[4], 'pin': row[5], 'notes': row[3]})
            else:
                writer.writerow({'type': recType, 'folder': row[0], 'title': 'UNKNOWN'})