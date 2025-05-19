from flask import Flask, request, jsonify

app = Flask(__name__)

stories = []

@app.route('/stories', methods=['GET'])
def get_stories():
    return jsonify(stories)

@app.route('/stories', methods=['POST'])
def add_story():
    data = request.json
    if 'story' in data:
        stories.append(data['story'])
        return jsonify({'message': 'Hikaye eklendi!'}), 201
    return jsonify({'error': 'Hikaye bulunamadı!'}), 400

if __name__ == '__main__':
    app.run(debug=True)
