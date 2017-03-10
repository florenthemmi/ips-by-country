import argparse
import os
import pickle
import re

from config import PICKLE_DIRECTORY, PICKLE_FILENAME

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='IPs by country')
    parser.add_argument('--country', dest='country', action='store', required=True)
    parser.add_argument('--search', dest='search', action='store')

    args = parser.parse_args()
    ips_by_country = pickle.load(open(os.path.join(PICKLE_DIRECTORY, PICKLE_FILENAME), 'rb'))

    for ip in ips_by_country.get(args.country.upper(), []):
        if args.search:
            if re.match(args.search, ip.owner, flags=re.IGNORECASE):
                print(ip)
        else:
            print(ip)
