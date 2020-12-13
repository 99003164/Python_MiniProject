import re  # import re module

def verify(email_id):  # method to verify valid email id
    if (re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email_id)):  # regular expression for validating email id
        print("Valid Email")
    else:
        print("Invalid Email")

if __name__ == '__main__':
    email_id = "mehuljain3038@gmail.com"  # valid email id
    verify(email_id)

    email_id = "mehul.jain3038@gail.com"  # valid email id
    verify(email_id)

    email_id = "mehuljain3038.com"  # invalid email id
    verify(email_id)
