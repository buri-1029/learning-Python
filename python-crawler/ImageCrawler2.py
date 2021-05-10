from selenium import webdriver
from bs4 import BeautifulSoup as soups


def search_selenium(search_name, search_path):
    search_url = "https://www.google.com/search?q=" + \
        str(search_name) + "&hl=ko&tbm=isch"

    browser = webdriver.Chrome()
    browser.get(search_url)

    image_count = len(browser.find_elements_by_tag_name("img"))

    print("로드된 이미지 개수 : ", image_count)

    browser.implicitly_wait(2)

    for i in range(image_count):
        image = browser.find_elements_by_tag_name("img")[i]
        image.screenshot("./train/Heteropanax fragrans/" +
                         "plant" + i + ".png")

    browser.close()


if __name__ == "__main__":

    search_name = "해피트리"
    search_path = "./train/Heteropanax fragrans"
    search_selenium(search_name, search_path)
