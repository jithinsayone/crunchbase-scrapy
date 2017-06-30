import requests, json, time
from lxml import html
from random import randint

list_headers = {
    'Host': 'www.crunchbase.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-Distil-Ajax': 'qqacxsyf',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/json;charset=utf-8',
    'X-XSRF-TOKEN': 'TdOe7Noub3KOCiYuL7hk37kymg30mKyPYVPEDSKc7r/Slckp1OIxWG/qN7Q4kp/AMZNrvphAE/jlbttBXTcn+A==',
    'Referer': 'https://www.crunchbase.com/app/search/companies',
    'Content-Length': '190',
    'Cookie': 'jaco_referer=; _hp2_props.973801186=%7B%22Logged%20In%22%3Atrue%2C%22Pro%22%3Atrue%7D; _hp2_id.973801186=%7B%22userId%22%3A8040550905367091%2C%22pageviewId%22%3A%224541330234875094%22%2C%22sessionId%22%3A%222221887375419927%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%223.0%22%7D; hblid=Kl2HfwZtD5fVFQSZ3F6pZ0J3NeL1BL1B; olfsk=olfsk24881608995815918; jaco_uid=c473cdfc-cab6-472d-8262-64ef39d8bbcd; _ga=GA1.2.643587490.1489665169; D_SID=103.194.69.3:HjjJN5tlVDsjHv9vFYjVCK8nmfC2uwvyWU/Nraiivxw; D_PID=93308F68-50BF-3C57-8385-0DE082BCCE5A; D_IID=029086AF-9784-34B3-91B7-73504D9121ED; D_UID=A082F39B-570F-348A-8A69-3E8414255654; D_HID=Il8jrfz/tKDOYE4GZFms3eSQ1FP+57Sj7eScuqBiIDw; D_ZID=5E9E2C3F-1552-36F5-B468-F900E33F481F; D_ZUID=5774F646-F442-38F2-A1B9-AFC63F664E2C; AMCV_6B25357E519160E40A490D44%40AdobeOrg=1256414278%7CMCMID%7C65410408573198511432652961885854227543%7CMCAID%7CNONE%7CMCAAMLH-1490329452%7C3%7CMCAAMB-1490329452%7Chmk_Lq6TPIBMW925SPhw3Q; __uvt=; s_pers=%20s_getnr%3D1489998493066-Repeat%7C1553070493066%3B%20s_nrgvo%3DRepeat%7C1553070493068%3B; __qca=P0-1594147612-1489724653594; _pxvid=9eaafe00-0ac9-11e7-b6a1-719c0d4588a2; uvts=5mXTZsbD0V48SBWg; multivariate_bot=false; mf_user=79ae9929aa1e889bdff9e435f07aa599|; jaco_pid=demoangad4%40gmail.com; s_cc=true; s_sq=%5B%5BB%5D%5D; wcsid=sKXYl2SFkgsxzHXf3F6pZ0J3NeL1BL1B; _oklv=1490000269909%2CsKXYl2SFkgsxzHXf3F6pZ0J3NeL1BL1B; _okdetect=%7B%22token%22%3A%2214899862585250%22%2C%22proto%22%3A%22https%3A%22%2C%22host%22%3A%22www.crunchbase.com%22%7D; _okbk=cd4%3Dtrue%2Cvi5%3D0%2Cvi4%3D1489986260243%2Cvi3%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd5%3Daway%2Ccd3%3Dfalse%2Ccd2%3D0%2Ccd1%3D0%2C; _ok=1554-355-10-6773; request_method=POST; _px=eyJ0IjoxNDkwMDAwNTY1MTkyLCJzIjp7ImEiOjAsImIiOjB9LCJoIjoiY2Y5NTA5MzRmYzZlYjNjZGRlNzYxYTU2NjMzYjE5YTIzNTk1ZmZlOTkwOTUwNWNlMmZjZjRkZTE0ODc1MWIzZSJ9; XSRF-TOKEN=TdOe7Noub3KOCiYuL7hk37kymg30mKyPYVPEDSKc7r%2FSlckp1OIxWG%2FqN7Q4kp%2FAMZNrvphAE%2FjlbttBXTcn%2BA%3D%3D; remember_user_token=W1s2OTI5MjBdLG51bGwsIjE0OTAwMDAyNjEuNTc4NjA2Il0%3D--d866327ed0c1262756c4edc7cdce003beb79ec88; _site_session=e28cfc1ea1843667288823acdef51e75; _gat_UA-60854465-1=1; _hp2_ses_props.973801186=%7B%22r%22%3A%22https%3A%2F%2Fwww.crunchbase.com%2Fapp%2Flogin%3Fredirect_to%3D%252Fapp%252Fsearch%252Fcompanies%22%2C%22ts%22%3A1490000269442%2C%22d%22%3A%22www.crunchbase.com%22%2C%22h%22%3A%22%2Fapp%2Fsearch%2Fcompanies%22%7D',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}

