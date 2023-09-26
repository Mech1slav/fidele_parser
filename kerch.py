import arrow
import time
import re
from selenium import webdriver
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from xml.dom import minidom

utc = arrow.utcnow().format('YYYY-MM-DD' + "T" 'HH:mm:ss' + "+03:00")
yml_catalog = ET.Element("yml_catalog", date=utc)

shop = ET.Element("shop")
yml_catalog.append(shop)

# ---------------------------шапка файла---------------------------

name = ET.Element("name")
name.text = "Fidele Керчь"
shop.append(name)

company = ET.Element("company")
company_text = 'Доставка еды Fidele Керчь'
company.text = company_text
shop.append(company)

url = ET.Element("url")
url_text = "https://fidele-food.ru/kerch"
url.text = url_text
shop.append(url)

currencies = ET.Element("currencies")
shop.append(currencies)

currency = ET.Element("currency")
currency.set('id', "RUR")
currency.set('rate', "1")
currencies.append(currency)

# ---------------------------/шапка файла---------------------------

# ---------------------------Категории---------------------------

categories = ET.Element("categories")
shop.append(categories)

category = ET.Element("category")
category.set('id', "2")
category.set('parent_Id', "1")
category_text = "Пицца"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "4")
category.set('parent_Id', "1")
category_text = "Паста"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "6")
category.set('parent_Id', "5")
category_text = "Маки роллы"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "7")
category.set('parent_Id', "5")
category_text = "Роллы"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "8")
category.set('parent_Id', "5")
category_text = "Запечённые роллы"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "9")
category.set('parent_Id', "5")
category_text = "Темпура"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "10")
category.set('parent_Id', "5")
category_text = "Наборы"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "14")
category.set('parent_Id', "13")
category_text = "Лапша WOK"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "16")
category.set('parent_Id', "13")
category_text = "Супы"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "18")
category.set('parent_Id', "17")
category_text = "Завтраки"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "155")
category.set('parent_Id', "17")
category_text = "Комбо обеды"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "19")
category.set('parent_Id', "17")
category_text = "Салаты"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "20")
category.set('parent_Id', "17")
category_text = "Первые блюда"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "21")
category.set('parent_Id', "17")
category_text = "Вторые блюда"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "22")
category.set('parent_Id', "17")
category_text = "Гарниры"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "23")
category.set('parent_Id', "17")
category_text = "Закуски"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "170")
category.set('parent_Id', "28")
category_text = "На одного"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "171")
category.set('parent_Id', "28")
category_text = "На двоих"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "157")
category.set('parent_Id', "28")
category_text = "Комбо наборы"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "32")
category_text = "Напитки"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "159")
category.set('parent_Id', "35")
category_text = "Крафт бургеры"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "160")
category.set('parent_Id', "35")
category_text = "Классика"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "31")
category.set('parent_Id', "77")
category_text = "Десерты"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "29")
category.set('parent_Id', "78")
category_text = "Блюда на мангале"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "163")
category.set('parent_Id', "78")
category_text = "Шаверма"
category.text = category_text
categories.append(category)

category = ET.Element("category")
category.set('id', "164")
category.set('parent_Id', "78")
category_text = "Наборы (мангал)"
category.text = category_text
categories.append(category)

# ---------------------------/Категории---------------------------

offers = ET.Element("offers")
shop.append(offers)


def slow_scroll_down(driver):
    scroll_pause_time = 0.3  # set pause time
    screen_height = driver.execute_script("return window.screen.height;")  # get the screen height of the web
    i = 1

    while True:
        # scroll one screen height each time
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
        i += 1
        time.sleep(scroll_pause_time)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if screen_height * i > scroll_height:
            break


def get_last_digits_from_href(href):
    last_digits = href.split("-")[-1]

    if last_digits.endswith("/"):
        last_digits = last_digits[:-1]

    return last_digits


def scrape_website(url):
    try:
        driver = webdriver.Chrome()

        driver.get(url)

        slow_scroll_down(driver)

        html_content = driver.page_source

        soup = BeautifulSoup(html_content, 'html.parser')

        card_container = soup.find_all('div', {'class': 'card-container'})

        div_description = []
        produt_name = []
        links = []
        price = []
        img_links = []
        last_digits_list = []
        cat_slug = []

        for c in card_container:
            cards = c.find_all('a', {'class': 'card-box'}, href=True)
            for card in cards:
                div_description.append(card.find('div', {'class': 'col-lg-12 description'}))  # описание товара

                produt_name.append(card.find('div', {'class': 'product-title'}))  # название товара

                links_soup = card['href']
                links.append(links_soup)  # ссылка на товар

                price.append(card.find('div', {'class': 'product-price'})) # цена

                img = card.find('img')
                img_links.append(img['src'])  # ссылка на картинку

                last_digits_list.append([get_last_digits_from_href(links_soup)])  # айдишники

                cat_id = card.find('meta', {'itemprop': 'description'})
                cat_slug.append(cat_id['content'])

        return last_digits_list, produt_name, links, div_description, img_links, cat_slug, price

    except Exception as e:
        print(f"Ошибка: {e}")
        return None, None


