import requests
KEY = 'trnsl.1.1.20200525T072029Z.2bda4bb1c2e30c2e.9bf6b08673dee84124b7d76ef54458cfaae86242' #API ключ, взяли с
#яндекса
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
def translate_me(mytext):
#    yandex translate plugin
#    docs: https://tech.yandex.com/translate/doc/dg/reference/translate-docpage/
#    вначале регаем API ключ на сайте яндекса
#    https: // translate.yandex.net / api / v1.5 / tr.json / translate
#    key= API-ключ достаем по ссылке https://translate.yandex.ru/developers/keys
#    text - переводимый текст
#    lang - направление перевода
#    format - формат текста, опционально
#    option - опция перевода, опционально
#    callback - имя колбэк функции, опционально
    params={ #словари для гет запросов
        'key':KEY,
        'text':mytext,
        'lang':'ru-en'# тут можно указать вместо en французский fr а вместо ru указать en
        # и будет перевод на французский с русского или английского и тд можно играться

    }
    response = requests.get(URL,params=params)
    return response.json()
json = translate_me('Привет друг')
#далее пишем принт и указываем что нужно вывести
#['text'] значит только текст без кода и тд
#[0] - убираем кавычки из текста
#print(json['text'][0])
print(''.join(json['text']))