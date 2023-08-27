import time
from functools import wraps
from datetime import datetime



def format_message(func):
    """Decorator to format the message given by the certstream flow, in order to obtain olny the relevan information
    Args:
        func (_type_): function to be decorated
    """
    @wraps(func)
    def wrapper_format_message(message,context):
        info = dict()
        info['domains'] = message['data']['leaf_cert']['all_domains']
        info['issuer'] = message['data']['leaf_cert']['issuer']['O']
        info['not_after'] = time.ctime(message['data']['leaf_cert']['not_after'])
        info['not_before'] = time.ctime(message['data']['leaf_cert']['not_before'])
        #func(info,context)
        return func(info,context)
    return wrapper_format_message


def add_date(func):
    """Decotaror to and a date at the beginnig of a message

    Args:
        func (_type_): fuction to be decorated
    """
    @wraps(func)
    def wapper_add_date(*args,**kwargs):
        date = datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        message_with_date = date + " -- " + kwargs['message']
        return func(*args, message = message_with_date)
    return wapper_add_date