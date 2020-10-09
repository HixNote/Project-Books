import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        return False


def get_book_data(book):
    html = get_html(book['book'])
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find('div', class_='product-description')
    title = soup.find('div', class_='prodtitle').find('h1').text
    author = data.find('div', class_='authors').find('a').text
    other_creators = None
    country = None
    original_language = None
    edition_language = None
    year_of_creating = None
    year_of_edition = data.find('div', class_='publisher').text[-7:-3]
    ISBN = data.find('div', class_='isbn').text[6:]
    publishing = data.find('div', class_='publisher').find('a').text
    pages_count = data.find('div', class_='pages2').text[9:13]
    cover = soup.find('div', id='product-image').find('img')['src']
    scans = soup.find('img', class_='fotorama__img')
    annotation = soup.find('div', id='product-about').text
    last_update = book['lastmod']
    shop_url = book['book']
    price = soup.find('span', class_='buying-priceold-val-number').text
    sale_price=soup.find('span', class_='buying-pricenew-val-number').text

    book_data = {
        'title': title,
        'author': author,
        'other_creators': other_creators,
        'country': country,
        'original_language': original_language,
        'edition_language': edition_language,
        'year_of_creating': year_of_creating,
        'year_of_edition': year_of_edition,
        'ISBN': ISBN,
        'publishing': publishing,
        'pages_count': pages_count,
        'cover': cover,
        'scans': scans,
        'annotation': annotation,
        'last_update': last_update,
        'shop_url': shop_url,
        'price':price,
        'sale_price':sale_price
        }
    print(book_data)


dict = {"book": "https://www.labirint.ru/books/746088/", "lastmod": "2020-09-26T01:45:47+03:00"}
get_book_data(dict)
