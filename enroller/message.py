'''
Created on Jan 14, 2021

@author: jct
'''

from email.parser import Parser
from email.policy import default

from centraltime import centraltime_str

def message_prep(message_str):
    '''Prepare a message (or template). This is for messages retrieved
    from an IMAP server and (probably) prepared by MS Outlook. We have
    to do some work to deOutlookify the template.
    '''

    # Parse the message (the default policy is good enough for now)
    # into a MessageObject.
    message_obj = Parser(policy=default).parsestr(message_str)

    # Delete the Date field because we are going to replace it by the
    # current date. The Date field left in the message by Outlook
    # represents the date of the most recent draft, which may cause
    # the message to be rejected by some SMTP servers (perhaps because
    # the deem the message too old?).
    del message_obj['Date']

    # Delete fields added by Outlook that aren't needed.
    del message_obj['User-Agent']
    del message_obj['Message-ID']
    del message_obj['Thread-Index']
    del message_obj['Thread-Topic']

    # Replace the Date field with a new field representing the current
    # time. Note that we use a date computed to represent Central
    # time.
    message_obj['Date'] = centraltime_str()    
    print("Message date = <%s>" % message_obj['Date'])

    # Turn the message object back into a string so we can do some
    # further manipulation of it before sending it.
    message_str = message_obj.as_string()

    # Return the fixed message.
    return message_str
