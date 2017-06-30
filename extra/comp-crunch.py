import json, requests, time
from random import randint

header = {
    'Host': 'www.crunchbase.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-Distil-Ajax': 'ytaswfswyaqbxfzzudszv',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/json;charset=utf-8',
    'X-XSRF-TOKEN': 'TdOe7Noub3KOCiYuL7hk37kymg30mKyPYVPEDSKc7r/Slckp1OIxWG/qN7Q4kp/AMZNrvphAE/jlbttBXTcn+A==',
    'Cache-Control': 'max-age=0',
    'Referer': 'https://www.crunchbase.com/app/search/people/ff3b57651041031d5ee77ddc4047862830d0e07d',
    'Content-Length': '223',
    'Cookie': 'jaco_referer=; _hp2_props.973801186=%7B%22Logged%20In%22%3Atrue%2C%22Pro%22%3Atrue%7D; _hp2_id.973801186=%7B%22userId%22%3A8040550905367091%2C%22pageviewId%22%3A%228367358662206890%22%2C%22sessionId%22%3A%222221887375419927%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%223.0%22%7D; hblid=Kl2HfwZtD5fVFQSZ3F6pZ0J3NeL1BL1B; olfsk=olfsk24881608995815918; jaco_uid=c473cdfc-cab6-472d-8262-64ef39d8bbcd; _ga=GA1.2.643587490.1489665169; D_SID=103.194.69.3:HjjJN5tlVDsjHv9vFYjVCK8nmfC2uwvyWU/Nraiivxw; D_PID=93308F68-50BF-3C57-8385-0DE082BCCE5A; D_IID=C43D5798-98E0-33B4-956C-34C9B9EB7AC4; D_UID=0C6821F2-4248-3C7D-8E0C-160FCE5237E7; D_HID=REXjUufvLPMNHM1xsCMbeYzEaZ7ICtDaMNvxH2CORzY; D_ZID=5E9E2C3F-1552-36F5-B468-F900E33F481F; D_ZUID=5774F646-F442-38F2-A1B9-AFC63F664E2C; AMCV_6B25357E519160E40A490D44%40AdobeOrg=1256414278%7CMCMID%7C65410408573198511432652961885854227543%7CMCAID%7CNONE%7CMCAAMLH-1490329452%7C3%7CMCAAMB-1490329452%7Chmk_Lq6TPIBMW925SPhw3Q; __uvt=; s_pers=%20s_getnr%3D1490000667465-Repeat%7C1553072667465%3B%20s_nrgvo%3DRepeat%7C1553072667466%3B; __qca=P0-1594147612-1489724653594; _pxvid=9eaafe00-0ac9-11e7-b6a1-719c0d4588a2; uvts=5mXTZsbD0V48SBWg; multivariate_bot=false; mf_user=79ae9929aa1e889bdff9e435f07aa599|; jaco_pid=demoangad4%40gmail.com; s_cc=true; s_sq=%5B%5BB%5D%5D; wcsid=sKXYl2SFkgsxzHXf3F6pZ0J3NeL1BL1B; _oklv=1490002584510%2CsKXYl2SFkgsxzHXf3F6pZ0J3NeL1BL1B; _okdetect=%7B%22token%22%3A%2214899862585250%22%2C%22proto%22%3A%22https%3A%22%2C%22host%22%3A%22www.crunchbase.com%22%7D; _okbk=cd4%3Dtrue%2Cvi5%3D0%2Cvi4%3D1489986260243%2Cvi3%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd5%3Daway%2Ccd3%3Dfalse%2Ccd2%3D0%2Ccd1%3D0%2C; _ok=1554-355-10-6773; _px=eyJ0IjoxNDkwMDAyNzA0NjIxLCJzIjp7ImEiOjAsImIiOjB9LCJoIjoiZmQwOThkNWYzODM0NThhNGUxYzI3ZmYyY2I2YTExNzExNGZkYzM3MDk2ZTlhZDFhNTVkYmQ0YjFhYjIzMDU0ZCJ9; XSRF-TOKEN=TdOe7Noub3KOCiYuL7hk37kymg30mKyPYVPEDSKc7r%2FSlckp1OIxWG%2FqN7Q4kp%2FAMZNrvphAE%2FjlbttBXTcn%2BA%3D%3D; remember_user_token=W1s2OTI5MjBdLG51bGwsIjE0OTAwMDAyNjEuNTc4NjA2Il0%3D--d866327ed0c1262756c4edc7cdce003beb79ec88; _site_session=e28cfc1ea1843667288823acdef51e75; _hp2_ses_props.973801186=%7B%22r%22%3A%22https%3A%2F%2Fwww.crunchbase.com%2Fapp%2Flogin%3Fredirect_to%3D%252Fapp%252Fsearch%252Fcompanies%22%2C%22ts%22%3A1490000269442%2C%22d%22%3A%22www.crunchbase.com%22%2C%22h%22%3A%22%2Fapp%2Fsearch%2Fcompanies%22%7D; request_method=POST',
    'Connection': 'keep-alive',
}


