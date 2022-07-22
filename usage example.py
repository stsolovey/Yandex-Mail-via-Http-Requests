from yandex_mail_requests_http import YandexMailHttpProcessing, MailFromRawToCollection
from config import login, password, to_mail

######### Login To Yandex Mail via http, requests
ymhp = YandexMailHttpProcessing(login, password)

######### Get Emails
raw_mails = ymhp.getMails()

######### Convert To List of Lists
lists = []
for mail in raw_mails:
    lists.append(MailFromRawToCollection(mail).array_mail())

######### To List of Dicts
dicts = []
for mail in raw_mails:
    dicts.append(MailFromRawToCollection(mail).dict_mail())

######### Example Output
for item in lists:
    print(item)

print("\n\n\n############################################\n\n\n")

for item in dicts:
    print(item)


print("\n\n\n############################################\n\n\n")
######### Send Drafts
res = ymhp.sendDrafts(to_mail)
for i in res:
    print(i)