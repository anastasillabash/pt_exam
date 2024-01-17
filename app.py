import re

class Exception(Exception):
    pass

def find_email(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    match = re.search(email_pattern, text)
    
    if match:
        print ("hello")
        return match.group()
    else:
        raise Exception( )