detail_header = {
    'Host': 'www.crunchbase.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': 'multivariate_bot=false; multivariate_bot=false; jaco_referer=; _hp2_props.973801186=%7B%22Logged%20In%22%3A%22false%22%2C%22Pro%22%3Afalse%7D; _hp2_id.973801186=%7B%22userId%22%3Anull%2C%22pageviewId%22%3A%226060605039357865%22%2C%22sessionId%22%3A%227354899075777982%22%2C%22identity%22%3A%22jithinjohnson11%40gmail.com%22%2C%22trackerVersion%22%3A%223.0%22%7D; hblid=Kl2HfwZtD5fVFQSZ3F6pZ0J3NeL1BL1B; olfsk=olfsk24881608995815918; jaco_uid=32c9fac4-81b7-4f84-a226-ea2797363d07; _ga=GA1.2.643587490.1489665169; D_SID=103.194.69.3:HjjJN5tlVDsjHv9vFYjVCK8nmfC2uwvyWU/Nraiivxw; D_PID=93308F68-50BF-3C57-8385-0DE082BCCE5A; D_IID=C43D5798-98E0-33B4-956C-34C9B9EB7AC4; D_UID=0C6821F2-4248-3C7D-8E0C-160FCE5237E7; D_HID=REXjUufvLPMNHM1xsCMbeYzEaZ7ICtDaMNvxH2CORzY; D_ZID=5E9E2C3F-1552-36F5-B468-F900E33F481F; D_ZUID=5774F646-F442-38F2-A1B9-AFC63F664E2C; wcsid=BpRG9Rg3DTezmCKK3F6pZ0J3NeL1BL1B; _oklv=1489754141543%2CBpRG9Rg3DTezmCKK3F6pZ0J3NeL1BL1B; _okdetect=%7B%22token%22%3A%2214897244960560%22%2C%22proto%22%3A%22https%3A%22%2C%22host%22%3A%22www.crunchbase.com%22%7D; _okbk=cd4%3Dtrue%2Cvi5%3D0%2Cvi4%3D1489724496732%2Cvi3%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd5%3Daway%2Ccd3%3Dfalse%2Ccd2%3D0%2Ccd1%3D0%2C; _ok=1554-355-10-6773; AMCV_6B25357E519160E40A490D44%40AdobeOrg=1256414278%7CMCMID%7C65410408573198511432652961885854227543%7CMCAID%7CNONE%7CMCAAMLH-1490329452%7C3%7CMCAAMB-1490329452%7Chmk_Lq6TPIBMW925SPhw3Q; __uvt=; s_pers=%20s_getnr%3D1489754041819-Repeat%7C1552826041819%3B%20s_nrgvo%3DRepeat%7C1552826041821%3B; s_cc=true; __qca=P0-1594147612-1489724653594; s_sq=%5B%5BB%5D%5D; _pxvid=9eaafe00-0ac9-11e7-b6a1-719c0d4588a2; uvts=5mXTZsbD0V48SBWg; multivariate_bot=false; mf_user=79ae9929aa1e889bdff9e435f07aa599|; mf_a9bdf657-9a0c-4b9f-9dd9-a03b3f6cea4a=b139e8b028636e6d26dbe2fd18f6596b|0317324959d20d134304ce085f5e9b4be9b31eec|1489744656688||2|||0; user_intent_path=%2Flogin; user_origin_path=%2F; XSRF-TOKEN=5GPpLR%2FtN0tfiIBR15ZLLdE99OHa%2F53NIdG8sdT5UW83bjfwe1TN%2BMRVFLZHiU8GGt2vNlNTSFYtvaB1TdKz8w%3D%3D; _site_session=aef2dc24071a6be3efe5731800caa320; request_method=POST; _hp2_ses_props.973801186=%7B%22ts%22%3A1489752965363%2C%22d%22%3A%22www.crunchbase.com%22%2C%22h%22%3A%22%2Fapp%2Fsearch%2Fcompanies%22%7D; jaco_pid=jithinjohnson11%40gmail.com; _px=eyJ0IjoxNDg5NzU0MzU0MTEzLCJzIjp7ImEiOjAsImIiOjB9LCJoIjoiZjVhNGZiNWM2MDY5NWQwNzY2OGU0ZTY0ZjMwZmU2M2ZkNzEwMjRlNjRhYTJmYWYwZDk5M2E0OTdhODQwZjVhNiJ9',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}
