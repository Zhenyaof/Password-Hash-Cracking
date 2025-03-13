import hashlib
import csv
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    passwords = OrderedDict()
    for i in range(0, 10000):
        if i <= 9:
            s = '000' + str(i)
        elif i > 9 and i <= 99:
            s = '00' + str(i)
        elif i > 99 and i <= 999:
            s = '0' + str(i)
        else:
            s = str(i)
        hash_num = hashlib.sha256(s.encode()).hexdigest()
        passwords[hash_num] = s

    users_pw = OrderedDict()
    with open(input_file_name) as csvfile:
        hashes = csv.reader(csvfile)
        for row in hashes:
            pw = passwords[row[1]]
            users_pw[row[0]] =  pw

    with open(output_file_name, 'w') as csvout:
        count = 0
        for item in users_pw:
            count += 1
            if count == 1:
                csvout.write(item + ',' + users_pw[item])
            else:
                csvout.write('\n' + item + ',' + users_pw[item])
        



