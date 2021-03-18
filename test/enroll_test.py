'''
Created on Jan 12, 2021

@author: jct
'''

from creds import SMTPCreds, IMAPCreds

from imap import IMAPInterface
from smtp import SMTPInterface

from macros import macro_fill
from message import message_prep

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
        
    base_template = message_prep(base_template)
        
    user_records = [
        { 
             "first_name":    "Jim",
             "last_name":     "Thompson",
             "email_address": "jim.thompson@pobox.com",
#             "email_address": "jthompson@delligattiassociates.com",
             "organization":  "Troutflap Associates"
           },
        { 
             "first_name":    "Albert",
             "last_name":     "Troutflap",
#             "email_address": "jim.thompson@pobox.com",
             "email_address": "blinkenjim@gmail.com",
             "organization":  "Troutflap Associates"
           }]
    
    for dict_ in user_records:

        to_line = "To: ${first_name} ${last_name} <${email_address}>"
        template = to_line + "\r\n" + base_template
            
        
        message = macro_fill(template, dict_)
            
        #fromaddr = "jim.thompson@outlook.com"
        fromaddr = "jthompson@delligattiassociates.com"
        toaddr = dict_["email_address"]

        if True:
            print_message = message.replace('\r', '')
            print_message = print_message.strip()
            print('--------------------------------------------------------------------------------------')
            print(print_message)
            print('--------------------------------------------------------------------------------------')
    
        if False:
            smtp_interface.sendmail(fromaddr, toaddr, message)
            #smtp_interface.sendmail(fromaddr, "jthompson@delligattiassociates.com", en_message)
    
    
    imap_interface.terminateService()
    smtp_interface.terminateService()
