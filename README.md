### Working with Yandex Mail using http requests.

This code works with [Yandex Mail](https://mail.yandex.ru/ "Yandex Mail"). 

It reads incoming emails and sends mails from drafts folder.

It works properly *at the current* (2022.07.22) moment. 

The folder **raw requests** contains the original http requests, except for sending a draft request (to be added later), with the username *example20220722* and the password *example20220722example20220722*, which does not belong to any mailbox (otherwise it is a coincidence).

### How to use?

Install python, download this package (libraries and dependencies are included) and adjust it to your needs.

**config.py** contains *login*, *password* and *to_mail* variables, substitute your values. *login* and *password* is your Yandex Mail credentials, *to_emails* assumes the destination address of emails when sending the contents of the drafts folder. 

You can find usage examples in **usage_example.py** file. Make sure that your mailbox contains emails, including the drafts folder. Keep in mind that sending drafts does not automatically remove it.

### Project objective

The goal of the project is to complete a task that meets the requirements: 
1. reading Yandex emails via http.
2. sending emails from the draft.

| contacts        | Stepan Solovey |
| ------------- |-------------:| 
| email:      | st.solovey@gmail.com |
| telegram:      | [t.me/duckever](https://t.me/duckever)      |   
