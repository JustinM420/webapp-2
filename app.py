from flask import Flask, render_template, jsonify, request


app = Flask (__name__)

STRAINS = [
  {
    'id':1,
    'title': 'White Widow',
    'type': 'Indica',
    'effects': 'sedative'
  },
  {
    'id':2,
    'title': 'Grand Daddy Purp (GDP)',
    'type': 'Indica',
    'effects': 'sedative'
  },
{
    'id':3,
    'title': 'OG',
    'type': 'Indica',
    'effects': 'sedative'
  },
{
    'id':4,
    'title': 'Gelato 41',
    'type': 'Indica',
    'effects': 'sedative'
  }
]


  

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         strains=STRAINS)

  @app.route("/api/strains")
  def list_strains():
    return jsonify(STRAINS)







if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
