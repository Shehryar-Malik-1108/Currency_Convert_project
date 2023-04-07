import requests
import requests


api_key = "248de08a7ea62102a9b027f6"

def convert_currency():
    from_currency = input('Enter a currency: ')
    to_currency = input('Enter a currency to convert: ')
    while True:
        try:
            amount = float(input('Enter the amount: '))
        except:
            print('The amount must be a numeric value!')
            continue

        if not amount > 0:
            print('The amount must be greater than 0')
            continue
        else:
            break

    url = (f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}")

    response = requests.request('GET', url)
    status_code = response.status_code

    if status_code != 200:
        print('Uh oh, there was a problem. Please try again later')
        quit()
    else:
        result = response.json()
        print('Conversion result: ' + str(result["conversion_rates"][to_currency]* amount))




if __name__ == '__main__':
    convert_currency()
