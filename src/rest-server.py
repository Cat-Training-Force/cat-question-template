#!flask/bin/python
from flask import Flask, jsonify, render_template, request
from flask_cors import cross_origin
from hashlib import sha256
from time import sleep

import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

PORT = 80
SECRET_LOCATION = '/chall/secret.txt'
ANSWER_HASH_LOCATION = '/chall/answer-hash'

flag = open(SECRET_LOCATION).read().strip()
logger.info(f'Readed flag: {flag}')

with open(ANSWER_HASH_LOCATION, 'r') as f:
    original_hash = f.read().strip()
logger.info(f'Readed hash: {original_hash}')

app = Flask(__name__, static_url_path="")

@app.route('/answer', methods=['POST'])
@cross_origin()
def answer():
    sleep(1)
    try:
        data = request.form.to_dict(flat=False)
        s = data['q1'][0] + data['q2'][0] + data['q3'][0] + \
            data['q4'][0] + data['q5'][0] + data['q6'][0]
        ans_hash = sha256(s.encode('utf-8')).hexdigest()
        print(s)
        print(ans_hash)
        assert ans_hash == original_hash
        ret = {
            "status": 0,
            "msg": flag,
        }
        return jsonify(ret)
    except:
        ret = {
            "status": 1,
            "msg": '答案不对喵～',
            # "msg": calc_sha256(str(data)),
        }
        return jsonify(ret)


@app.route("/")
def main():
    return render_template("main.html", port=PORT)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=str(PORT))
