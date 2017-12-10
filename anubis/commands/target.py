"""The target command."""

from json import dumps

import requests

from .base import Base


class Target(Base):
	"""Main enumeration module"""
	domains = []

	def run(self):
		self.subdomain_hackertarget()
		print('You supplied the following options:',
		      dumps(self.options, indent=2, sort_keys=True))

	def subdomain_hackertarget(self):
		headers = {'Upgrade-Insecure-Requests': '1',
		           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
		params = (('q', self.options["TARGET"]),)

		results = requests.get('http://api.hackertarget.com/hostsearch/',
		                       headers=headers, params=params)
		results = results.text.split('\n')
		for res in results:
			self.domains.append(res.split(","))

		print(dumps(self.domains, indent=2, sort_keys=True))
