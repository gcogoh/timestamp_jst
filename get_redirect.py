#!/usr/bin/env python3
#
# curl -s --head http://url-file | grep Last-Modified
#
import requests
import sys
import os
import datetime
import time
import pytz

count = 0;
for url in sys.argv:
	if count > 0:
		print(url)
		filename = os.path.basename(url)
		print(filename)
		res = requests.head(url)
		if 'Last-Modified' in res.headers:
			print(res.headers['Last-Modified'])
		else:
			print(res.headers['Location'])
		#print(res.headers)
	count += 1
