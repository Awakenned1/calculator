from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        try:
            expression = request.json['expression']
            result = eval(expression)
            return jsonify({'result': result})
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
