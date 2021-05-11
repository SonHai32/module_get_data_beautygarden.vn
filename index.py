from selenium import webdriver
import time
import json
driver = webdriver.Chrome()

driver.get('https://beautygarden.vn/danh-muc/khuon-mat.html')

product_list_container = driver.find_elements_by_class_name('pd-box')
product_link_list = []
for item in product_list_container: 
    product_link_list.append(item.find_element_by_tag_name('a').get_attribute('href'))


def get_data_from_page(page_url):
    driver.get(page_url)
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/button[1]').click()

    time.sleep(1)

    prd_name = driver.find_element_by_class_name('title-Product').text
    prd_price = driver.find_element_by_class_name('price-drop').find_elements_by_tag_name('span')[0].text
    prd_old_price = driver.find_element_by_class_name('price-vince').find_elements_by_tag_name('span')[0].text
    prd_discount = driver.find_element_by_class_name('price-vince').find_elements_by_tag_name('span')[2].text
    prd_rating = driver.find_element_by_class_name('text-rating').find_elements_by_tag_name('span')[0].text
    prd_cat = {"cat_id": "phan-ma-hong", "cat_text": "Phấn má hồng", "parent_cat": {"cat_id": "trang-diem", "cat_text": "Trang Điểm"}}

    color_select_items = driver.find_element_by_class_name('select-land').find_elements_by_tag_name('li')
    prd_color = []

    for item in color_select_items:
        item_color_hex = item.find_element_by_tag_name('a').get_attribute('style')
        prd_color.append(item_color_hex.split(':')[1].split(';')[0])

    prd_info_obj = {"product_name": prd_name, "product_price": prd_price, "product_old_price": prd_old_price, "product_discount": prd_discount, "product_rating": prd_rating, "product_colors": prd_color, "product_cat": prd_cat}
    #prd_info_json = json.dumps(prd_info_obj, ensure_ascii=False).encode('utf8')
    return prd_info_obj 


get_data_from_page(product_link_list[0])

driver.close()