import argparse
import csv
import operator
import os
import pickle
import time

from config import CIDR_MAX_SUBNETS, COUNTRIES, MARKDOWN_DIRECTORY, PICKLE_DIRECTORY, PICKLE_FILENAME, RAW_DIRECTORY
from utils import IPRange

def build_markdown(ips_by_country):
    sorted_countries = sorted({key: COUNTRIES[key] for key in ips_by_country.keys()}.items(), key=operator.itemgetter(1))

    with open(os.path.join(MARKDOWN_DIRECTORY, 'README.md'), 'w') as f:
        f.write('# Countries\n\n')

        for country in sorted_countries:
            f.write('[{}]({})  \n'.format(country[1], '{}.md'.format(country[0].lower())))

    for country_code, ips in ips_by_country.items():
        filename = '{}.md'.format(country_code.lower())

        with open(os.path.join(MARKDOWN_DIRECTORY, filename), 'w') as f:
            f.write('# {}\n\n'.format(COUNTRIES[country_code]))
            f.write('CIDR               | Range start     | Range end       | Total IPs  | Assign date | Owner\n')
            f.write('------------------ | --------------- | --------------- | ---------- | ----------- | -----\n')

            for ip in ips:
                f.write('{} | {} | {} | {} | {} | {}\n'.format(
                    (ip.cidr if ip.cidr else '').ljust(18),
                    ip.range_start.ljust(15),
                    ip.range_end.ljust(15),
                    str(ip.total_ips).ljust(10),
                    ip.assign_date.strftime('%Y-%m-%d').ljust(11),
                    ip.owner
                ))

def build_pickle(ips_by_country):
    pickle.dump(ips_by_country, open(os.path.join(PICKLE_DIRECTORY, PICKLE_FILENAME), 'wb'))

if __name__ == '__main__':
    ips_by_country = {}

    for _, _, files in os.walk(RAW_DIRECTORY):
        break

    for f in files:
        country_code = f.split('.')[0].upper()
        ips_by_country[country_code] = []

        with open(os.path.join(RAW_DIRECTORY, f)) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')

            for row in reader:
                if not len(row):
                    continue

                ips_by_country[country_code].append(IPRange(row))

    build_markdown(ips_by_country)
    build_pickle(ips_by_country)
