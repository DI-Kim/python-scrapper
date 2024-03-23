from flask import Flask, render_template, request
from berlin import extractor_berlin
from web3 import extractor_web3

app = Flask(__name__)

# fake database
db = {
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
    berlin = extractor_berlin(keyword)
    web3 = extractor_web3(keyword)
    jobs = berlin + web3
    db[keyword] = jobs
  return render_template('search.html', keyword=keyword, jobs=jobs)

if __name__ == "__main__":
  app.run("127.0.0.1", port=8000, debug=True)