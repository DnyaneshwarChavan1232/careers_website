from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'Location': 'Bengaluru, India',
    'Salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'Location': 'Delhi, India',
}, {
    'id': 3,
    'title': 'Backend Engineer',
    'Location': 'San Francisco, USA',
    'Salary': '$ 120,000'
}]


@app.route("/")
def hello():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
