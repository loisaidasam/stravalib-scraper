import cookielib
import time
import urllib
import urllib2

from BeautifulSoup import BeautifulSoup

from credentials import *

TIME_BT_REQUESTS = 2

def main():
	print "Logging in..."
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

	f = opener.open('https://www.strava.com/login')
	soup = BeautifulSoup(f.read())

	time.sleep(TIME_BT_REQUESTS)

	utf8 = soup.findAll('input', {'name': 'utf8'})[0].get('value').encode('utf-8')
	token = soup.findAll('input', {'name': 'authenticity_token'})[0].get('value')

	values = {
		'utf8': utf8,
		'authenticity_token': token,
		'email': EMAIL,
		'password': PASSWORD,
	}
	data = urllib.urlencode(values)
	url = 'https://www.strava.com/session'
	response = opener.open(url, data)
	soup = BeautifulSoup(response.read())

	print "Logged in, let's see what's good..."

	time.sleep(TIME_BT_REQUESTS)

	f = opener.open('http://app.strava.com/challenges/rapha-rising-circle-of-death/')
	soup = BeautifulSoup(f.read())

	print soup

main()
