from flask import Flask, request, jsonify

app = Flask(__name__)

offensive_words = [
    "মাগি", "চুদি", "গুদ", "চুদ", "মা চুদি", "বোদা", "মাদার", "মাদারবোর্ড", "ফাক", "নেকেড", "sex", "rape"
]

def check_for_abuse(message):
    message = message.lower()
    found = [word for word in offensive_words if word in message]
    return found

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    message = data.get("message", "")
    found = check_for_abuse(message)

    if found:
        return jsonify({"status": "offensive", "words": found})
    else:
        return jsonify({"status": "clean"})

@app.route('/', methods=['GET'])
def home():
    return "Anti-Abuse Bot is Running!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)