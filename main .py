from flask import Flask, render_template, request

app = Flask("JobScrapper")

# fake database
db = {
  'react': [{'company': 'TELUS International AI',
            'title': 'Fully Remote: Data Analyst (Anywhere in Germany)',
            'link': 'https://berlinstartupjobs.com/engineering/fully-remote-data-analyst-anywhere-in-germany-telus-international-ai/',
            'skills': ['Freelancer', 'Part Time', 'remote', 'Studenten', 'Working Students'],
            },]
}

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/search")
def search():
  keyword = request.args.get('keyword')
  if keyword in db:
    jobs = db[keyword]
  else:
    jobs = [
            {'company': 'TELUS International AI',
            'title': 'Fully Remote: Data Analyst (Anywhere in Germany)',
            'link': 'https://berlinstartupjobs.com/engineering/fully-remote-data-analyst-anywhere-in-germany-telus-international-ai/',
            'skills': ['Freelancer', 'Part Time', 'remote', 'Studenten', 'Working Students'],
            },
            {'company': 'TELUS AI',
            'title': 'Data Analyst (Anywhere)',
            'link': 'https://berlinstartupjobs.com/engineering/fully-remote-data-analyst-anywhere-in-germany-telus-international-ai/',
            'skills': ['Freelancer', 'Studenten', 'Working Students'],
            }       
            ]
  return render_template('search.html', keyword=keyword, jobs=jobs)

app.run("127.0.0.1", port=8000, debug=True)