### Yandex-Mail-via-Http-Requests

### tested on a mailbox with five incoming emails and a non-empty folder with drafts (no more than 10)

      #Login To Yandex Mail via http, requests
      ymhp = YandexMailHttpProcessing(login, password)

      #Get Emails
      raw_mails = ymhp.getMails()

      #Convert To List of Lists
      lists = []
      for mail in raw_mails:
            lists.append(MailFromRawToCollection(mail).array_mail())

      #To List of Dicts
      dicts = []
      for mail in raw_mails:
            dicts.append(MailFromRawToCollection(mail).dict_mail())

      #Example Output
      for item in lists:
            print(item)

      print("\n\n\n############################################\n\n\n")

      for item in dicts:
            print(item)

      #Send Drafts
      ymhp.sendDrafts(to_mail)

### Output


      """
      [datetime.datetime(2022, 6, 13, 0, 40), 'Команда Яндекс.Диска', 'Команда Яндекс.Диска <promo@disk.yandex.ru>', '"test04072022@yandex.ru"', '"test04072022@yandex.ru" <test04072022@yandex.ru>', 'Добро пожаловать в Яндекс Диск! 
      Мы поможем вам узнать больше о функциях сервиса', 'Вы зарегистрировались в Яндекс Диске Безлимит для фото Установите мобильное приложение Диска, и вы сможете хранить все свои фото, снятые на телефон. Освободите место на компьютере Скачайте приложение Диска']
      [datetime.datetime(2022, 6, 13, 0, 39), 'Яндекс ID', 'Яндекс ID <noreply@id.yandex.ru>', '"test04072022@yandex.ru"', '"test04072022@yandex.ru" <test04072022@yandex.ru>', 'Кто-то входит в Ваш аккаунт на Яндексе', 'Кто-то ввёл 
      правильный пароль от аккаунта test04072022, который Вы используете в Почте и других сервисах Яндекса. Вот что нам известно: Место: Москва и Московская область Программа: Chrome 103.0.0.0 (Windows 10) Если это были не']       
      [datetime.datetime(2022, 6, 4, 18, 53), 'Команда Яндекс.Почты', 'Команда Яндекс.Почты <hello@yandex-team.ru>', '"test04072022@yandex.ru"', '"test04072022@yandex.ru" <test04072022@yandex.ru>', 'Как убедиться, что письмо доставлено', 'Мы подготовили несколько писем с полезными советами, которые помогут вам освоиться в новом ящике. Для начала расскажем про отправку писем. Послать письмо — дело нехитрое. Но иногда возникает сомнение, дошло']
      [datetime.datetime(2022, 6, 4, 15, 34), 'Stepan Solovey', 'Stepan Solovey <st.solovey@gmail.com>', '"test04072022@yandex.ru"', '"test04072022@yandex.ru" <test04072022@yandex.ru>', 'Письмо2', 'Тело письма 2']
      [datetime.datetime(2022, 6, 4, 15, 33), 'Stepan Solovey', 'Stepan Solovey <st.solovey@gmail.com>', '"test04072022@yandex.ru"', '"test04072022@yandex.ru" <test04072022@yandex.ru>', 'Тема письма', 'Текст вложения']



      ############################################



      {'dateTime': datetime.datetime(2022, 6, 13, 0, 40), 'fromName': 'Команда Яндекс.Диска', 'fromEmail': 'Команда Яндекс.Диска <promo@disk.yandex.ru>', 'toName': '"test04072022@yandex.ru"', 'toEmail': '"test04072022@yandex.ru" <test04072022@yandex.ru>', 'subject': 'Добро пожаловать в Яндекс Диск! Мы поможем вам узнать больше о функциях сервиса', 'firstline': 'Вы зарегистрировались в Яндекс Диске Безлимит для фото Установите мобильное приложение Диска, и вы сможете хранить все свои фото, снятые на телефон. Освободите место на компьютере Скачайте приложение Диска'}
      {'dateTime': datetime.datetime(2022, 6, 13, 0, 39), 'fromName': 'Яндекс ID', 'fromEmail': 'Яндекс ID <noreply@id.yandex.ru>', 'toName': '"test04072022@yandex.ru"', 'toEmail': '"test04072022@yandex.ru" <test04072022@yandex.ru>', 'subject': 'Кто-то входит в Ваш аккаунт на Яндексе', 'firstline': 'Кто-то ввёл правильный пароль от аккаунта test04072022, который Вы используете в Почте и других сервисах Яндекса. Вот что нам известно: Место: Москва и Московская область Программа: Chrome 103.0.0.0 (Windows 10) Если это были не'}
      {'dateTime': datetime.datetime(2022, 6, 4, 18, 53), 'fromName': 'Команда Яндекс.Почты', 'fromEmail': 'Команда Яндекс.Почты <hello@yandex-team.ru>', 'toName': '"test04072022@yandex.ru"', 'toEmail': '"test04072022@yandex.ru" <test04072022@yandex.ru>', 'subject': 'Как убедиться, что письмо доставлено', 'firstline': 'Мы подготовили несколько писем с полезными советами, которые помогут вам освоиться в новом ящике. Для начала расскажем про отправку писем. Послать письмо — дело нехитрое. Но иногда возникает сомнение, дошло'}
      {'dateTime': datetime.datetime(2022, 6, 4, 15, 34), 'fromName': 'Stepan Solovey', 'fromEmail': 'Stepan Solovey <st.solovey@gmail.com>', 'toName': '"test04072022@yandex.ru"', 'toEmail': '"test04072022@yandex.ru" <test04072022@yandex.ru>', 'subject': 'Письмо2', 'firstline': 'Тело письма 2'}
      {'dateTime': datetime.datetime(2022, 6, 4, 15, 33), 'fromName': 'Stepan Solovey', 'fromEmail': 'Stepan Solovey <st.solovey@gmail.com>', 'toName': '"test04072022@yandex.ru"', 'toEmail': '"test04072022@yandex.ru" <test04072022@yandex.ru>', 'subject': 'Тема письма', 'firstline': 'Текст вложения'}
      """
