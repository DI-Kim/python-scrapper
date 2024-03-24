import requests
from bs4 import BeautifulSoup

# scraping function
# company, title, desc, link, skills
def scrape_page(url):
  all_jobs = []
  print(f'scraping {url}...')
  response = requests.get(url,
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
  )
  soup = BeautifulSoup(response.content, 'html.parser')
  if soup.find('ul', class_='jobs-list-items'):
    jobs = soup.find('ul', class_='jobs-list-items').find_all('li', class_='bjs-jlid')
  

    for job in jobs:
      company = job.find('a', class_='bjs-jlid__b')
      link_html = job.find('h4', class_='bjs-jlid__h').find('a')
      tags = []
      tags_html = job.find('div', class_='links-box').find_all('a')
      for tag in tags_html:
        tags.append(tag.text.strip())

      job_data = {
        'company': company.text,
        'title': link_html.text,
        'link': link_html['href'],
        'tags': tags,
      }

      all_jobs.append(job_data)
  # print(type(tags))
  print('finished...✅')
  return all_jobs

#scraping skill pages
def extractor_berlin(keyword):
  url = f'https://berlinstartupjobs.com/skill-areas/{keyword}/'
  return scrape_page(url)