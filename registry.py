import re
import urllib.request

def fetch_available_versions(limit=10):
    url = "https://www.python.org/ftp/python/"
    html = urllib.request.urlopen(url).read().decode()
    versions = re.findall(r'href="([0-9]+\.[0-9]+\.[0-9]+)/"', html)
    versions = sorted(set(versions), reverse=True)
    return versions[:limit]