import re

def validate_password(password):
            # define our regex pattern for validation
            pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*_=+-]).{8,16}$"

            # We use the re.match function to test the password against the pattern
            match = re.match(pattern, password)

            # return True if the password matches the pattern, False otherwise
            return bool(match)

def validate_phone(phone_number):

    # Regular expression to check if the phone number is exactly 10 digits
    phone_regex = re.compile(r'^[6-9]\d{9}$')
    # Regular expression to check if the phone number consists of repeated digits
    repeated_digits = re.compile(r'^(\d)\1{7,}')
    message = True

    if not phone_regex.match(phone_number):
        message = False

    if repeated_digits.match(phone_number):
        message = False

    return message

        
import bcrypt


def hash_password(password):
    password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt)



def check_password(password, hashed_password):
    hashed_password = hashed_password.strip('b')
    hashed_password = hashed_password.replace("'","")
    hashed_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

