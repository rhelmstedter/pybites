from collections import defaultdict
import os
from pathlib import Path
from urllib.request import urlretrieve
import xml.etree.ElementTree as ET

# import the countries xml file
tmp = Path(os.getenv("TMP", "/tmp"))
countries = tmp / 'countries.xml'

if not countries.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/countries.xml',
        countries
    )


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    country_dict = defaultdict(list)
    countries_data = ET.parse(countries).getroot()
    for country in countries_data:
        country_dict[country[4].text].append(country[1].text)
    return country_dict


if __name__ == "__main__":
    data = get_income_distribution()
    print(data)
