import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def is_valid_phone_number(phone_number):
    pattern = r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$'
    return bool(re.match(pattern, phone_number))


print(is_valid_email("nexiq1337@gmail.com"))
print(is_valid_email("nexiq@!1337@gmail.com"))

print(is_valid_phone_number("89123456789"))
print(is_valid_phone_number("89123456789"))
print(is_valid_phone_number("+7(123)456-78-90"))
print(is_valid_phone_number("+7 912 345 67 89"))
print(is_valid_phone_number("8(912)345-67-89"))
print(is_valid_phone_number("8 912 345 67 89"))