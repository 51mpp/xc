from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/getcode', methods=['GET'])
def get_code():
    return jsonify({'code': 200}), 200
@app.route('/plus/<a>/<b>', methods=['GET'])
def plus(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return jsonify({'message': 'Invalid input'}), 400
    return jsonify({'result': a + b}), 200
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)