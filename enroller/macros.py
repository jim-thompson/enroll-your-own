'''
Created on Jan 12, 2021

@author: jct
'''

import re

prog = re.compile(b"\${([a-zA-Z0-9:_-]+)}")

def macro_substitute(text, m, fill_text):
    """
    Substitute the string match in regex match m with fill_text within text.
    """

    # Get the start and end indexes of the regex match.
    start_index = m.start(0)
    end_index = m.end(0)

    # Get the text that precedes the match and the text that follows
    # the match. 
    start_text = text[0:start_index]
    end_text = text[end_index:]

    # The result is the concatenation of the start text, the fill
    # text, and the end text. Return the concatenation.
    return start_text + fill_text + end_text
    
def get_macro_expansion(_dict, name):
    """Return _dict[name] or "" if name not in _dict."""
    try:
        return _dict[name]
    except:
        return b""

def macro_fill(text, _dict):
    """
    Find macros in text and use the key-value pairs to substitute
    macros with their text. A macro within text looks like ${name},
    and the entire macro is replaced with _dict["name"]. Note that text
    and _dict should all be defined as byte-strings (because that's how
    they're return from imaplib.
    """

    # Find the first macro
    match = prog.search(text)

    # Loop through every macro we find.
    while match is not None:

        # Extract the macro name from the match. The name is the
        # substring defined by group 1 of the regex.
        macro_name = match.group(1)

        # Macros that look like ${tag:some-text} are replaced by the
        # empty string. They exist just for keyword matching and must
        # always be removed entirely.
        if (macro_name[0:4] == b"tag:"):

            # Substitute the macro with an empty string
            text = macro_substitute(text, match, b"")
        else:
            # Look up the macro name in the dictionary to get the text
            # to replace it with.
            fill_text = get_macro_expansion(_dict, macro_name)

            # And do the replacement
            text = macro_substitute(text, match, fill_text)

        # Find the next match
        match = prog.search(text)

    # Finally, return the macro-substituted text.
    return text

