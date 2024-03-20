import requests
from bs4 import BeautifulSoup

all_jobs = []

response = requests.get(
    "https://berlinstartupjobs.com/engineering/",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
)

soup = BeautifulSoup(response.content, 'html.parser')

# total pages of engineering url
total_pages = len(soup.find('ul', class_='bsj-nav').find_all('a'))

# scraping function
# company, title, desc, link, skills
def scrape_page(url):
  print(f'scraping {url}...')
  response = requests.get(url,
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
  )
  soup = BeautifulSoup(response.content, 'html.parser')
  jobs = soup.find('ul', class_='jobs-list-items').find_all('li', class_='bjs-jlid')

  for job in jobs:
    company = job.find('a', class_='bjs-jlid__b')
    link_html = job.find('h4', class_='bjs-jlid__h').find('a')
    desc = job.find('div', class_='bjs-jlid__description')
    skills = []
    skills_html = job.find('div', class_='links-box').find_all('a')
    for skill in skills_html:
      skills.append(skill.text.strip())

    job_data = {
      'company': company.text,
      'title': link_html.text,
      'link': link_html['href'],
      'skills': skills,
      'desc': " ".join(desc.text.split())
    }

    all_jobs.append(job_data)
  print('finished...✅')

# scraping all pages
for page in range(total_pages):
  url = f"https://berlinstartupjobs.com/engineering/page/{page+1}/"
  scrape_page(url)  

skills = [
    "python",
    "typescript",
    "javascript",
    "rust"
]

#scraping skill pages
for skill in skills:
  url = f'https://berlinstartupjobs.com/skill-areas/{skill}/'
  scrape_page(url)

print(len(all_jobs))


