from datetime import datetime

from config import CIDR_MAX_SUBNETS


class IPRange(object):
    def __init__(self, data):
        self.range_start = data[0]
        self.range_end = data[1]
        self.total_ips = int(data[2])
        self.assign_date = datetime.strptime(data[3], '%d/%m/%y')
        self.owner = data[4]

        self.cidr = IPRange.get_cidr(self.range_start, self.total_ips)

    @staticmethod
    def get_cidr(range_start, total_ips):
        mask = CIDR_MAX_SUBNETS.get(total_ips, None)

        if not mask:
            return None

        return '{}/{}'.format(range_start, CIDR_MAX_SUBNETS[total_ips])

    def __str__(self):
        return '{}'.format(self.cidr or self.range_start)
