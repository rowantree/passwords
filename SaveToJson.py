import csv
import json
import secrets
import string

fields = {
    "login": ['login', 'password', 'url', 'fileRef', 'oneTimeCode'],
    "softwareLicense": ['login', 'password', 'url', 'fileRef', 'oneTimeCode']
}


def set_values(rec_type, data_row, value_list):

    field_list = []
    custom_fields = []

    if rec_type in fields:
        field_list = fields[rec_type]

    data_array = {}
    schema = ['$title', '$notes']
    data_array['title'] = data_row[2]
    for x in range(len(value_list)):
        value = data_row[x + 4].replace(r'\\n', r'\n')
        if len(value) > 0:
            if value_list[x] in field_list:
                data_array[value_list[x]] = value
            else:
                custom_fields.append({value_list[x]: value})
        schema.append('$' + value_list[x])

    if len(data_row[3]) > 0:
        data_array['notes'] = data_row[3].replace(r'\n', '\n')

    data_array['schema'] = schema

    if 'password' in data_array:
        alphabet = string.ascii_letters + string.digits + '!@#$%^&*()_+-={}|\][;:,<.>/?~`'
        data_array['password'] = ''.join(secrets.choice(alphabet) for i in range(20))  # for a 20-character password

    if len(custom_fields) > 0:
        data_array['custom_fields'] = custom_fields

    return data_array


with open(r"C:\Users\stephen\Documents\passwords.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = []
    folders = []

    for row in csv_reader:
        dict_row = {}

        recType = row[1]

        if recType == 'Account':
            dict_row = set_values(recType, row, ['login', 'domain', 'password'])

        elif recType == 'Credit Cards':
            dict_row = set_values(recType, row, ['login', 'domain', 'password'])

        elif recType == 'Web Logins':
            recType = "login"
            dict_row = set_values(recType, row, ['login', 'password', 'login_url', 'additional', 'old password'])

        elif recType == 'Passwords':
            dict_row = set_values(recType, row, ['password', 'domain'])

        elif recType == 'Vehicle Info':
            dict_row = set_values(recType, row, ['license', 'vin', 'year'])

        elif recType == 'Software':
            recType = 'softwareLicense'
            dict_row = set_values(recType, row, ['registration', 'regNbr', 'url', 'login', 'password'])

        elif recType == 'Email Accts':
            dict_row = set_values(recType, row, ['login', 'password'])

        elif recType == 'mySQL':
            dict_row = set_values(recType, row, ['login', 'password', 'login_url'])

        elif recType == 'Bank Accts':
            recType = 'bankAccount'
            dict_row = set_values(recType, row, ['account', 'pin'])

        else:
            dict_row['title'] = 'UNKNOWN'

        dict_row['folders'] = [{"folder": row[0]}]
        if not row[0] in folders:
            folders.append(row[0])
        dict_row["$type"] = recType

        data.append(dict_row)

shared_folders = []
for folder in folders:
    shared_folders.append({"path": folder})

with open(r"c:\Users\stephen\Documents\sample.json", "w") as outfile:
    json.dump({'shared_folders': shared_folders, 'records': data}, outfile, indent=4)
