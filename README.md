### Login to the Yandex Mail, return the list of emails and send emails from drafts, using http requests.

This code works with [Yandex Mail](https://mail.yandex.ru/ "Yandex Mail"). It reads incoming emails and sends mails from drafts folder.

### How to use?

Install python, download this package (libraries and dependencies are included) and adjust it to your needs.

**config.py** contains *login*, *password* and *to_mail* variables, substitute your values. 

*login* and *password* is your Yandex Mail credentials, *to_emails* assumes the destination address of emails when sending the contents of the drafts folder. 

Keep in mind that sending drafts does not automatically delete it.

You can find usage examples in **usage_example.py** file.

### Project objective

The goal of the project is to complete a task that meets the requirements: 
1. reading emails on Yandex via http.
2. sending emails from the draft.

| contacts        | Stepan Solovey |
| ------------- |-------------:| 
| email:      | st.solovey@gmail.com |
| telegram:      | [t.me/duckever](https://t.me/duckever)      |   
