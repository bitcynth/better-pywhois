import re
from .protocol import whois_raw

# Regex to extract the referred whois server
IANA_WHOIS_REFER_REGEX = re.compile('whois:[\s]+([\.a-z0-9\-]+)')

def recursive_query(query, root='whois.iana.org'):
    root_res = whois_raw(root, query)
    matches = IANA_WHOIS_REFER_REGEX.findall(root_res)
    if len(matches) < 1:
        return root_res
    return whois_raw(matches[0], query)