count = 1
while True:
    try:
        d = {"field_ids": ["identifier", "category_groups","status","last_funding_investment_type", "headquarters_identifiers", "short_description", "rank",
                           "website",
                           "twitter", "facebook", "linkedin", "contact_email", "phone_number"],
             "order": [{"field_id": "rank", "sort": "asc"}],
             "query": [{"type": "predicate", "field_id": "rank", "operator_id": "gte", "values": [count]}],
             "field_aggregators": [], "limit": 2000}
        list_data = requests.post('https://www.crunchbase.com/v4/data/companies/search', data=json.dumps(d),
                                  headers=list_headers)
        #] print list_data.text
        list_json_data = json.loads(list_data.text)
        list_json_data = list_json_data["entities"]

        for entry in list_json_data:
            # print entry

            name = entry["properties"]["identifier"]["value"]
            description = entry["properties"]["short_description"]
            rank = entry["properties"]["rank"]
            try:
                category = ''
                for temp in entry["properties"]["category_groups"]:
                    category=category+temp["value"]+","
            except:
                category = None
            try:
                location = ''
                for temp in entry["properties"]["headquarters_identifiers"]:
                    location=location+temp["value"]+","
            except:
                location = None
            try:
                twitter = entry["properties"]["twitter"]["value"]
            except:
                twitter = None
            try:
                facebook = entry["properties"]["facebook"]["value"]
            except:
                facebook = None
            try:
                website = entry["properties"]["website"]["value"]
            except:
                website = None
            try:
                linkdin = entry["properties"]["linkedin"]["value"]
            except:
                linkdin = None
            try:
                ph_num = entry["properties"]["phone_number"]
            except:
                ph_num = None
            try:
                email = entry["properties"]["contact_email"]
            except:
                email = None
            try:
                funding_type=entry["properties"]["last_funding_investment_type"]
            except:
                funding_type=None
            try:
                status=entry["properties"]["status"]
            except:
                status=None


            # print "NAME:", name
            # print"DESCRIPTION:", description
            # print"RANK:", rank
            # print"CATEGORY:", category
            # print"LOCATION:", location
            # print"WEBSITE:", website
            # print "FACEBOOK:", facebook
            # print "TWITTER:", twitter
            # print"LINKDIN:", linkdin
            # print"PHONE:", ph_num
            # print "EMAIL:", email
            final_data = {"name": name, "description": description, "rank": rank, "category": category,
                          "location": location, "website": website, "facebook": facebook, "twitter": twitter,
                          "linkdin": linkdin, "phone": ph_num, "email": email,"status":status,"last-funding-type":funding_type}
            # print final_data
            try:
             save=requests.post('http://138.68.238.208/api/v1/save-company/',data=json.dumps(final_data),headers={'Authorization':'Token 124fe5f2ea8fc82018832567a7465ed6ea941577','Content-type': 'application/json'})
             result_data=json.loads(save.text)
             print result_data["data_status"], name
            except:
             print"Error while saving.."
            #print save.text
        wait_time = randint(120, 360)
        time.sleep(randint(120, wait_time))
        count = count + 2000
        print"NEXT..."
    except:
        print"ERROR IN RESPONSE...."
        break







