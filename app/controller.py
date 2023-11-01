import hashlib
import logging
import validators

def shorten_url(user_input):

    logging.info("User Input is ",user_input)
    output_hash_string=hashlib.md5(user_input.encode())
    output_hash_string_in_user_readable_format=output_hash_string.hexdigest()
    output_hash_string_formatted=output_hash_string_in_user_readable_format[0:7]
    return output_hash_string_formatted

def find_if_valid_url(user_input):
    if(validators.url(user_input)):
        return True
    return False