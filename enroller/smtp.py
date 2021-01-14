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
        print("Connecting SMTP")

        print("---> connect")

        server_addr = service["server_addr"]
        port = service["port"]
        local_hostname = service["local_hostname"]
        
        self._server = smtplib.SMTP(host = server_addr,
                                    port = port,
                                    local_hostname = local_hostname)
        # self._server.set_debuglevel(1)

        print("---> starttls")
        self._server.starttls()

        print("---> login")
        self._server.login(creds.username, creds.password)

    def sendmail(self, fromaddr, toaddr, message):
        print("---> sendmail from<%s>, to <%s>" % (fromaddr, toaddr))
        self._server.sendmail(fromaddr, toaddr, message)

    def terminateService(self):
        print("---> quit")
        self._server.quit()


