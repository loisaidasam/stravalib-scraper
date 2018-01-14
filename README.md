stravalib-scraper
=========

Library for web-scraping Strava data.

Note: Strava does have a [developer portal](https://developers.strava.com/) complete with a proper API and examples. This web-scraping based library was initially written years ago, before that API officially came about.

In no way does the author of this library advocate using it, particularly in any way that is abusive or in conflict with Strava's terms or developer guidelines. Proceed at your own risk!

Installation:
-------------

```
$ pip install -r requirements.txt
```

Command line interface:
-----------------------

To simply login and get the HTML from the dashboard, use the scraper from the command line:

```
$ ./scraper.py "your.email@example.com" "your-password"
```

If there's a specific page you'd like to get info from, say the [Rapha Rising challenge from 2012](https://www.strava.com/challenges/rapha-rising-circle-of-death), pass that URL as the final argument:

```
$ ./scraper.py "your.email@example.com" "your-password" "https://www.strava.com/challenges/rapha-rising-circle-of-death"
```

Python interface:
-----------------

To use the scraper from your own python code, you could do something like this:

```python
from scraper import StravaScraper

email = "your.email@example.com"
password = "your-password"
scraper = StravaScraper(email, password)
scraper.login()
dashboard_html = scraper.dashboard_content
url = "https://www.strava.com/challenges/rapha-rising-circle-of-death"
response = scraper.get_page(url)
rapha_html = response.content
```
