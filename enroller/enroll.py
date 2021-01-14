'''
Created on Jan 12, 2021

@author: jct
'''

from creds import SMTPCreds, IMAPCreds

from imap import IMAPInterface
from smtp import SMTPInterface

from macros import macro_fill

if __name__ == '__main__':
    # Note: SMTP creds are used for both SMTP and IMAP servers.
    smtp_creds = SMTPCreds()
    imap_creds = IMAPCreds()
    
    imap_service = {
                     "server_addr": "outlook.office365.com",
                     "port": 993
                     }
    
    # smtp_service = {
    #                  "server_addr": 'smtp.office365.com',
    #                  "port": 587,
    #                  "local_hostname": 'delligattiassociates.com'
    #                }
    
    smtp_service = {
                     "server_addr": 'smtp.domain.com',
                     "port": 587,
                     "local_hostname": 'delligattiassociates.com'
                   }
    
    imap_interface = IMAPInterface()
    smtp_interface = SMTPInterface()
    
    imap_interface.readyService(imap_service, imap_creds)
    smtp_interface.readyService(smtp_service, smtp_creds)
    
    base_template = imap_interface.getTemplate("welcome-sysml")
    
    if base_template is None:
        print("***Error: template not found!")
    
    user_records = [
        { 
             b"first_name":    b"Jim",
             b"last_name":     b"Thompson",
#             b"email_address": b"jtoftx+test@gmail.com",
             b"email_address": b"jthompson@delligattiassociates.com",
             b"organization":  b"Troutflap Associates"
           },
        { 
             b"first_name":    b"Albert",
             b"last_name":     b"Troutflap",
#             b"email_address": b"jim.thompson@pobox.com",
             b"email_address": b"blinkenjim@gmail.com",
             b"organization":  b"Troutflap Associates"
           }]
    
    for dict_ in user_records:

        to_line = b"To: ${first_name} ${last_name} <${email_address}>"
        template = to_line + b"\r\n" + base_template
            
        message = macro_fill(template, dict_)
            
        #fromaddr = "jim.thompson@outlook.com"
        fromaddr = "jthompson@delligattiassociates.com"
        toaddr = dict_[b"email_address"]
#         toaddr = "jim.thompson@pobox.com"
        
#         from_line = b"From: %s\r\n" % fromaddr.encode()
#         message = from_line + message
        
        toaddr = toaddr.decode()
    
        if True:
            print_message = message
            print_message = print_message.decode('UTF-8')
            print_message = print_message.replace('\r', '')
            print(print_message)
    
        message = message.decode('UTF-8')
    
        if True:
            smtp_interface.sendmail(fromaddr, toaddr, message)
            #smtp_interface.sendmail(fromaddr, "jthompson@delligattiassociates.com", message)
    
    
    imap_interface.terminateService()
    smtp_interface.terminateService()
