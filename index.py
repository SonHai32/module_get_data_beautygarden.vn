from selenium import webdriver
import time
import json
driver = webdriver.Chrome()

driver.get('https://beautygarden.vn/danh-muc/sua-rua-mat.html?page=2')

time.sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/button[1]').click()
time.sleep(1)

product_list_container = driver.find_elements_by_class_name('pd-box')
product_link_list = []
product_list = []

with open('product_data.json', 'r') as file:
    product_list= list(json.load(file))
for item in product_list_container: 
    product_link_list.append(item.find_element_by_tag_name('a').get_attribute('href'))


def get_data_from_page(page_url):
    driver.get(page_url)


    try:
        prd_cat = {
            "cat_id": "sua-rua-mat", 
            "cat_text": "Sữa rửa mặt", 
            "parent_cat": {
                "cat_id": "cham-soc-da", 
                "cat_text": "Chăm Sóc Da"}}
        prd_name = driver.find_element_by_class_name('title-Product').text
        prd_price = driver.find_element_by_class_name('price-drop').find_elements_by_tag_name('span')[0].text
        prd_old_price = driver.find_element_by_class_name('price-vince').find_elements_by_tag_name('span')[0].text
        prd_discount = driver.find_element_by_class_name('price-vince').find_elements_by_tag_name('span')[2].text
        prd_rating = driver.find_element_by_class_name('text-rating').find_elements_by_tag_name('span')[0].text
        prd_color = []
        prd_img_url = []
        
        img_container = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div[1]/div[1]/div/div[1]/div/div[2]/div/div[1]').find_elements_by_tag_name('a')
        for item_img in img_container:
            prd_img_url.append(item_img.get_attribute('href'))

        try:
            color_select_items = driver.find_element_by_class_name('select-land').find_elements_by_tag_name('li')
            for item in color_select_items:
                item_color_hex = item.find_element_by_tag_name('a').get_attribute('style')
                prd_color.append(item_color_hex.split(':')[1].split(';')[0])
        except:
            print()
    except: 
        return

    

    prd_info_obj = {
        "product_name": prd_name, 
        "product_price": prd_price, 
        "product_old_price": prd_old_price, 
        "product_discount": prd_discount, 
        "product_rating": prd_rating, 
        "product_colors": prd_color, 
        "product_cat": prd_cat,
        "product_img_urls": prd_img_url
        }
    #prd_info_json = json.dumps(prd_info_obj, ensure_ascii=False).encode('utf8')
    return prd_info_obj 

for item in product_link_list:
    product_list.append(get_data_from_page(item))

product_list_obj = json.dumps(product_list, ensure_ascii=False).encode('utf8')

with open('product_data.json', 'w') as file:
    json.dump(product_list, file)

driver.close()

