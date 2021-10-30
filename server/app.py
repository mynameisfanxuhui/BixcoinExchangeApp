from flask import Flask, jsonify
import show_data

app = Flask(__name__)



@app.route('/')
def index():
    return 'Hello, world'

@app.route('/data')
def data():
    dataList = show_data.showData()
    return jsonify(dataList)



if __name__ == '__main__':
    app.run(debug=True)