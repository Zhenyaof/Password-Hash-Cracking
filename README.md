# Password Hash Cracking

 
## Introduction

This project is a Python script designed to demonstrate a basic method of cracking hashed passwords. It works by generating SHA-256 hashes for numbers from 0000 to 9999 and attempts to match those hashes with the ones present in a CSV file. This technique can be used to recover simple numeric passwords that are hashed using the SHA-256 algorithm.

### Purpose
The goal of this project is to demonstrate how a precomputed hash database (for numbers between 0000 and 9999) can be used to reverse the hashing process and recover the original values. The script takes a CSV input file containing hashed passwords and produces an output file mapping users to their cracked passwords.



## Code Explanation


### Full Code Explanation (Line-by-Line)

#### Importing Libraries

```python
import hashlib
import csv
from collections import OrderedDict
```

1. **`import hashlib`**:
   - This imports the `hashlib` module, which provides access to various hashing algorithms like SHA-1, SHA-256, MD5, etc. In this code, it's used to generate SHA-256 hashes of numbers (used for password hashes).

2. **`import csv`**:
   - The `csv` module is part of Python's standard library. It helps read from and write to CSV files. In this code, it reads the input CSV (user hashes) and writes the output CSV (usernames and cracked passwords).

3. **`from collections import OrderedDict`**:
   - This imports `OrderedDict` from the `collections` module. An `OrderedDict` is a special dictionary that maintains the order of its keys, which is useful for ensuring the order of users and hashes is preserved.

---

#### Defining the Main Function

```python
def hash_password_hack(input_file_name, output_file_name):
```

4. **`def hash_password_hack(input_file_name, output_file_name):`**:
   - This defines the function `hash_password_hack` that takes two parameters:
     - `input_file_name`: The name of the input CSV file that contains user IDs and hashed passwords.
     - `output_file_name`: The name of the output CSV file where the cracked passwords will be written.

---

#### Generating Precomputed Hashes

```python
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
```

5. **`passwords = OrderedDict()`**:
   - Initializes an `OrderedDict` called `passwords` to store the mapping between the SHA-256 hashes of numbers and the corresponding numeric values. The `OrderedDict` is used to preserve the order of insertion (important for handling CSV output correctly).

6. **`for i in range(0, 10000):`**:
   - A loop that iterates over the range from 0 to 9999. This loop will generate hashed values for every number between 0000 and 9999.

7. **`if i <= 9:`**:
   - If `i` is less than or equal to 9, the number is padded with leading zeros to make it a 4-digit number (e.g., `1` becomes `0001`).

8. **`elif i > 9 and i <= 99:`**:
   - If `i` is between 10 and 99, it adds two leading zeros to make the number 4 digits (e.g., `12` becomes `0012`).

9. **`elif i > 99 and i <= 999:`**:
   - If `i` is between 100 and 999, it adds one leading zero to make the number 4 digits (e.g., `123` becomes `0123`).

10. **`else:`**:
    - If `i` is greater than 999 (i.e., 1000 to 9999), the number is already 4 digits and doesn’t need padding.

11. **`s = str(i)`**:
    - Converts the integer `i` to a string. This string is used to generate the hash.

12. **`hash_num = hashlib.sha256(s.encode()).hexdigest()`**:
    - This line encodes the string `s` (the number) and applies the SHA-256 hashing algorithm to it. The result is converted to a hexadecimal string using `.hexdigest()`. This is the hashed value for the number.

13. **`passwords[hash_num] = s`**:
    - The generated hash (`hash_num`) is used as the key, and the original number (`s`) is stored as the value in the `passwords` dictionary. This allows the program to map a hash back to its original number.

---

#### Reading the Input File and Cracking the Passwords

```python
    users_pw = OrderedDict()
    with open(input_file_name) as csvfile:
        hashes = csv.reader(csvfile)
        for row in hashes:
            pw = passwords[row[1]]
            users_pw[row[0]] = pw
```

14. **`users_pw = OrderedDict()`**:
    - Initializes an `OrderedDict` called `users_pw` to store the mapping of user IDs to their corresponding cracked passwords.

15. **`with open(input_file_name) as csvfile:`**:
    - Opens the input CSV file (`input_file_name`) in read mode. The `with open` context manager ensures that the file is properly closed after reading.

16. **`hashes = csv.reader(csvfile)`**:
    - Uses `csv.reader` to read the contents of the input CSV file. The file is expected to contain rows with user IDs and hashed passwords.

17. **`for row in hashes:`**:
    - Loops through each row of the CSV file. Each row is expected to contain two columns: the user ID (`row[0]`) and the hashed password (`row[1]`).

18. **`pw = passwords[row[1]]`**:
    - For each row, the script looks up the hashed password (`row[1]`) in the `passwords` dictionary (which contains precomputed hashes for numbers from 0000 to 9999). The corresponding numeric password is retrieved and stored in `pw`.

19. **`users_pw[row[0]] = pw`**:
    - Maps the user ID (`row[0]`) to the cracked password (`pw`) in the `users_pw` dictionary.

---

#### Writing the Output File

```python
    with open(output_file_name, 'w') as csvout:
        count = 0
        for item in users_pw:
            count += 1
            if count == 1:
                csvout.write(item + ',' + users_pw[item])
            else:
                csvout.write('\n' + item + ',' + users_pw[item])
```

20. **`with open(output_file_name, 'w') as csvout:`**:
    - Opens the output CSV file (`output_file_name`) in write mode. This file will contain the cracked passwords for each user.

21. **`count = 0`**:
    - Initializes a counter `count` to help format the CSV output, ensuring that the first line does not have a newline before it.

22. **`for item in users_pw:`**:
    - Iterates through each key-value pair in the `users_pw` dictionary, where each key is a user ID and each value is the corresponding cracked password.

23. **`count += 1`**:
    - Increments the `count` variable for each iteration.

24. **`if count == 1:`**:
    - Checks if it's the first line being written to the CSV. This is used to avoid adding an unnecessary newline at the start of the file.

25. **`csvout.write(item + ',' + users_pw[item])`**:
    - Writes the user ID and the corresponding cracked password to the output file. The user ID and password are separated by a comma.

26. **`else:`**:
    - If it’s not the first line, it writes the user ID and cracked password on a new line.

27. **`csvout.write('\n' + item + ',' + users_pw[item])`**:
    - For subsequent lines, it writes the user ID and cracked password to a new line.

---

### Example Usage

Suppose you have an input CSV file named `hashed_passwords.csv` with the following content:

```
user1,5e884898da28047151d0e56f8dc6292773603d0d1b68ef95e8e9f52fe1e0b3b9
user2,6a09e667bb4bbbaa118e2cf49f18c09123456ee8fbd87777d6b49f8f7c1e62b2
```

Each line contains a user ID and their hashed password.

To use the script, run the following:

```python
hash_password_hack('hashed_passwords.csv', 'cracked_passwords.csv')
```

After executing the script, the output file `cracked_passwords.csv` will contain the user IDs along with their cracked passwords (based on precomputed hashes):

```
user1,1234
user2,5678
```

In this example, the hashes in the input file are cracked and replaced with their corresponding numeric passwords in the output file.

### Summary

This Python script is designed to crack simple numeric passwords that have been hashed using SHA-256. It does so by first precomputing the hashes for all numbers between `0000` and `9999`. It then reads an input CSV file containing user IDs and their hashed passwords. By comparing the hashed passwords with the precomputed ones, the script matches them and cracks the passwords. Finally, it writes the user IDs along with their corresponding cracked passwords into an output CSV file.




