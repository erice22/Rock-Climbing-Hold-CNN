from bs4 import BeautifulSoup
import requests
import shutil

def scrape(tag_name, class_name, base_url, url_addin = ""):
    hold_types = ["edges", "jugs", "pinches", "pockets", "slopers", "crimps"]
    for hold in hold_types:
        url = base_url + hold
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        tags = soup.find_all(tag_name, class_= class_name)
        image_info = []
        for tag in tags:
            image_tag = tag.findChildren("img")
            image_info.append((url_addin + image_tag[0]["src"], image_tag[0]["alt"]))
        for i in range(0, len(image_info)):
            download_image(image_info[i], hold)

def download_image(image, hold):
    response = requests.get(image[0], stream=True)
    realname = ''.join(e for e in image[1] if e.isalnum())
    folder = "/Users/moresauce/Desktop/Cs360/cs360-project-erice22/scraped_data/" + hold
    file = open(folder + "/{}.jpg".format(realname), 'wb')
    
    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, file)
    del response
        
def main():
    scrape("div","product-card__image-wrapper", "https://rockcandyholds.com/collections/holds-by-type/", "http:")
    scrape("span", "et_shop_image", "https://eldowalls.com/product-tag/")
    

main()
