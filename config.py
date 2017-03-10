import json
import os

CIDR_MAX_SUBNETS = {}
CONFIG_DIRECTORY = 'config'
COUNTRIES = json.load(open(os.path.join(CONFIG_DIRECTORY, 'countries.json'), 'r'))

cidr_max_subnets_dict = json.load(open(os.path.join(CONFIG_DIRECTORY, 'cidr_max_subnets.json'), 'r'))
config_dict = json.load(open(os.path.join(CONFIG_DIRECTORY, 'config.json'), 'r'))

for key, value in cidr_max_subnets_dict.items():
    CIDR_MAX_SUBNETS[int(key)] = value

for key, value in config_dict.items():
    globals()[key.upper()] = value
