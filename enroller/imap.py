'''
Created on Jan 12, 2021

@author: jct
'''

import imaplib

class IMAPInterface:
    def __init__(self):
        print("Init IMAP interface")
        self._server = None

    def readyService(self, service, creds):

        _server_addr = service["server_addr"]
        _port = service["port"]

        print("Connecting IMAP <%s:%d>" %(_server_addr, _port))
        print("Using SMTP user = <%s>, password = <%s>" % (creds.username, creds.password))

        print("---> connect")
        self._server = imaplib.IMAP4_SSL(host = _server_addr, port = _port)

        print("---> login")
        rval = self._server.login(creds.username, creds.password)
        print(rval)

    def terminateService(self):
        print("---> logout")
        self._server.logout()

    def getTemplate(self, template_name):

        message = None
        self._server.select('python-templates')

        try:
            tagdict = { 
                        "welcome-sysml-html": "${tag:welcome-sysml-html}",
                        "welcome-sysml": "${tag:welcome-sysml}",
                        "welcome-mbse": "${tag:welcome-mbse}",
                       }

            search_string = tagdict[template_name]

            print("Search string is <%s>" % search_string)

            _typ, data = self._server.search(None, 'SUBJECT', search_string)

            templates = data[0].split()

            # Check the number of templates found. If it's not exactly
            # one, report an error and return None.
            if len(templates) < 1:
                print("***Error: template not found, aborting")
                message = None

            elif len(templates) > 1:
                print("***Error: too many templates found, aborting")
                message = None
                
            else:
                print("SUCCESS! Found the <%s> template" % template_name)

                print("Fetching template body")

                # TO-DO: Figure out what errors can reasonably occur
                # here and how to catch them.
                _typ, data = self._server.fetch(templates[0], '(RFC822)')

                # Get the message from the return data
                message = data[0][1]

        except KeyError:
            print("*** Error: template tag <%s> not found." % template_name)
            message = None
        
        return message
        