'''
Created on Jan 12, 2021

@author: jct
'''

import smtplib

class SMTPInterface:
    def __init__(self):
        print("Init SMTP interface")
        self._server = None

    def readyService(self, service, creds):
        '''
        Get the SMTP service ready to use. Connect to the SMTP server
        specified using service with the authentication credentials
        specified in creds.

        '''

        print("Connecting SMTP")

        print("---> connect")

        # Get the hostname, port number, and name of the local
        # hostname from the service dictionary.
        server_addr = service["server_addr"]
        port = service["port"]
        local_hostname = service["local_hostname"]

        # Connect to the server
        self._server = smtplib.SMTP(host = server_addr,
                                    port = port,
                                    local_hostname = local_hostname)
        # self._server.set_debuglevel(1)

        # Start TLS (encryption mode).
        print("---> starttls")
        self._server.starttls()

        # And log in with the provided credentials
        print("---> login")
        self._server.login(creds.username, creds.password)

    def sendmail(self, fromaddr, toaddr, message):
        '''Send a message from the specified email address to the
        specified email address.
        '''
        print("---> sendmail from<%s>, to <%s>" % (fromaddr, toaddr))
        self._server.sendmail(fromaddr, toaddr, message)

    def terminateService(self):
        '''Log out and disconnect from the IMAP server. '''
        print("---> quit")
        self._server.quit()


