import os
import xml.etree.ElementTree as ET

# Список имен файлов
file_names = ["simf.yml", "sev.yml", "yalta.yml", "feo.yml", "kerch.yml", "evp.yml"]


# Функция для удаления offer с categoryId равным 999
def remove_offers_with_category_id_999(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Ищем все offer с categoryId равным 999 и удаляем их из списка offers
    offers = root.find(".//offers")
    if offers is not None:
        for offer in offers.findall("offer"):
            category_id_elem = offer.find("categoryId")
            if category_id_elem is not None and category_id_elem.text == "999":
                offers.remove(offer)

    # Сохраняем изменения обратно в файл
    tree.write(file_path, encoding="utf-8", xml_declaration=True)


# Проходим по каждому файлу и удаляем offer с categoryId равным 999
for file_name in file_names:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    remove_offers_with_category_id_999(file_path)
