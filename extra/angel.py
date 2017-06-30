import cookielib
import os, json
import urllib2
import time
from lxml import html
import requests

from fake_useragent import UserAgent

ua = UserAgent()

try:
    os.remove("parser_list.cookies.txt")
    os.remove("parser_detail.cookies.txt")
except:
    pass

from lxml import etree


class AngelInParser():
    def __init__(self, flag=''):
        """ Start up... """

        if flag == 1:
            cookie_filename = "parser_list.cookies.txt"
        else:
            cookie_filename = "parser_detail.cookies.txt"

        # Simulate browser with cookies enabled

        self.cj = cookielib.MozillaCookieJar(cookie_filename)
        if os.access(cookie_filename, os.F_OK):
            self.cj.load()
        self.opener = urllib2.build_opener(
            urllib2.HTTPRedirectHandler(),
            urllib2.HTTPHandler(debuglevel=0),
            urllib2.HTTPSHandler(debuglevel=0),
            urllib2.HTTPCookieProcessor(self.cj)
        )
        if flag == 1:
            self.opener.addheaders = [
                ('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; '
                                'Windows NT 5.2; .NET CLR 1.1.4322)'))
            ]
        else:
            self.opener.addheaders = [
                ('User-agent', (str(ua.random)))
            ]

        # Login
        # self.loginPage(self.url,flag)



        self.cj.save()


    def loadPage(self, url):
        """
        Utility function to load HTML from URLs for us with hack to continue despite 404
        """
        # We'll print the url in case of infinite loop
        # print "Loading URL: %s" % url
        try:

            response = self.opener.open(url)

            return ''.join(response.readlines())
        except:
            # If URL doesn't load for ANY reason, try again...
            # Quick and dirty solution for 404 returns because of network problems
            # However, this could infinite loop if there's an actual problem
            pass

    def loginPage(self, url, flag):
        """
        Handle login. This should populate our cookie jar.
        """
        html = self.loadPage(url)
        if flag != 1:
            return html
            # print "DATA:",html


parser = AngelInParser(1)
data = parser.loginPage("https://angel.co/companies", 1)
print "LOAD COOKIE:"
final_data = []
cj = cookielib.MozillaCookieJar('parser_list.cookies.txt')
cj.load()
header = {  # "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0",
            #"Accept": "*/*",
            #"Accept-Language": "en-US,en;q=0.5",
            #"Accept-Encoding": "gzip, deflate, br",
            #"X-CSRF-Token": "d/u8a8qRuiZEQa4TcoR3pX/3XN0JSHjktVa1C68FW6U=",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            #"Referer": "https://angel.co/companies",
            #"Content-Length": "11",
            #"Connection": "keep-alive"
}
angel_list = requests.Session()
angel_list.cookies = cj
count = 1
while True:
    try:
        d = {"sort": "signal", "page": count}
        r = angel_list.post(url='https://angel.co/company_filters/search_data', data=json.dumps(d), headers=header)
        time.sleep(5)
        post_data = json.loads(r.text)
        id_data = post_data["ids"]
        total_data = post_data["total"]
        page_data = post_data["page"]
        sort_data = post_data["sort"]
        new_data = post_data["new"]
        hexdigest_data = post_data["hexdigest"]

        get_url = "https://angel.co/companies/startups?"
        for entry in id_data:
            get_url = get_url + "ids[]=" + str(entry) + "&"

        get_url = get_url + "total=" + str(total_data) + "&page=" + str(page_data) + "&sort=" + str(
            sort_data) + "&new=" + str(new_data) + "&hexdigest=" + str(hexdigest_data)
        print"COUNT:", count
        # print"STATUS_POST:",r.status_code
        # print"URL:",get_url
        list_data = angel_list.get(url=get_url)
        temp_data = json.loads(str(list_data.text))
        doc = html.fromstring(temp_data["html"])
        name_list = doc.xpath("//div[contains(@class, 'name')]/a/text()")
        for i in range(0, len(name_list)):
            name=name_list[i].lower()
            print"NAME:", name_list[i].lower()
            try:
              save=requests.post('http://138.68.238.208/api/v1/angellist/',data=json.dumps({"name":name}),headers={'Authorization':'Token 124fe5f2ea8fc82018832567a7465ed6ea941577','Content-type': 'application/json'})
              result_data=json.loads(save.text)
              print result_data["data_status"], name
            except:
              print"Error while saving.."


        count = count + 1
        time.sleep(5)
    except:
        print"LOOP COMPLETED"
        break



