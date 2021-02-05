import requests
from datetime import date

def scraper(pageNumber=0):

    try:
        url = f"https://mercavus-api.com/api/maker?currencyCode=EUR&limit=40&servingCountryCode=FR&skip={pageNumber}"

        payload={
        'platform': 'RetailerWeb'
        }
        headers = {
        'platform': 'RetailerWeb',
        'Content-Type': 'application/json',
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
        }

        response = requests.get(url, headers=headers, data=payload)

        datas = response.json()

        brands = datas['data']['list']

        for brand in brands:
            id = brand['_id']
            name = brand['name']
            country = brand['originCountryCode']

            products = {
                'id': id,
                'name': name,
                'country': country,
                'date': date.today()
            }

            

        pageNumber += 40
        scraper(pageNumber=pageNumber)

        
    except RecursionError:
        return

scraper()

        







