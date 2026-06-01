#Import the required libraries

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from tqdm import tqdm

website_url = "https://anycallmobilemm.com/product-category/smartphone/"

def create_page_urls(main_url):
    """Create web page urls from the website url."""
    web_data = requests.get(main_url).text
    bsObj = BeautifulSoup(web_data, "html.parser")
    # Create web page urls
    # Find Max Page Number
    max_page_num = int(bsObj.find_all("a", "page-numbers")[-2].text)
    page_url_list = []
    page_url_list.append(website_url)
    for i in range(2, max_page_num+1):
        page_url = main_url + "page/" + str(i)
        page_url_list.append(page_url)
    return page_url_list


def extract_p_info_tags(url):
    """Finding the product info tags"""
    response = requests.get(url)
    web_data = response.text
    bsObj = BeautifulSoup(web_data,"html5lib")
    product_info_tags_list = bsObj.find_all("div","product-wrapper")
    return product_info_tags_list

def extract_p_name(product_info_tags_list):
    """Finding the product name"""
    product_name_list = []
    for product_info_tag in product_info_tags_list:
        p_name_tag = product_info_tag.find("h3", "wd-entities-title")
        p_name = p_name_tag.text
        product_name_list.append(p_name)
    return product_name_list



def extract_smart_phone_brand(product_name_list):
    """Finding what is the smart phone brand"""
    brand_list= []
    existing_brand_list = ["Samsung", "Huawei", "Tecno", "Vivo", "Oppo", "Realme", "Honor", "Mi", "Xiaomi", "Redmi", "Oneplus", "Infinix", "Itel", "Nubia", "Meizu", "Poco"]
    
    for each_product_name in product_name_list:
        found_brand = None 
        name_lower = each_product_name.lower()
        
        for each_brand in existing_brand_list:
            if name_lower.startswith(each_brand.lower()):
                if each_brand.lower() in ["redmi", "xiaomi", "mi"]:
                    found_brand = "Mi"
                else:
                    found_brand = each_brand
                
        brand_list.append(found_brand)
        
    return brand_list


def extract_p_price(product_info_tags_list):
    """Finding the product price"""
    product_price_list = []
    for product_info_tag in product_info_tags_list:
        p_price_tag = product_info_tag.find("span", "woocommerce-Price-amount amount")
        p_price = p_price_tag.text
        p_price = p_price.replace("\xa0Ks","")
        p_price = p_price.replace(",","")
        product_price_list.append(int(p_price))   
    return product_price_list

def get_current_dt():
    #"""Finding the current data time """
    current_dt = datetime.now()
    current_dt = str(current_dt)
    current_dt = current_dt.replace(":","-")
    current_dt = current_dt.split(".")[0] 
    return current_dt   
    
##################### Main Programe ###########################

def main():
    
    #In here, we create a list of url from the website_url 
    web_url_list = create_page_urls(website_url)

    #Find the product info tags, product name and product price
    url_count = 0
    final_df = pd.DataFrame()
    
    #web_url contains web pages as list so we must use for loop to extract the product information from each of the web page. 

    for each_url in tqdm(web_url_list):
        
        #In here, we will get a list of product information tags from every web page.
        p_info_tags_list = extract_p_info_tags(each_url)
        
        #Using each of the product info tag, we will find the product name, prodcut brand, and price of every product information.
        product_name = extract_p_name(p_info_tags_list)
        product_price = extract_p_price(p_info_tags_list)
        product_brand = extract_smart_phone_brand(product_name)
        
        #Here, we create the data frame from panda library to create the data tables for each of the web page.
        page_df= pd.DataFrame({"Name": product_name,
                               "Price" : product_price,
                               "Brand" : product_brand})
        
        url_count+=1
        current_dt = get_current_dt()
        
        #This will make excel files for each of the web page with each web page name and time created.
        page_df.to_excel(f"Final Capstone Project Batch 4 {url_count} {current_dt}.xlsx", index= False)
        
        #Creating the final data excel file from each of the web page excel file.
        final_df = pd.concat([final_df,page_df])
        final_df.to_excel("Final Data.xlsx", index=False)
        
        
print("The project is completed successfully.")

if __name__=="__main__":
    main()