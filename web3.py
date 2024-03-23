import requests
from bs4 import BeautifulSoup

# company: td.job-location-mobile > a > h3.text
# title: div.job-title-mobile > a > h2.text
# link: td.job-location-mobile > a:href
# tags: tr.table_row > td:nth-child(6) > span

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
  jobs_all = soup.find('tbody', class_='tbody')
  for _ in jobs_all:
    if jobs_all.find('tr', class_='border-paid-table') is None:
      break
    jobs_all.find('tr', class_='border-paid-table').decompose()
  jobs = jobs_all.find_all('tr', class_='table_row')
  

  for job in jobs:
    company = job.find('td', class_='job-location-mobile').find('h3')
    title = job.find('div', class_='job-title-mobile').find('h2')
    link = job.find('td', class_='job-location-mobile').find('a')['href']
    tags = []
    tags_html = job.find_all('span', class_='my-badge')
    for tag in tags_html:
      tags.append(tag.text.strip())

    job_data = {
      'company': company.text,
      'title': title.text,
      'link': f'https://web3.career{link}',
      'tags': tags,
    }

    all_jobs.append(job_data)
  print('finished...✅')
  return all_jobs

#scraping skill pages
def extractor_web3(keyword):
  url = f'https://web3.career/{keyword}-jobs'
  return scrape_page(url)
