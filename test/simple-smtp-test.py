'''
Created on Jan 13, 2021

@author: jct

A simple and not-to-be-maintained program to test exchanges with smtp
servers.
'''

import smtplib
from creds import SMTPCreds


if __name__ == '__main__':
    creds = SMTPCreds()
    
    fromaddr = "jthompson@delligattiassociates.com"
    #toaddr = "jtoftx@gmail.com"
    #toaddr = "kzinti@protonmail.com"
    toaddr = "blinkenjim@gmail.com"
    #msg="From: " + fromaddr + "\r\nTo: " + toaddr + "\r\nSubject: From Python.\r\n\r\nfoobar.\r\n"
    #msg = msg.encode('utf-8')
    
    msg = """To: blinkenjim@gmail.com
User-Agent: Microsoft-MacOutlook/16.44.20121301
Subject: Welcome to the Delligatti Associates OCSMP
 Accelerator SysML training course
From: Jim Thompson <jthompson@delligattiassociates.com>
Thread-Topic: Welcome to the Delligatti Associates OCSMP
 Accelerator SysML training course
Thread-Index: AQHW5eBkSi8yeZixKUm3/yRARlkm3w==
Content-type: text/plain;
    charset="UTF-8"
Content-transfer-encoding: quoted-printable
MIME-Version: 1.0

This is a test.
"""
    
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
