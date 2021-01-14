import json
import re


ath = "./campaigns_data.txt"
#camp_data = "./example.txt"

url = "https://app.leadflow360.net/api/login"
url2 = " https://app.leadflow360.net/api/getdashboarddata"
url3 = "https://app.leadflow360.net/api/data"
header = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36"
}

headers1 = {"Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "55",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "PHPSESSID=6088746151e390bf29d5e46f2056c692; G_ENABLED_IDPS=google",
            "Host": "app.leadflow360.net",
            "Origin": "https://app.leadflow360.net",
            "Pragma": "no-cache",
            "Referer": "https://app.leadflow360.net/login",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36"
}

headers2 = {"Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language":
                "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Cookie": "PHPSESSID=6088746151e390bf29d5e46f2056c692; G_ENABLED_IDPS=google",
            "Host": "app.leadflow360.net",
            "Pragma": "no-cache",
            "Referer": "https://app.leadflow360.net/dashboard",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"}

headers3 = {"Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "18",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "PHPSESSID=6088746151e390bf29d5e46f2056c692; G_ENABLED_IDPS=google",
            "Host": "app.leadflow360.net",
            "Origin": "https://app.leadflow360.net",
            "Pragma": "no-cache",
            "Referer": "https://app.leadflow360.net/campaigns",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"}


appminheaders = {   "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Cookie": "PHPSESSID=6088746151e390bf29d5e46f2056c692; G_ENABLED_IDPS=google",
                    "Host": "app.leadflow360.net",
                    "Pragma": "no-cache",
                    "Referer": "https://app.leadflow360.net/dashboard",
                    "Sec-Fetch-Dest": "script",
                    "Sec-Fetch-Mode": "no-cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36"}

appminurl = "https://app.leadflow360.net/tm/assets/js/app.min.js"

api_data_value = {"userCompaigns": "true"}

"""
{"userCampaigns":[{"id":"19352","name":"Dentist Johannesburg ","created_date":"2019-11-21 13:13:14","owner_id":"7460","leads":"34","leads_contacted":"21","leads_responded":"4"},{"id":"20409","name":"Dentist Cape Town (JM)","created_date":"2020-01-08 14:19:30","owner_id":"7460","leads":"14","leads_contacted":"13","leads_responded":"2"},{"id":"20427","name":"Dentist - Ireland Dublin (SM)","created_date":"2020-01-09 22:29:15","owner_id":"7460","leads":"16","leads_contacted":"12","leads_responded":"0"},{"id":"20436","name":"Dentist - UK ","created_date":"2020-01-09 22:45:49","owner_id":"7460","leads":"108","leads_contacted":"84","leads_responded":"9"},{"id":"20530","name":"Dentist - Maryland - USA ","created_date":"2020-01-17 15:21:45","owner_id":"7460","leads":"239","leads_contacted":"376","leads_responded":"17"},{"id":"20561","name":"Gym - Capetown","created_date":"2020-01-20 10:33:52","owner_id":"7460","leads":"21","leads_contacted":"16","leads_responded":"3"},{"id":"20562","name":"Gym - Durban ","created_date":"2020-01-20 10:37:03","owner_id":"7460","leads":"22","leads_contacted":"19","leads_responded":"14"},{"id":"20571","name":"Gym - Canada ","created_date":"2020-01-20 19:16:17","owner_id":"7460","leads":"271","leads_contacted":"218","leads_responded":"28"},{"id":"20648","name":"Car Dealerships Jhb (OTC)","created_date":"2020-01-26 23:16:52","owner_id":"7460","leads":"18","leads_contacted":"34","leads_responded":"0"},{"id":"20649","name":"Construction company CTC (OTC)","created_date":"2020-01-26 23:26:59","owner_id":"7460","leads":"21","leads_contacted":"54","leads_responded":"6"},{"id":"20650","name":"Embroidery Jhb (OTC)","created_date":"2020-01-26 23:33:04","owner_id":"7460","leads":"31","leads_contacted":"67","leads_responded":"21"},{"id":"20754","name":"Barbershop JHB (OTC)","created_date":"2020-02-02 12:26:58","owner_id":"7460","leads":"22","leads_contacted":"8","leads_responded":"5"},{"id":"20755","name":"Clothing store JHB (OTC)","created_date":"2020-02-02 12:38:11","owner_id":"7460","leads":"23","leads_contacted":"50","leads_responded":"30"},{"id":"21272","name":"Saloon JHB (OTC)","created_date":"2020-03-07 15:22:16","owner_id":"7460","leads":"52","leads_contacted":"5","leads_responded":"2"},{"id":"21676","name":"Saloon PTA (OTC)","created_date":"2020-03-29 06:40:13","owner_id":"7460","leads":"26","leads_contacted":"3","leads_responded":"0"},{"id":"21714","name":"Saloon JHB APR (OTC)","created_date":"2020-04-01 20:50:01","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"21797","name":"Finances Alberton (OTC)","created_date":"2020-04-06 22:07:35","owner_id":"7460","leads":"4","leads_contacted":"0","leads_responded":"0"},{"id":"21798","name":"finances Germiston (OTC)","created_date":"2020-04-06 22:13:33","owner_id":"7460","leads":"21","leads_contacted":"0","leads_responded":"0"},{"id":"21799","name":"finances JHB (OTC)","created_date":"2020-04-06 22:15:09","owner_id":"7460","leads":"10","leads_contacted":"0","leads_responded":"0"},{"id":"21800","name":"finances East Rand","created_date":"2020-04-06 22:18:26","owner_id":"7460","leads":"9","leads_contacted":"0","leads_responded":"0"},{"id":"21801","name":"finances Midrand (OTC)","created_date":"2020-04-06 22:22:20","owner_id":"7460","leads":"3","leads_contacted":"0","leads_responded":"0"},{"id":"21802","name":"finances benoni (OTC)","created_date":"2020-04-06 22:24:16","owner_id":"7460","leads":"23","leads_contacted":"0","leads_responded":"0"},{"id":"21803","name":"finances kempton park (OTC)","created_date":"2020-04-06 22:25:44","owner_id":"7460","leads":"20","leads_contacted":"0","leads_responded":"0"},{"id":"21804","name":"finances centurion (OTC)","created_date":"2020-04-06 22:26:48","owner_id":"7460","leads":"7","leads_contacted":"0","leads_responded":"0"},{"id":"21805","name":"retail alberton (OTC)","created_date":"2020-04-06 22:32:26","owner_id":"7460","leads":"10","leads_contacted":"0","leads_responded":"0"},{"id":"21806","name":"retail germiston (OTC)","created_date":"2020-04-06 22:35:09","owner_id":"7460","leads":"20","leads_contacted":"0","leads_responded":"0"},{"id":"21807","name":"retail jhb (OTC)","created_date":"2020-04-06 22:37:15","owner_id":"7460","leads":"12","leads_contacted":"0","leads_responded":"0"},{"id":"21808","name":"retail east rand (OTC)","created_date":"2020-04-06 22:38:57","owner_id":"7460","leads":"23","leads_contacted":"0","leads_responded":"0"},{"id":"21809","name":"retail lenasia (OTC)","created_date":"2020-04-06 22:41:01","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"21810","name":"retail midrand (OTC)","created_date":"2020-04-06 22:42:44","owner_id":"7460","leads":"22","leads_contacted":"0","leads_responded":"0"},{"id":"21811","name":"retail randburg (OTC)","created_date":"2020-04-06 22:45:49","owner_id":"7460","leads":"24","leads_contacted":"0","leads_responded":"0"},{"id":"21818","name":"retail roodeport (OTC)","created_date":"2020-04-07 22:30:02","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"21819","name":"retail benoni (OTC)","created_date":"2020-04-07 22:32:14","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"21820","name":"retail kempton park (OTC)","created_date":"2020-04-07 22:36:50","owner_id":"7460","leads":"1","leads_contacted":"0","leads_responded":"0"},{"id":"21821","name":"retail centurion (OTC)","created_date":"2020-04-07 22:38:10","owner_id":"7460","leads":"7","leads_contacted":"0","leads_responded":"0"},{"id":"21822","name":"construction alberton (OTC)","created_date":"2020-04-07 22:40:02","owner_id":"7460","leads":"3","leads_contacted":"0","leads_responded":"0"},{"id":"21823","name":"construction germiston (OTC)","created_date":"2020-04-07 22:41:10","owner_id":"7460","leads":"18","leads_contacted":"0","leads_responded":"0"},{"id":"21824","name":"construction jhb (OTC)","created_date":"2020-04-07 22:42:49","owner_id":"7460","leads":"22","leads_contacted":"0","leads_responded":"0"},{"id":"21825","name":"construction east rand (OTC)","created_date":"2020-04-07 22:44:06","owner_id":"7460","leads":"24","leads_contacted":"0","leads_responded":"0"},{"id":"21826","name":"construction lenasia (OTC)","created_date":"2020-04-07 22:46:04","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"21827","name":"construction midrand (OTC)","created_date":"2020-04-07 22:47:15","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"21828","name":"construction randburg (OTC)","created_date":"2020-04-07 22:48:22","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"21829","name":"construction roodeport (OTC)","created_date":"2020-04-07 22:50:05","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"21830","name":"construction benoni (OTC)","created_date":"2020-04-07 22:51:20","owner_id":"7460","leads":"26","leads_contacted":"0","leads_responded":"0"},{"id":"21831","name":"construction kempton park (OTC)","created_date":"2020-04-07 22:52:37","owner_id":"7460","leads":"17","leads_contacted":"0","leads_responded":"0"},{"id":"21832","name":"construction centurion (OTC)","created_date":"2020-04-07 22:54:03","owner_id":"7460","leads":"7","leads_contacted":"0","leads_responded":"0"},{"id":"21843","name":"technology alberton (OTC)","created_date":"2020-04-09 17:56:21","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"21844","name":"technology germiston (OTC)","created_date":"2020-04-09 17:57:43","owner_id":"7460","leads":"23","leads_contacted":"0","leads_responded":"0"},{"id":"21845","name":"technology jhb (OTC)","created_date":"2020-04-09 17:58:59","owner_id":"7460","leads":"16","leads_contacted":"0","leads_responded":"0"},{"id":"21846","name":"technology east rand (OTC)","created_date":"2020-04-09 18:00:09","owner_id":"7460","leads":"22","leads_contacted":"0","leads_responded":"0"},{"id":"21847","name":"technology lenasia (OTC)","created_date":"2020-04-09 18:02:09","owner_id":"7460","leads":"21","leads_contacted":"0","leads_responded":"0"},{"id":"21848","name":"technology midrand (OTC)","created_date":"2020-04-09 18:03:33","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"21849","name":"technology randburg (OTC)","created_date":"2020-04-09 18:04:38","owner_id":"7460","leads":"26","leads_contacted":"0","leads_responded":"0"},{"id":"21850","name":"technology roodeport (OTC)","created_date":"2020-04-09 18:06:05","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"21851","name":"technology benoni (OTC)","created_date":"2020-04-09 18:35:01","owner_id":"7460","leads":"26","leads_contacted":"0","leads_responded":"0"},{"id":"21852","name":"technology kempton park (OTC)","created_date":"2020-04-09 18:36:18","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"21853","name":"technology centurion (OTC)","created_date":"2020-04-09 18:37:38","owner_id":"7460","leads":"5","leads_contacted":"0","leads_responded":"0"},{"id":"21881","name":"investment alberton (OTC)","created_date":"2020-04-11 23:56:24","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"21882","name":"investment germiston (OTC)","created_date":"2020-04-11 23:58:22","owner_id":"7460","leads":"22","leads_contacted":"0","leads_responded":"0"},{"id":"21883","name":"investment jhb (OTC)","created_date":"2020-04-12 00:00:36","owner_id":"7460","leads":"17","leads_contacted":"0","leads_responded":"0"},{"id":"21884","name":"investment east rand (OTC)","created_date":"2020-04-12 00:01:46","owner_id":"7460","leads":"21","leads_contacted":"0","leads_responded":"0"},{"id":"21885","name":"investment lenasia (OTC)","created_date":"2020-04-12 00:02:53","owner_id":"7460","leads":"18","leads_contacted":"0","leads_responded":"0"},{"id":"21886","name":"investment midrand (OTC)","created_date":"2020-04-12 00:04:00","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"21887","name":"investment randburg (OTC)","created_date":"2020-04-12 00:06:06","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"21888","name":"investment roodeport (OTC)","created_date":"2020-04-12 00:07:28","owner_id":"7460","leads":"24","leads_contacted":"0","leads_responded":"0"},{"id":"21889","name":"investment benoni (OTC)","created_date":"2020-04-12 00:08:55","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"21890","name":"investment kempton park (OTC)","created_date":"2020-04-12 00:10:44","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"21891","name":"investment centurion (OTC)","created_date":"2020-04-12 00:13:00","owner_id":"7460","leads":"4","leads_contacted":"0","leads_responded":"0"},{"id":"22000","name":"food industry alberton (OTC)","created_date":"2020-04-20 00:35:31","owner_id":"7460","leads":"8","leads_contacted":"0","leads_responded":"0"},{"id":"22002","name":"food industry germiston (OTC)","created_date":"2020-04-20 00:37:09","owner_id":"7460","leads":"9","leads_contacted":"0","leads_responded":"0"},{"id":"22003","name":"food industry jhb (OTC)","created_date":"2020-04-20 00:38:51","owner_id":"7460","leads":"12","leads_contacted":"0","leads_responded":"0"},{"id":"22004","name":"food industry east rand (OTC)","created_date":"2020-04-20 00:40:15","owner_id":"7460","leads":"19","leads_contacted":"0","leads_responded":"0"},{"id":"22005","name":"food industry lenasia(OTC)","created_date":"2020-04-20 00:42:18","owner_id":"7460","leads":"2","leads_contacted":"0","leads_responded":"0"},{"id":"22006","name":"food industry midrand (OTC)","created_date":"2020-04-20 00:43:53","owner_id":"7460","leads":"16","leads_contacted":"0","leads_responded":"0"},{"id":"22007","name":"food industry randburg (OTC)","created_date":"2020-04-20 00:45:19","owner_id":"7460","leads":"12","leads_contacted":"0","leads_responded":"0"},{"id":"22008","name":"food industry roodeport (OTC)","created_date":"2020-04-20 00:47:54","owner_id":"7460","leads":"12","leads_contacted":"0","leads_responded":"0"},{"id":"22009","name":"food industry benoni (OTC)","created_date":"2020-04-20 00:49:57","owner_id":"7460","leads":"7","leads_contacted":"0","leads_responded":"0"},{"id":"22010","name":"food industry kempton park (OTC)","created_date":"2020-04-20 00:51:45","owner_id":"7460","leads":"22","leads_contacted":"0","leads_responded":"0"},{"id":"22011","name":"food industry centurion (OTC)","created_date":"2020-04-20 00:54:20","owner_id":"7460","leads":"14","leads_contacted":"0","leads_responded":"0"},{"id":"22016","name":"financial services alberton (OTC)","created_date":"2020-04-20 10:50:47","owner_id":"7460","leads":"4","leads_contacted":"0","leads_responded":"0"},{"id":"22017","name":"financial services germiston (OTC)","created_date":"2020-04-20 10:52:35","owner_id":"7460","leads":"21","leads_contacted":"0","leads_responded":"0"},{"id":"22018","name":"financial services jhb (OTC)","created_date":"2020-04-20 10:54:01","owner_id":"7460","leads":"23","leads_contacted":"0","leads_responded":"0"},{"id":"22019","name":"financial services east rand (OTC)","created_date":"2020-04-20 11:01:38","owner_id":"7460","leads":"24","leads_contacted":"0","leads_responded":"0"},{"id":"22034","name":"financial services lenasia (OTC)","created_date":"2020-04-21 01:59:47","owner_id":"7460","leads":"15","leads_contacted":"0","leads_responded":"0"},{"id":"22035","name":"financial services midrand (OTC)","created_date":"2020-04-21 02:00:53","owner_id":"7460","leads":"26","leads_contacted":"0","leads_responded":"0"},{"id":"22036","name":"financial services randburg (OTC)","created_date":"2020-04-21 02:02:08","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"22037","name":"financial services roodeport (OTC)","created_date":"2020-04-21 02:03:19","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"22038","name":"financial services benoni (OTC)","created_date":"2020-04-21 02:04:39","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"22039","name":"financial services kempton park (OTC)","created_date":"2020-04-21 02:06:19","owner_id":"7460","leads":"24","leads_contacted":"0","leads_responded":"0"},{"id":"22040","name":"financial services centurion (OTC)","created_date":"2020-04-21 02:07:37","owner_id":"7460","leads":"5","leads_contacted":"0","leads_responded":"0"},{"id":"22112","name":"catering alberton (OTC)","created_date":"2020-04-25 23:40:51","owner_id":"7460","leads":"11","leads_contacted":"0","leads_responded":"0"},{"id":"22113","name":"catering germiston (OTC)","created_date":"2020-04-25 23:43:00","owner_id":"7460","leads":"23","leads_contacted":"0","leads_responded":"0"},{"id":"22114","name":"catering jhb (OTC)","created_date":"2020-04-25 23:44:17","owner_id":"7460","leads":"22","leads_contacted":"0","leads_responded":"0"},{"id":"22115","name":"catering east rand","created_date":"2020-04-25 23:45:40","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"22116","name":"catering lenasia (OTC)","created_date":"2020-04-25 23:47:40","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"22117","name":"catering midrand (OTC)","created_date":"2020-04-25 23:49:00","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"22118","name":"catering randburg (OTC)","created_date":"2020-04-25 23:50:18","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"22119","name":"catering roodeport (OTC)","created_date":"2020-04-25 23:51:44","owner_id":"7460","leads":"25","leads_contacted":"0","leads_responded":"0"},{"id":"22120","name":"catering benoni (OTC)","created_date":"2020-04-25 23:53:15","owner_id":"7460","leads":"22","leads_contacted":"0","leads_responded":"0"},{"id":"22121","name":"catering kempton park (OTC)","created_date":"2020-04-25 23:54:50","owner_id":"7460","leads":"19","leads_contacted":"0","leads_responded":"0"},{"id":"22122","name":"catering centurion (OTC)","created_date":"2020-04-25 23:56:47","owner_id":"7460","leads":"20","leads_contacted":"0","leads_responded":"0"},{"id":"22123","name":"real estate alberton (OTC)","created_date":"2020-04-26 06:32:00","owner_id":"7460","leads":"1","leads_contacted":"0","leads_responded":"0"},{"id":"22124","name":"real estate germiston (OTC)","created_date":"2020-04-26 06:33:44","owner_id":"7460","leads":"12","leads_contacted":"0","leads_responded":"0"},{"id":"22125","name":"real estate jhb (OTC)","created_date":"2020-04-26 06:34:56","owner_id":"7460","leads":"8","leads_contacted":"0","leads_responded":"0"},{"id":"22126","name":"real estate east rand (OTC)","created_date":"2020-04-26 06:37:07","owner_id":"7460","leads":"23","leads_contacted":"0","leads_responded":"0"},{"id":"22127","name":"real estate lenasia (OTC)","created_date":"2020-04-26 06:39:25","owner_id":"7460","leads":"13","leads_contacted":"0","leads_responded":"0"},{"id":"22128","name":"real estate midrand (OTC)","created_date":"2020-04-26 06:41:31","owner_id":"7460","leads":"24","leads_contacted":"0","leads_responded":"0"},{"id":"22129","name":"real estate randburg (OTC)","created_date":"2020-04-26 06:43:34","owner_id":"7460","leads":"23","leads_contacted":"0","leads_responded":"0"},{"id":"22130","name":"real estate roodeport (OTC)","created_date":"2020-04-26 06:48:28","owner_id":"7460","leads":"23","leads_contacted":"0","leads_responded":"0"},{"id":"22131","name":"real estate benoni (OTC)","created_date":"2020-04-26 06:50:56","owner_id":"7460","leads":"8","leads_contacted":"0","leads_responded":"0"},{"id":"22132","name":"real estate kempton park","created_date":"2020-04-26 06:53:22","owner_id":"7460","leads":"10","leads_contacted":"0","leads_responded":"0"}],"status":"success","message":"Data acquired successfully!"}
"""

url4 = "https://app.leadflow360.net/api/campaigndata" # post request campaign id


def writeContentTo(filePath, data_array):
    saveFile = open(filePath, "w")
    for data in data_array:
        saveFile.write(str(data))
        saveFile.flush()
    saveFile.close()

def printFrom(filePath):
    saveFile = open(filePath, "r")
    data = saveFile.read()
    print(data)
    saveFile.close()

def getJSONFromString(s):
    saveData = str(s) 
    saveData = saveData.replace("\'", "\"")
    return json.loads(saveData)

def getJSONFromFile(filePath):
    saveFile = open(filePath, "r")
    saveData = saveFile.read()
    saveData = saveData.replace("\'", "\"")
    info = json.loads(saveData)
    saveFile.close()
    return info

def getLeads(data):
    output = ""

    for x in data:
        #print(x['name'])
        input = "name: "+str(x['name'])+"\n"+"fb_link: "+str(x['fb_link'])+"\n"+"likes: "+str(x['likes'])+"\n"+"city: "+str(x['city'])+"\n"+"street: "+str(x['street'])+"\n"+"zip: "+str(x['zip'])+"\n"+"website: "+str(x['website'])+"\n"+"email: "+str(x['email'])+"\n"+"phone: "+str(x['phone'])+"\n"+"description: "+str(x['description'])+"\n"+"\n"
        output = output + input
    return output

""""
'name': 'PKM Investments', 'fb_id': '316702535653450', 'fb_link': 'https://www.facebook.com/316702535653450', 'likes': '0'
'city': 'Alberton' 'street': '54 Kritzinger Ave', 'zip': '1449' 'website': '', 'email': '', 'phone': '+27119024909'
 'description': ''
"""


def getOTCCampaignIDs(userCampaigns):
    output_ids = list()
    for x in userCampaigns:
        a = str(x["name"])
        if a.__contains__("OTC"):
            output_ids.append([x["id"], x["name"]])
    return output_ids


def getDataAndSaveToPath(campaignInfos, ses):
    for x in campaignInfos:
        file = "./campaigns/" + x[1] + ".txt"
        #print(x)
        data = str(getCompaignDataText(str(x[0]), ses))
        #print(data)



        #data = getJSONFromString(data)
        data = json.loads(data)
        actions = data["actions"]
        leads = getLeads(actions)

        f = open(file, "w")
        f.write(leads)
        f.close()
    pass

def getCompaignData(c_id, ses):
    id = {"id": c_id}
    urlcampid = "https://app.leadflow360.net/api/campaigndata"
    camp = ses.post(urlcampid, headers=appminheaders, data=id)

    return camp.json()


def getCompaignDataText(c_id, ses):
    id = {"id": c_id}
    urlcampid = "https://app.leadflow360.net/api/campaigndata"
    camp = ses.post(urlcampid, headers=appminheaders, data=id)

    return camp.text