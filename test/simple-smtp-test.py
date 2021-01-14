'''
Created on Jan 13, 2021

@author: jct
'''

import smtplib
from creds import SMTPCreds


if __name__ == '__main__':
    creds = SMTPCreds()
    
    def prompt(prompt):
        return input(prompt).strip()
    
    # fromaddr = prompt("From: ")
    # toaddrs  = prompt("To: ").split()
    # print("Enter message, end with ^D (Unix) or ^Z (Windows):")
    
    # # Add the From: and To: headers at the start!
    # msg = ("From: %s\r\nTo: %s\r\n\r\n"
    #        % (fromaddr, ", ".join(toaddrs)))
    # while True:
    #     try:
    #         line = input()
    #     except EOFError:
    #         break
    #     if not line:
    #         break
    #     msg = msg + line
    
    fromaddr = "jthompson@delligattiassociates.com"
    #toaddr = "jtoftx@gmail.com"
    #toaddr = "kzinti@protonmail.com"
    toaddr = "blinkenjim@gmail.com"
    msg="From: " + fromaddr + "\r\nTo: " + toaddr + "\r\nSubject: From Python.\r\n\r\nfoobar.\r\n"
    #msg = msg.encode('utf-8')
    
    print("Using SMTP user = <%s>, password = <%s>" % (creds.username, creds.password))
    
    print("Message length is", len(msg))
    print("----> message follows:\n", msg)
    
    print("---> connect")
    server = smtplib.SMTP(host = 'smtp.domain.com', port = 587, local_hostname = 'delligattiassociates.com')
    
    #server.set_debuglevel(1)
    print("---> starttls")
    server.starttls()
    
    print ("---> login with user=<%s>, pass=<%s>" % (creds.username, creds.password))
    server.login(creds.username, creds.password)
    
    print("---> sendmail")
    server.sendmail(fromaddr, toaddr, msg)
    
    print("---> quit")
    server.quit()
    
    print("***> done")
