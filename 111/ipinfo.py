import requests

IPINFO_URL = 'http://ipinfo.io/{}/json'


def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    r = requests.get(IPINFO_URL.format(ip_address))
    return r.json()['country']


if __name__ == "__main__":
    print(get_ip_country('187.190.38.36'))
