'''
Created on Jan 12, 2021

@author: jct
'''

import logging
import smtplib

def info(str_):
    print("SMTP: " + str_)
    logging.info("SMTP: " + str_)

def debug(str_):
    logging.debug("SMTP: " + str_)

class SMTPInterface:
    def __init__(self):
        debug("Initializing")
        self._server = None

    def readyService(self, service, creds):
        '''
        Get the SMTP service ready to use. Connect to the SMTP server
        specified using service with the authentication credentials
        specified in creds.

        '''

        # Get the hostname, port number, and name of the local
        # hostname from the service dictionary.
        server_addr = service["server_addr"]
        port = service["port"]
        local_hostname = service["local_hostname"]
        
        info("Connecting %s:%s" % (server_addr, port))

        # Connect to the server
        self._server = smtplib.SMTP(host = server_addr,
                                    port = port,
                                    local_hostname = local_hostname)

        # Start TLS (encryption mode).
        debug("---> StartTLS")
        self._server.starttls()

        # And log in with the provided credentials
        debug("---> Login")
        print("Using user = <%s>, password = <%s>" % (creds.username, creds.password))
        self._server.login(creds.username, creds.password)

    def sendmail(self, fromaddr, toaddr, message_str):
        '''Send a en_message from the specified email address to the
        specified email address.
        '''
        info("---> sendmail from<%s>, to <%s>" % (fromaddr, toaddr))
        self._server.sendmail(fromaddr, toaddr, message_str)
        
    from email.policy import default
    MHTMLPolicy = default.clone(linesep='\r\n', max_line_length=0)
    
    def message_bytes(self, message_obj):
        return message_obj.as_bytes(policy = self.MHTMLPolicy)

    def send_message(self, fromaddr, toaddr, message_obj):
        info('---> sendmail from "%s", to "%s"' % (fromaddr, toaddr))
        message_bytes = message_obj.as_bytes(policy = self.MHTMLPolicy)
        self._server.sendmail(fromaddr, toaddr, message_bytes)
        
#         self._server.send_message(message_obj,
#                                   from_addr = fromaddr,
#                                   to_addrs = toaddr)

    def terminateService(self):
        '''Log out and disconnect from the IMAP server. '''
        debug("---> quit")
        self._server.quit()


