# 데이터 크롤링을 위한 패키지
import requests
# html에서 정보를 추출하기에 정말 유용한 패키지
from bs4 import BeautifulSoup


LIMIT = 50
URL = f"https://www.indeed.com/jobs?as_and=python&limit={LIMIT}"


def get_last_pages():
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


def extract_job(html):
    # title
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    # company
    company = html.find("span", {"class": "company"})

    # company에 a태그가 있는 곳 & 없는 곳 존재...
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    company = company.strip()  # 빈칸 없애기

    # location - div안에 있는 attr에 접근
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    # job_id
    job_id = html["data-jk"]

    return {
        'title': title,
        'company': company,
        'location': location,
        'link': f"https://www.indeed.com/viewjob?jk={job_id}"
    }


# request 페이지 만드는 function
def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping Indeed: Page {page}")
        result = requests.get(f"{URL}&start={0*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})

        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_pages()
    jobs = extract_jobs(last_page)
    return jobs
