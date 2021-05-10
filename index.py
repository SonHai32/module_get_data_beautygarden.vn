from selenium import webdriver
import time

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

    color_select_items = driver.find_element_by_class_name('select-land').find_elements_by_tag_name('li')


    for item in color_select_items:
        item_color_hex = item.find_element_by_tag_name('a').get_attribute('style')
        print(item_color_hex)

    print(prd_name, prd_price, prd_old_price, prd_discount)

get_data_from_page(product_link_list[0])

driver.close()