import requests
from bs4 import BeautifulSoup
import json
import datetime
from math import floor
import config


class MailFromRawToCollection:
    def __init__(self, raw_mail):
        self.dateTime = datetime.datetime(year = raw_mail['date']['chunks']['year'], 
                          month = raw_mail['date']['chunks']['month'],
                          day = raw_mail['date']['chunks']['date'],
                          hour = raw_mail['date']['chunks']['hours'],
                          minute = raw_mail['date']['chunks']['minutes'])
        self.fromName = raw_mail['recipients']['from']['displayName']
        self.fromEmail = raw_mail['recipients']['from']['email']
        self.toName = raw_mail['recipients']['to']['displayName']
        self.toEmail = raw_mail['recipients']['to']['email']
        self.subject = raw_mail['subject']
        self.firstline = raw_mail['firstline']
    def array_mail(self):
        return [self.dateTime, self.fromName,self.fromEmail,self.toName,self.toEmail,self.subject,self.firstline]
    def dict_mail(self):
        return {
            "dateTime":self.dateTime,
            "fromName":self.fromName,
            "fromEmail":self.fromEmail,
            "toName":self.toName,
            "toEmail":self.toEmail,
            "subject":self.subject,
            "firstline":self.firstline
        }

class YandexMailHttpProcessing:
    def __init__(self, login, password):
        self.s = requests.Session()
        ######## 1 get csrf and process_uuid
        headers1 = {
            'Host' : 'passport.yandex.ru',
            'Connection' : 'keep-alive',
            'sec-ch-ua' : '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile' : '?0',
            'sec-ch-ua-platform' : '"Windows"',
            'Upgrade-Insecure-Requests' : '1',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site' : 'same-site',
            'Sec-Fetch-Mode' : 'navigate',
            'navigate' : '?1',
            'Sec-Fetch-Dest' : 'document',
            'Referer' : 'https://yandex.ru/',
            'Accept-Encoding' : 'gzip, deflate, br',
            'Accept-Language' : 'en-US,en;q=0.9'
            }
        url1 = 'https://passport.yandex.ru/auth'
        r1 = self.s.get(url1, headers=headers1)

        ######## 2 send login
        soup1 = BeautifulSoup(r1.text, 'lxml')
        csrf_token = soup1.find('input', attrs={'type':'hidden', 'name':'csrf_token'})['value']
        href = soup1.find('a', attrs={'class':'Button2 Button2_type_link Button2_size_l Button2_view_pseudo Button2_width_max'})['href']
        process_uuid = href.split("=")[1]

        
        headers2 = {
            'Host': 'passport.yandex.ru',
            'Connection': 'keep-alive',
            'Content-Length': '189',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'Origin': 'https://passport.yandex.ru',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://passport.yandex.ru/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        url2 = 'https://passport.yandex.ru/registration-validations/auth/multi_step/start'
        data2 = {
            "csrf_token":csrf_token, 
            'process_uuid':process_uuid, 
            'login':login, 
            'repath': 'https://yandex.ru', 
            'origin':'home_yandexid'
            }
        r2 = self.s.post(url2, headers=headers2, cookies=self.s.cookies, data=data2)

        ######## 3 send password
        headers3 = {
            'Host': 'passport.yandex.ru',
            'Connection': 'keep-alive',
            'Content-Length': '177',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'Origin': 'https://passport.yandex.ru',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://passport.yandex.ru/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        url3 = 'https://passport.yandex.ru/registration-validations/auth/multi_step/commit_password'

        track_id = json.loads(r2.text)['track_id']
        data3 = {
            'csrf_token':csrf_token,
            'track_id':track_id,
            'password':password,
            'retpath':'https://yandex.ru'
        }
        self.s.post(url3, headers=headers3, cookies=self.s.cookies, data=data3)

        ######### 4 
        headers4 = {
            'Host': 'mail.yandex.ru',
            'Connection': 'keep-alive',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://yandex.ru/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        url4 = 'https://mail.yandex.ru/'
        r4 = self.s.get(url4, headers = headers4, cookies = self.s.cookies,data={})

        ######## 4 get draft emails

        soup4 = BeautifulSoup(r4.text, 'lxml')
        script4 = json.loads(soup4.find("script", {"id": "insert-js"}).string)
        d4 = script4['prefetched']['models']['account-information']['data']
        self.ckey = d4['ckey']
        self.uid = d4['uid']
        self.locale = d4['locale']
        self.product = script4['Config']['product']
        self.connection_id = script4['Config']['connection_id']
        self.exp = script4['Config']['exp-boxes']
        self.eexp = script4['Config']['eexp-boxes']
        self.service = script4['Config']['service']
        self.version = script4['Config']['version']
        self.messages_per_page = script4['prefetched']['models']['settings']['data']['messages_per_page']

    def rawMailToArray(raw_mail):
        dateTime = datetime.datetime(year = raw_mail['date']['chunks']['year'], 
                          month = raw_mail['date']['chunks']['month'],
                          day = raw_mail['date']['chunks']['date'],
                          hour = raw_mail['date']['chunks']['hours'],
                          minute = raw_mail['date']['chunks']['minutes'])
        fromName = raw_mail['recipients']['from']['displayName']
        fromEmail = raw_mail['recipients']['from']['email']
        toName = raw_mail['recipients']['to']['displayName']
        toEmail = raw_mail['recipients']['to']['email']
        subject = raw_mail['subject']
        firstline = raw_mail['firstline']
        return [dateTime, fromName,fromEmail,toName,toEmail,subject,firstline]

    def getMails(self):
        mailsModel = [{'name': 'folders', 'params': {}, 'meta': {'requestAttempt': 1}},
            {'name': 'labels', 'params': {}, 'meta': {'requestAttempt': 1}},
            {'name': 'messages',
            'params': {'current_folder': True,
            'with_pins': 'yes',
            'sort_type': 'date',
            'threaded': 'yes',
            'tabId': 'relevant'},
            'meta': {'requestAttempt': 1}},
            {'name': 'tabs', 'params': {}, 'meta': {'requestAttempt': 1}},
            {'name': 'stickers',
            'params': {'type': 'reply_later'},
            'meta': {'requestAttempt': 1}}]
        timestamp = floor(datetime.datetime.timestamp(datetime.datetime.now())*1000)
        data5 =   {'_ckey' : self.ckey,
            '_uid' : self.uid, 
            '_locale' : self.locale,
            '_timestamp' : timestamp,
            '_product' : self.product,
            '_connection_id' : self.connection_id,
            '_exp' : self.exp,
            '_eexp' : self.eexp,
            '_service': self.service,
            '_version': self.version,
            '_messages_per_page': self.messages_per_page,
            'models': mailsModel
            }
        url5 = 'https://mail.yandex.ru/web-api/models/liza1?_m=folders,labels,messages,tabs,stickers'
        headers5 = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; encoding=utf-8',
            'Origin': 'https://mail.yandex.ru',
            'Referer': 'https://mail.yandex.ru/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            }
        r5 = self.s.post(url5, headers = headers5, cookies = self.s.cookies, json = data5)

        ##### getting the list of mails from the mailbox
        mailbox = json.loads(r5.text)
        models = mailbox['models'][2]
        mails = models['data']['message']

        return mails

    def sendDrafts(self, to_mail):
        draftModels = [{
                        "name":"messages",
                        "params":
                            {
                            "current_folder":"6",
                            "sort_type":"date"
                            },
                        "meta":
                            {
                            "requestAttempt":1
                            }
                        }]
        timestamp = floor(datetime.datetime.timestamp(datetime.datetime.now())*1000)
        data5 =   {'_ckey' : self.ckey,
            '_uid' : self.uid, 
            '_locale' : self.locale,
            '_timestamp' : timestamp,
            '_product' : self.product,
            '_connection_id' : self.connection_id,
            '_exp' : self.exp,
            '_eexp' : self.eexp,
            '_service': self.service,
            '_version': self.version,
            '_messages_per_page': self.messages_per_page,
            'models': draftModels
            }
        url5 = 'https://mail.yandex.ru/web-api/models/liza1?_m=folders,labels,messages,tabs,stickers'
        headers5 = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; encoding=utf-8',
            'Origin': 'https://mail.yandex.ru',
            'Referer': 'https://mail.yandex.ru/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            }
        r5 = self.s.post(url5, headers = headers5, cookies = self.s.cookies, json = data5)



        ##### 6 emails sending
        url6 = 'https://mail.yandex.ru/web-api/do-send/liza1'
        headers6 = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://mail.yandex.ru',
        'Referer': 'https://mail.yandex.ru/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        }
        
        mailbox = json.loads(r5.text)
        drafts = mailbox['models'][0]['data']['message']
        statuses = []
        for i in drafts:
            message_id = i['message_id']
            subject = i['subject']
            email = i['field'][0]['email']
            name = i['field'][0]['name']
            
            data_send = {
                'bcc': '',
                'captcha_entered': '',
                'captcha_key': '',
                'cc': '',
                'charset': '',
                'confirm_limit': '',
                'current_folder': '6',
                'doit': '',
                'fid': '',
                'from_mailbox': email,
                'from_name': name,
                'get_abook': '',
                'html': '',
                'idcs': '',
                'ign_overwrite': 'no',
                'initial_cc': '',
                'initial_to': '',
                'inreplyto': '',
                'lids': 'FAKE_SEEN_LBL',
                'mark_as': '',
                'disk_att': '',
                'nosave': '',
                'nosend': '',
                'notify_on_send': 'no',
                'overwrite': '179862510118109269',
                'phone': '',
                'references': '',
                'remind_period': '',
                'retpath': '',
                'returl': '',
                'saveDraft': '',
                'save_symbol': 'draft',
                'send': '',
                'send_time': '',
                'store_fid': '',
                'store_name': '',
                'strict_charset': '',
                'style': '',
                'subj': subject,
                'to': to_mail,
                'ttype': 'html',
                'withUpdatedUndoAndDelayedErrorHandling': 'yes',
                '_connection_id': self.connection_id,
                '_ckey': self.ckey,
                '_uid': self.uid,
                '_eexp': self.eexp,
                'message_id': message_id,
                'current_time': '',
                'captcha_token': '',
                'parts_json': ''
            }
            r6 = self.s.post(url6, headers = headers6, cookies = self.s.cookies, data = data_send)

            statuses.append(json.loads(r6.text))

        return statuses