def save_person(data):
    save = requests.post("http://0.0.0.0:8000/api/v1/save-people/", data=json.dumps(data))
    print"STATUS:", save.text


print"Requesting...."
count = 1
while True:
    print
    d = {
        "field_ids": ["identifier", "primary_job", "primary_company", "rank", "bio", "first_name", "last_name",
                      "gender",
                      "linkedin",
                      "twitter", "facebook", "location_identifiers"], "order": [{"field_id": "rank", "sort": "asc"}],
        "query": [{"type": "predicate", "field_id": "rank", "operator_id": "gte", "values": [count]}],
        "field_aggregators": [], "limit": 2000}
    r = requests.post('https://www.crunchbase.com/v4/data/people/search', data=json.dumps(d), headers=header)
    # print r.text
    try:
        print"PROCESSING..."
        data = json.loads(r.text)
        data = data["entities"]
        for entry in data:
            entry = entry["properties"]
            name = entry["identifier"]["value"]
            try:
                gender = entry["gender"]
            except:
                gender = None
            try:
                rank = entry["rank"]
            except:
                rank = None
            try:
                company = entry["primary_company"]["value"]
            except:
                company = None
            try:
                twitter = entry["twitter"]["value"]
            except:
                twitter = None
            try:
                facebook = entry["facebook"]["value"]
            except:
                facebook = None
            try:
                linkdin = entry["linkedin"]["value"]
            except:
                linkdin = None
            try:
                designation = entry["primary_job"]
            except:
                designation = None
            try:
                first_name = entry["first_name"]
            except:
                first_name = None
            try:
                last_name = entry["last_name"]
            except:
                last_name = None
            try:
                temp = entry["location_identifiers"]
                location = ''
                for i in temp:
                    location = location + i["value"] + ","
            except:
                location = None
            try:
                bio = entry["bio"]
            except:
                bio = None

            final_data = {"name": name, "gender": gender, "designation": designation, "first_name": first_name,
                          "last_name": last_name, "rank": rank, "twitter": twitter, "linkdin": linkdin,
                          "facebook": facebook,
                          "company": company, "location": location, "biography": bio}

            # print final_data
            try:
              save = requests.post('http://138.68.238.208/api/v1/save-people/', data=json.dumps(final_data),
                                 headers={'Authorization': 'Token 124fe5f2ea8fc82018832567a7465ed6ea941577',
                                          'Content-type': 'application/json'})
              result_data=json.loads(save.text)
              print result_data["data_status"], name
            except:
              print"Error While saving.."

        count = count + 2000
        print"NEXT:"
        wait_time = randint(300, 360)
        time.sleep(randint(300, wait_time))
        print"LOADING..."
    except:
        print"ERROR RESPONSE...."
        break















