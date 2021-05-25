import requests
import datetime as dat


def currency_rates(charcode):
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    response_text = response.text

    start_valuate = 0
    end_value = 0
    list_valute = []

    start_date = response_text.find("Date=""", 0, len(response_text))
    start = start_date + len("Date=""") + 1
    end = start_date + len("Date=""") + 11
    datatime_currency = response_text[start:end]
    data_currency = dat.datetime.strptime(datatime_currency.replace('.', '/'), "%d/%m/%Y").date()

    while end_value != -1:
        start_valuate = response_text.find("<Valute ID", start_valuate, len(response_text))
        end_value = response_text.find("</Valute>", start_valuate, len(response_text))

        result = response_text[start_valuate:end_value]
        list_valute.append(result)

        start_valuate += len(result)

    for valute in list_valute:
        if charcode.upper() in valute:
            start = valute.find("<Value>", 0, len(valute)) + len("<Value>")
            end = valute.find("</Value>", 0, len(valute))

            result = valute[start:end]
            result_currency = float(result.replace(',', '.'))

            return f'{result_currency}, {data_currency}'
    else:
        return f'{None}, {data_currency}'


if __name__ == '__main__':
    currency_rates()
else:
    pass
