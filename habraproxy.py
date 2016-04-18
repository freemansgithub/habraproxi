#  habraproxy.py — это простейший http-прокси-сервер, запускаемый локально (порт на ваше 
#  усмотрение), который показывает содержимое страниц Хабра. С одним исключением: после  
#  каждого слова из шести букв должен стоять значок «™». Примерно так:
#
#  http://habrahabr.ru/company/yandex/blog/258673/
#  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#  Сейчас на фоне уязвимости Logjam все в индустрии в очередной раз обсуждают проблемы и 
#  особенности TLS. Я хочу воспользоваться этой возможностью, чтобы поговорить об одной из 
#  них, а именно — о настройке ciphersiutes.
#
#  http://127.0.0.1:8232/company/yandex/blog/258673/
#  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#  Сейчас™ на фоне уязвимости Logjam™ все в индустрии в очередной раз обсуждают проблемы и 
#  особенности TLS. Я хочу воспользоваться этой возможностью, чтобы поговорить об одной из 
#  них, а именно™ — о настройке ciphersiutes. 
#
#  Условия:
#    * Python 2.x
#    * можно использовать любые общедоступные библиотеки, которые сочтёте нужным
#    * чем меньше кода, тем лучше. PEP8 — обязательно
#    * в случае, если не хватает каких-то данных, следует опираться на здравый смысл
#
#  Если задача кажется слишом простой, можно добавить следующее:
#    * параметры командной строки (порт, хост, сайт, отличный от хабра и т.п.)
#    * после старта локального сервера автоматически запускается браузер с открытой 
#      обработанной™ главной страницей
 
 
def main():
    print 'Coming soon...'
 
 
if __name__ == '__main__':
    main()