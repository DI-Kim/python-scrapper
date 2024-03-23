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
  jobs_all = soup.find('div', class_='row')
  for _ in jobs_all:
    if jobs_all.find('li', class_='view-all') is None:
      break
    jobs_all.find('li', class_='view-all').decompose()
  jobs = jobs_all.find_all('li')

  for job in jobs:
    company, position, tags = job.find_all('span', class_='company')
    tags = [position.text] + tags.text.split('/')
    title = job.find('span', class_='title')
    link_html = job.find('div', class_='tooltip--flag-logo').next_sibling['href']

    job_data = {
      'company': company.text,
      'title': title.text,
      'link': f'https://weworkremotely.com{link_html}',
      'tags': tags,
    }

    all_jobs.append(job_data)
  print('finished...✅')
  return all_jobs

#scraping skill pages
def extractor_wwr(keyword):
  url = f'https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={keyword}'
  return scrape_page(url)
