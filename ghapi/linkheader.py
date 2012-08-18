# -*- coding: utf-8 -*-
import re

TOKEN = r'(?:[^\(\)<>@,;:\\"/\[\]\?={} \t]+?)'
QUOTED_STRING = r'(?:"(?:\\"|[^"])*")'
PARAMETER = r'(?:%(TOKEN)s(?:=(?:%(TOKEN)s|%(QUOTED_STRING)s))?)' % locals()
LINK = r'<[^>]*>\s*(?:;\s*%(PARAMETER)s?\s*)*' % locals()
COMMA = r'(?:\s*(?:,\s*)+)'
LINK_SPLIT = r'%s(?=%s|\s*$)' % (LINK, COMMA)

def _unquotestring(instr):
    if instr[0] == instr[-1] == '"':
        instr = instr[1:-1]
        instr = re.sub(r'\\(.)', r'\1', instr)
    return instr
def _splitstring(instr, item, split):
    if not instr:
        return []
    return [ h.strip() for h in re.findall(r'%s(?=%s|\s*$)' % (item, split), instr)]

link_splitter = re.compile(LINK_SPLIT)

def parse_link_value(instr):
    """
    Given a link-value (i.e., after separating the header-value on commas), 
    return a dictionary whose keys are link URLs and values are dictionaries
    of the parameters for their associated links.
    
    Note that internationalised parameters (e.g., title*) are 
    NOT percent-decoded.
    
    Also, only the last instance of a given parameter will be included.
    
    For example, 
    
    >>> parse_link_value('</foo>; rel="self"; title*=utf-8\'de\'letztes%20Kapitel')
    {'/foo': {'title*': "utf-8'de'letztes%20Kapitel", 'rel': 'self'}}
    
    """
    out = {}
    if not instr:
        return out
    for link in [h.strip() for h in link_splitter.findall(instr)]:
        url, params = link.split(">", 1)
        url = url[1:]
        param_dict = {}
        for param in _splitstring(params, PARAMETER, "\s*;\s*"):
            try:
                a, v = param.split("=", 1)
                param_dict[a.lower()] = _unquotestring(v)
            except ValueError:
                param_dict[param.lower()] = None
        out[url] = param_dict
    return out
