from flask import flask

app = flask(__name__)

@app.route('/')
def home():
  return '<hl>Hello World!</hl>'

if __name__ == '__main__':
  app.run()