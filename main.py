import re
from itertools import chain
# Task 1
with open('test_emails.txt', 'r') as file:
    filelines = file.read()

# Task 2 getting names without regrex
python_code_name = []
for line in filelines.strip().split("\n"):
    if line.startswith("From:"):
        for count in range(len(line)):
            if line[count] == "<":
                break
        string_slicing = line[7:count - 2]
        python_code_name.append((string_slicing))
print("Task 2 answers:")
for name in python_code_name:
    print(name)

# Task 3 Getting names using Regrex
python_regrex = re.findall(r'From: "(.*?)" <', filelines)
print("Task 3 answers:")
for name in python_regrex:
    print(name)

# Task 4 getting emails using Regrex
python_regrex_emails = re.findall(r'Return-Path: <(.*?)>', filelines)
print("Task 4 answers:")
python_regrex_emails=list(set(python_regrex_emails))
for name in python_regrex_emails:
    print(name)


# Task 5 extracting the first part of the email address
first_part = [re.findall(r'(.*?)\@', email) for email in python_regrex_emails]
print("Task 5 answers:")
first_part = list(chain(*first_part))
for name in first_part:
    print(name)

# Task 5 extracting the second part of the email address
second_part = [re.findall(r'@(.*)', email) for email in python_regrex_emails]
print("Task 6 answers:")
second_part = list(chain(*second_part))
for name in second_part:
    print(name)

