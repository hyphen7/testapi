from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
  return jsonify({
    "message": "テスト!!"
  })
@app.route('/home')
def home():
  return jsonify({
    "message": "家に帰りましょう!!"
  })

if __name__ == '__main__':
  app.run()
