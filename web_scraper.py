from __future__ import print_function
import urllib2
import cookielib
import urllib
import requests
import mechanize
from mechanize._opener import urlopen
from mechanize._form import ParseResponse
from bs4 import BeautifulSoup
import bs4, sys, re, sys

USERNAME = ###SENSITIVE
PASSWORD = ###SENSITIVE
URL      = ###SENSITIVE 



browser = mechanize.Browser()
browser.open(URL)
browser.select_form(nr = 0)
browser.form['uid'] = USERNAME
browser.form['pwd'] = PASSWORD
browser.submit()

# initial page
i = 0

while i <= 480:
	browser.open(""" SENSITIVE """ + str(i))

	soup = BeautifulSoup(browser.response().read(), "html.parser")

	# get the main table within the page that we're interested in
	table = soup.find('table', width="500")

	# stringify the table to replace newlines and carriage-returns
	text = str(table)
	text = text.replace('\n', ' ').replace('\r', '')

	# remove break tags
	soup = bs4.BeautifulSoup(re.sub('(<br>)|(</br>)', '', text), "html.parser")

	# find individual rows within the table
	tables = soup.findAll('table', class_="hamper")

	for table in tables:
		# address
		innerTables = table.findAll('td')
		address = innerTables[1].getText()
		address = re.sub('[,]', '', address)
		print (address, end=",")

		# find all html content that are of tag type "th" and have attribute 'height' of value '16'
		th_es = table.findAll('th', {'height': 16})


		for th in th_es:
			names = th.findChildren()
			for name in names:
				cName = name.getText()
				
				# print name & phone number only if string is not empty
				if (len(cName) > 0):
					# print string if ends with digit
					if (cName[-1].isdigit()):
						parts = re.split('(\d.*)',cName)
						print(parts[0], end=",")
						print(parts[1], end=",")

			# for the email addresses
			email = th.contents[0]

			# strip all whitespace, tab, newline, CR
			email = email.strip(' \t\n\r')

			# print email only if string is not empty
			if (len(email) > 0):
				print(email, end="\n")

	print ("done with page " + str((++i/20)+1))
	# change pointer to next page
	i = i + 20






