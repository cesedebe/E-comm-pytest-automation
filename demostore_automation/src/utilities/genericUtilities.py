"""
Module for random unitilies. Helpful functions go here.
Example:
    generating random email

"""


import random
import string
import logging as logger



def generate_random_email_and_password(domain='supersqa.com', email_prefix='testuser', elength=10):
    """
    Generates a random email and password combination.
    :param domain:
    :param email_prefix:
    :return: dictionary. A dictionary with keys 'email' & 'password'
    """

    random_string = ''.join(random.choices(string.ascii_lowercase, k=elength))
    # email = email_prefix + '_' + random_string + '@' + domain
    email = f'{email_prefix}_{random_string}@{domain}'

    password_length = 20
    password_string = ''.join(random.choices(string.ascii_letters, k=password_length))

    random_info = {'email': email, 'password': password_string}
    logger.debug(f"Randomly generated email and password: {random_info}")

    return random_info

def generate_random_coupon_code(sufix=None, length=10):
    """
       Generates a random coupon
       Parameters:
       suffix (str): Suffix to use.
       length(int): Length of coupon
       Returns:
       code (str): Random coupon code
    """
    code = ''.join(random.choices(string.ascii_uppercase, k=length))
    if sufix:
        code += sufix

    return code

def generate_random_string(length=10, prefix=None, suffix=None):
    """
       Generates a random string
       Parameters:
       suffix (str): Suffix to use.
       prefix(str): Prefix to use
       length(int): Length of string
       Returns:
       random_string (str): Random string
    """
    random_string = ''.join(random.choices(string.ascii_lowercase, k=length))

    if prefix:
        random_string = prefix + random_string
    if suffix:
        random_string = random_string + suffix

    return random_string

if __name__ == '__main__':
    print(generate_random_email_and_password())