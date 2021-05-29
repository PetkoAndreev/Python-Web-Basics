'''
You will receive encoded URL. Decode the URL and validate it. If the URL is valid, print on the console the parts of the URL in the format:
"Protocol: {protocol}"
"Host: {host}"
"Port: {port}"
"Path: {path}"
"Query: {query string}" (if any)
"Fragment: {fragment}" (if any)
If the URL is invalid, print "Invalid URL".
A valid URL has the following parts:
Protocol	Required
Host	Required
Port	Required (default value for http - 80, for https - 443)
Path	Required (default value: /)
Query Strings	Optional (multiple query strings are separated by &)
Fragment	Optional
'''
from urllib import parse

urls = [
    'http://softuni.bg/',
    'https://softuni.bg:447/search?Query=pesho&Users=true#go',
    'http://google:443/',
    'https://mysite:80/demo/index.aspx',
    'somesite.com:80/search?',
    'https/mysite.bg?id=2',
]


def get_protocol(scheme):
    if scheme in ('http', 'https'):
        return scheme
    return None


def get_host_and_port(netloc, scheme):
    if '.' not in netloc:
        return None, None
    if ':' in netloc:
        return netloc.split(':')
    return netloc, 80 if scheme == 'http' else 443


def get_path(path):
    return path or '/'


def get_query(query):
    return query


def get_fragment(fragment):
    return fragment


def validate_url(url):
    url_components = parse.urlparse(url)
    protocol = get_protocol(url_components.scheme)
    host, port = get_host_and_port(url_components.netloc, url_components.scheme)
    path = get_path(url_components.path)
    query = get_query(url_components.query)
    fragment = get_fragment(url_components.fragment)
    if None in (protocol, host, port, path):
        return 'Invalid URL'
    return f'''-----------
URL: {url}
Coponents: {url_components}
Protocol: {protocol}
Host: {host}
Port: {port}
Path: {path}
Query: {query}
Fragment: {fragment}'''


for url in urls:
    print(validate_url(url))
