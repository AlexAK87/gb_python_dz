import requests


def currency_rates(*args):
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    response_text = response.text

    start_valuate = 0
    end_value = 0
    list_valute = []

    while end_value != -1:
        start_valuate = response_text.find("<Valute ID", start_valuate, len(response_text))
        end_value = response_text.find("</Valute>", start_valuate, len(response_text))

        result = response_text[start_valuate:end_value]
        list_valute.append(result)

        start_valuate += len(result)

    result_valute = {}
    for charcode in args:
        for valute in list_valute:
            if charcode.upper() in valute:
                start = valute.find("<Value>", 0, len(valute)) + len("<Value>")
                end = valute.find("</Value>", 0, len(valute))

                result = valute[start:end]

                result_valute.setdefault(charcode, float(result.replace(',', '.')))
        else:
            result_valute.setdefault(charcode, None)

    return result_valute


print(currency_rates("USD", "EUR"))
