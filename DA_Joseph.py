
# --Part 1 - Performing a GET request on the webpage--

# Use the Request library
import requests
# Set the target webpage
url = "http://172.18.58.80/nantes/"
r = requests.get(url)
# This will get the full page
print(r.text)

# --Part 2 -- Obtaining status code of the webpage to check whether the performed GET request was successful``

print("Status code:")
print("\t *", r.status_code)

# --Part 3 - Displaying website header--

# This will just get just the headers
h = requests.head(url)
print("Header:")
print("**********")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")

# --Part 4 - Modification of Header User-Agent--

# This will modify the headers user-agent
headers = {
    'User-Agent' : 'Mobile'
}
#Testing the modified headers on an external website
url2 = 'http://172.18.58.80/headers.php'
rh = requests.get(url2, headers=headers)
print(rh.text)

# --Part 5 - Importing Scrapy web-crawler for web-crawling the webpage--

import scrapy
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://172.18.58.80/nantes']

# Used the appropriate parser "response.css"
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }
            #Recursively extracting JPG images
            Page_selector = '.next a ::attr(href)'
            next_page = response.css(Page_selector).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )











