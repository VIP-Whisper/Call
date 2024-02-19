import requests,random
NUMS = '1234567890'
LETTS = 'abcdefghijklmnopqrstuvwxyz'
num = input('[+] Enter Number With Country Code : ')
req = requests.post('https://account-asia-south1.truecaller.com/v2/sendOnboardingOtp',headers= {'content-type':'application/json; charset=UTF-8','accept-encoding':'gzip','user-agent':'Truecaller/11.75.5 (Android;10)','clientsecret':'lvc22mp3l1sfv6ujg83rd17btt'},json={'countryCode':'','dialingCode':None,'installationDetails': {'app': {'buildVersion':5,'majorVersion':11,'minorVersion':75,'store':'GOOGLE_PLAY'},'device': {'deviceId':''.join(random.choices(NUMS+LETTS, k=16)),'language':'en','manufacturer':'Xiaomi','mobileServices':['GMS'],'model':'M2010J19SG','osName':'Android','osVersion':'10','simSerials':[''.join(random.choices(NUMS, k=19)), ''.join(random.choices(NUMS, k=20))]},'language':'en','sims': [{'imsi':''.join(random.choices(NUMS, k=15)),'mcc':'413','mnc':'2','operator':None}]},'phoneNumber':num,'region':'region-2','sequenceNo':random.randint(1,2)})
if req.json()['status'] == 1 or req.json()['status'] == 9:
 print(req.json()['message'])
else:
 print(req.json()['message'])