'''
Created on Jan 12, 2021

@author: jct
'''

import logging
import imaplib

def info(str_):
    print("IMAP: " + str_)
    logging.info("IMAP: " + str_)

def error(str_):
    print("IMAP: " + str_)
    logging.error("IMAP: " + str_)

def debug(str_):
    logging.debug("IMAP: " + str_)

class IMAPInterface:
    def __init__(self):
        debug("Initializing")
        self._server = None
        
    def getServer(self):
        return self._server

    def readyService(self, service, creds):
        '''
        Get the IMAP service ready to use. Connect to the IMAP server
        specified using service with the authentication credentials
        specified in creds.

        '''

        # Get the hostname and port number from the service dictionary. 

        _server_addr = service["server_addr"]
        _port = service["port"]

        # Debug
        info("Connecting to %s:%d" %(_server_addr, _port))
        # print("Connecting IMAP <%s:%d>" %(_server_addr, _port))
        print("Using SMTP user = <%s>, password = <%s>" % (creds.username, creds.password))

        # Connect to the server.
        debug("---> connect")
        self._server = imaplib.IMAP4_SSL(host = _server_addr, port = _port)

        # And log in with the provided credentials.
        debug("---> login")
        #rval = self._server.login(creds.username, creds.password)
        self._server.login(creds.username, creds.password)

    def terminateService(self):
        '''Log out and disconnect from the IMAP server. '''
        debug("---> logout")
        self._server.logout()

    def getTemplate(self, template_name):
        '''
        Get the template specified by template_name from the IMAP
        server, where template_name is one of:
            welcome-sysml
            welcome-sysml-html
            welcome-mbse
            welcome-mbse-html
        These names may change without notice.
        '''

        # At the end of this function, we return en_message; set it to
        # None for those cases where a suitable template could not be
        # identified.
        message = None

        # Select the IMAP folder named python-templates
        self._server.select('python-templates')

        # Try to get the template. Unrecognized template names will
        # cause an exception which we must catch.
        try:
            # Map from template names to tag-like strings
            tagdict = { 
                        "welcome-sysml-html": "${tag:welcome-sysml-html}",
                        "welcome-sysml": "${tag:welcome-sysml}",
                        "welcome-mbse": "${tag:welcome-mbse}",
                       }

            # Get the string to search for.
            search_string = tagdict[template_name]

            debug("Search string is <%s>" % search_string)

            # Call the IMAP server to try to find a en_message with the
            # search tag as its subject.
            _typ, data = self._server.search(None, 'SUBJECT', search_string)

            # Check the number of templates found. If it's not exactly
            # one, report an error and return None.
            templates = data[0].split()

            if len(templates) < 1:
                info("*** Error: template not found, aborting")
                message = None

            elif len(templates) > 1:
                info("*** Error: too many templates found, aborting")
                message = None
                
            else:
                info("SUCCESS! Found the <%s> template" % template_name)

                info("Fetching template body")

                # TO-DO: Figure out what errors can reasonably occur
                # here and how to catch them.
                _typ, data = self._server.fetch(templates[0], '(RFC822)')

                # Get the en_message from the return data
                message = data[0][1]

                # The IMAP interface returns an array of bytes. Convert it to a string.
                message = message.decode('UTF-8')
    
        except KeyError:
            # Catch the axception if the tag name was unknown.
            info("*** Error: template tag <%s> not found." % template_name)
            message = None

        # Return the message found, or None if wasn't found.
        return message
        
