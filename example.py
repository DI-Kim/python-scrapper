import requests

from bs4 import BeautifulSoup

all_jobs  = []

def scrape_page(url):
  print(f'scraping {url}...')
  response = requests.get(url)

  soup = BeautifulSoup(response.content, "html.parser")

  jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

  for job in jobs:
    title = job.find("span", class_='title')
    company, position, region = job.find_all('span', class_='company')
    url = job.find('div', class_='tooltip--flag-logo').next_sibling['href']

    job_data = {
      "title": title.text,
      "company": company.text,
      "position": position.text,
      "region": region.text,
      'url': f'https://weworkremotely.com{url}'
    }
    all_jobs.append(job_data)

def get_pages(url):
  response = requests.get(url, headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"})

  soup = BeautifulSoup(response.content, 'html.parser')

  # return page numbers of url
  return len(soup.find('div', class_='pagination').find_all('span', class_='page'))



# url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"
# scrape_page(url)

url = "https://weworkremotely.com/remote-full-time-jobs?page=1"    

total_pages = get_pages(url)

for x in range(total_pages):
  url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
  scrape_page(url)

print(len(all_jobs))