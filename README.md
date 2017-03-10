# IPs by country
This project aims to provide a suite of scripts to retrieve ips by country.  
When available you can also get IPs used by a specific ISP.

## [Browse countries](countries/)

## Usage
- Get all IPs from France: `python query.py --country fr`
- Get all IPs from Online in France: `python query.py --country fr --search online`

## Install environment and fetch the data (optional)
The code has been tested with Python 3 and it depends on Scrapy. It is not a necessary step: all the stuff is already committed.

```bash
mkvirtualenv --python=$(which python3) ips-by-country
pip install -r requirements.txt
```

Now, you can get fresh data by running Scrapy.

1. The first script fetches IPs in the CSV format ([`raw` directory](raw/)).
2. The second one generates a binary [`ips-by-country.p`](data/)) with all the data.
3. It builds the markdown pages for each country ([`countries` directory](countries/)). 

```bash
scrapy runspider --nolog ip_spider.py
python parse.py
```