if __name__ == "__main__":

    target_url = "https://fidele-food.ru/kerch"
    domain = "https://fidele-food.ru"
    menuallowed = "True"

    created_ids = {}

    last_digits_list, produt_name, links, div_description, img_links, cat_slug, price = scrape_website(target_url)

    if last_digits_list and produt_name and div_description and img_links and links and cat_slug:
        for lq, n, d, im, lks, c, p in zip(last_digits_list, produt_name, div_description, img_links, links, cat_slug, price):

            offer_id = None
            for numb in lq:
                offer_id = numb

            lq_tuple = tuple(lq)
            if lq_tuple in created_ids:
                continue

            offer = ET.Element("offer")
            offer.set('id', f"{offer_id}")
            offer.set('available', f"{menuallowed}")
            offers.append(offer)

            created_ids[lq_tuple] = True

            if n is not None:
                name_prod = n.text.strip()
                current_name = name_prod.replace('"', '')
                name_product = ET.Element("name")
                name_product.text = current_name
                offer.append(name_product)

            if d is not None:
                desc = d.text.strip()
                current_desc = desc.replace('"', '')
                current_description = current_desc.replace(':', '')
                c_description = current_description.replace('*', '')
                current_description_2 = " ".join(c_description.split())
                desc_product = ET.Element("description")
                desc_product.text = current_description_2
                offer.append(desc_product)

            image_links = im
            image_lnks = ET.Element("picture")
            image_lnks.text = image_links
            offer.append(image_lnks)

            links = lks
            lks_el = ET.Element("url")
            lks_el.text = domain + links
            offer.append(lks_el)

            price = p
            price_int = []
            for item in price:
                match = re.search(r'\d+', item)
                if match:
                    price_int.append(str(int(match.group())))
            numeric_values = ', '.join(price_int)  # массив в строку с разделителем
            p_price = ET.Element("price")
            p_price.text = numeric_values
            offer.append(p_price)

            currencys = ET.Element("currencyId")
            currencys.text = "RUR"
            offer.append(currencys)

            pickup = ET.Element("pickup")
            pickup.text = "false"
            offer.append(pickup)

            cat_slug = c
            if 'Пицца' in c:
                cat_id = "2"
            elif 'Паста' in c:
                cat_id = "4"
            elif 'Маки роллы' in c:
                cat_id = "6"
            elif 'Роллы' in c:
                cat_id = "7"
            elif 'Запечённые роллы' in c:
                cat_id = "8"
            elif 'Темпура' in c:
                cat_id = "9"
            elif 'Наборы' in c:
                cat_id = "10"
            elif 'Лапша WOK' in c:
                cat_id = "14"
            elif 'Супы' in c:
                cat_id = "16"
            elif 'Блины' in c:
                cat_id = "18"
            elif 'Завтраки' in c:
                cat_id = "18"
            elif 'Первые блюда' in c:
                cat_id = "20"
            elif 'Комбо обеды' in c:
                cat_id = "155"
            elif 'Салаты' in c:
                cat_id = "19"
            elif 'Вторые блюда' in c:
                cat_id = "21"
            elif 'Блюда на мангале' in c:
                cat_id = "29"
            elif 'Гарниры' in c:
                cat_id = "22"
            elif 'Закуски' in c:
                cat_id = "23"
            elif 'На одного' in c:
                cat_id = "170"
            elif 'На двоих' in c:
                cat_id = "171"
            elif 'Комбо наборы' in c:
                cat_id = "157"
            elif 'Крафт бургеры' in c:
                cat_id = "159"
            elif 'Классика' in c:
                cat_id = "160"
            elif 'Шаверма' in c:
                cat_id = "163"
            elif 'Наборы (мангал)' in c:
                cat_id = "164"
            elif 'Десерты' in c:
                cat_id = "31"
            elif 'Напитки' in c:
                cat_id = "32"
            else:
                cat_id = "999"

            category_id = ET.Element("categoryId")
            category_id.text = cat_id
            offer.append(category_id)

    tree = ET.ElementTree(yml_catalog)
    xml_string = ET.tostring(yml_catalog, encoding="utf-8")

    dom = minidom.parseString(xml_string)
    pretty_xml_string = dom.toprettyxml(indent="\t")

    with open("kerch.yml", "w") as file:
        file.write(pretty_xml_string)
