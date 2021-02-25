# 데이터 크롤링을 위한 패키지
import requests
# html에서 정보를 추출하기에 정말 유용한 패키지
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?as_and=python&limit={LIMIT}"


def extract_indeed_pages():
    # 1페이지
    result = requests.get(URL)
    # 한 페이지의 모든 데이터
    soup = BeautifulSoup(result.text, "html.parser")

    # 이 다음부터 원하는 데이터 다듬기
    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')
    pages = []

    # 마지막 'Next'는 무시 int변환하기 위해
    for link in links[:-1]:
        pages.append(int(link.string))

    # 마지막 페이지
    max_page = pages[-1]
    return max_page


# pages = pagination.find_all('a')
# spans = []

# for page in pages:
#   spans.append(page.find("span"))
# pages = spans[0:-1]
# print(pages)


# request 페이지 만드는 function
def extract_indeed_jobs(last_page):
    for page in range(last_page):
        # print(f"start={page*LIMIT}")
        # request 요청
        requests.get(f"{URL}&start={page*LIMIT}")
        # print(result.status_code) 200
