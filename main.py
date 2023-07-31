import re
from itertools import chain

# Task 1
with open('test_emails.txt', 'r') as file:
    filelines = file.read()


def regular_python_on_emails_names():
    python_code_name = []
    for line in filelines.strip().split("\n"):
        if line.startswith("From:"):
            for count in range(len(line)):
                if line[count] == "<":
                    break
            string_slicing = line[7:count - 2]
            python_code_name.append((string_slicing))

    for name in python_code_name:
        print(name)


# Task 2 getting names without regrex
print("\nTask 2 answers:\n")
regular_python_on_emails_names()


def regrex_python_on_names(filetemp, flag=False):
    python_regrex = re.findall(r'From: "(.*?)" <', filetemp)
    for name in python_regrex:
        print(name)
        if flag:
            return name


# Task 3 Getting names using Regrex
print("\nTask 3 answers:\n")
regrex_python_on_names(filelines)


def python_regrex_on_emails(filetemp, temp):
    global python_regrex_emails
    if temp == "Sender":
        python_regrex_emails = re.findall(r'Return-Path: <(.*?)>', filetemp)
    else:
        python_regrex_emails = re.findall(r'(?<=\nTo: ).*?(?=\n\S)', filetemp, re.DOTALL)
    python_regrex_emails = list(set(python_regrex_emails))
    for name in python_regrex_emails:
        print(name)


# Task 4 getting emails using Regrex
print("\nTask 4 answers:\n")
python_regrex_on_emails(filelines, "Sender")


def first_part_of_email():
    first_part = [re.findall(r'(.*?)\@', email) for email in python_regrex_emails]
    first_part = list(chain(*first_part))
    for name in first_part:
        print(name)


# Task 5 extracting the first part of the email address
print("\nTask 5 answers:\n")
first_part_of_email()


def second_part_of_email():
    second_part = [re.findall(r'@(.*)', email) for email in python_regrex_emails]
    second_part = list(chain(*second_part))
    for name in second_part:
        print(name)


# Task 5 extracting the second part of the email address
print("\nTask 5 answers:\n")
second_part_of_email()


def email_date(filetemp):
    lines = filetemp.split('\n')
    print("Date: " + lines[0])


def email_subject(filetemp):
    subjects = re.findall(r'(?<=\nSubject: ).*?(?=\n\S)', filetemp, re.DOTALL)
    '''print("Subject: " + subjects[0])'''
    if isinstance(subjects, list):
        if subjects:
            print("Subject: " + subjects[0])
    elif isinstance(subjects, str):
        print("Subject: " + subjects)



def body_email(filetemp, exit_string):
    flag = False
    for line in filetemp.split("\n"):
        if flag:
            print(line)
        if line.startswith("Status:"):
            flag = True



# Task 6 Sorting
print("\nTask 6 answers:\n")
emails = filelines.split("From r")[1:]

# Process each email and print its contents
for i, email in enumerate(emails, 1):
    print(f"\nEmail {i}:")
    print("Sender Name: ", end="")
    sender_name = regrex_python_on_names(email.strip(), True)
    print("Sender Address: ", end="")
    sender_address = python_regrex_on_emails(email.strip(), "Sender")
    print("Recipient Address: ", end="")
    recipient_address = python_regrex_on_emails(email.strip(), "recipient_address")
    date_sent = email_date(email.strip())
    subject = email_subject(email.strip())
    print("email Body: ", end="")
    email_body = body_email(email.strip(), sender_name)
