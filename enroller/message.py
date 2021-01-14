'''
Created on Jan 14, 2021

@author: jct
'''

from email.parser import Parser
from email.policy import default

from centraltime import centraltime_str

def message_prep(message_str):
    message_obj = Parser(policy=default).parsestr(message_str)
    
    del message_obj['Date']
    del message_obj['User-Agent']
    del message_obj['Message-ID']
    del message_obj['Thread-Index']
    del message_obj['Thread-Topic']
    
    message_obj['Date'] = centraltime_str()    
    print("Message date = <%s>" % message_obj['Date'])
          
    message_str = message_obj.as_string()
    
    return message_str