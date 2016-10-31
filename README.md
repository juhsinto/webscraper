# Data Scraper using BS4 and Mechanize


I wrote this script to extract fields from a portal that had several table sections, the data was to be extracted and presented in a csv file.
You can use this code to create your own data scraper, this code should demonstrate the possiblities that a data scraper is capable of.

### How it works:
- So I basically find the main table within the page, sanitize the html (remove unnecessary whitespace and newlines (including CR's & `<br>`'s)
- Then I find all the sub-tables (rows), and iterate through each of them, and extract the required data.

### Instructions:

- If you require to login into a portal, use the Mechanize component, else comment it out. Obviously replace the username, password, and URL fields.
- Customize the procedure to your requirement

### How to Run:

```sh
$ cd scraper
$ python web-scraper.py > output.csv
```

