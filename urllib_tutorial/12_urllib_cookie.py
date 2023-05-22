import urllib.request
import urllib.parse
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.aritzia.com/en/my-account'

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
# }


headers ={
'Cookie':
'dw=1; dw=1; cqcid=bebn24Py74YSnGvRacqzw1MEV0; dwanonymous_2229be5ea6f3843440b278529e0389ad=bebn24Py74YSnGvRacqzw1MEV0; AritziaSiteCookie=Aritzia_CA|ca|en_CA; __cq_dnt=0; dw_dnt=0; _dy_csc_ses=t; _dy_c_exps=; _dycnst=dg; _dyid=-7606579528426061968; _dyjsession=1515d1903c7752da5d24658784040422; dy_fs_page=www.aritzia.com%2Fen%2Fhome; _dy_geo=CA.NA.CA_MB.CA_MB_Winnipeg; _dy_df_geo=Canada..Winnipeg; _gid=GA1.2.123577421.1684537201; scarab.visitor=%2235D7612AA37B7547%22; __cq_uuid=bebn24Py74YSnGvRacqzw1MEV0; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; _dyid_server=-7606579528426061968; _dy_c_att_exps=; _dy_toffset=0; _gcl_au=1.1.1749686520.1684537243; dwcustomer_2229be5ea6f3843440b278529e0389ad=adVZulRay2pZXli5b6yxSuL2oc; dwsid=QKUXK7zsy2Kh5638lHIsa9fiT3PAxahDeEgQy9l6CFLkgOxAoP1Lbf8UKOhI9OU-j2vkGp67ckAevMP8s4Ww7g==; dwac_bccBUiaagYFO6aaacZXJ6E64UQ=JpmUtcC9fQnAJTUsILkThAWxCoBYzMnZeYo%3D|dw-only|9006220545||CAD|false|Canada%2FPacific|true; cquid=Z4B8DbQq8osE9TGXWpJOh5V8KqQGfjTIgoTM2Ea0PKM=|a2ed312dd8e5766515139dc6daef8f1f926f4ba8ab887e16ad15fbdc6570db53|a2ed312dd8e5766515139dc6daef8f1f926f4ba8ab887e16ad15fbdc6570db53; sid=0jetyMj-W-Ov3GI8NfwP20Vw9ZC01zjCdnM; _dy_soct=772465.1466703.1684537276*776956.1473910.1684537276*700461.1338537.1684537276; _dyfs=1684537276511; _dycst=dk.m.c.ms.; _dy_ses_load_seq=47690%3A1684537357033; _dy_lu_ses=1515d1903c7752da5d24658784040422%3A1684537357033; _ga_JXP2NR5NZ4=GS1.1.1684537201.1.1.1684537373.0.0.0; OptanonConsent=isIABGlobal=false&datestamp=Fri+May+19+2023+18%3A02%3A54+GMT-0500+(Central+Daylight+Time)&version=6.38.0&hosts=&consentId=44ad15a7-e2a3-45c4-a719-fe153428d773&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false; _ga=GA1.2.77853865.1684537201; ADRUM=s=1684537710641&r=https%3A%2F%2Fwww.aritzia.com%2Fen%2Fmy-account',

'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}


# Customization of the request object
request = urllib.request.Request(url=url, headers=headers)
# Simulate a browser sending a request to the server
response = urllib.request.urlopen(request)
# Get the data for the response
content = response.read().decode('utf-8')
print(content)


with open('aritzia.html','w',encoding='utf-8')as fp:
    fp.write(content)