from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diary', methods=['POST'])
def diary():
    mood = request.form['mood']
    event = request.form['event']
    gratitude = request.form['gratitude']
    summary = summarize(mood, event, gratitude)
    return render_template('result.html', summary=summary)

def summarize(mood, event, gratitude):
    return f"오늘 당신은 '{mood}' 기분이었고, 이런 일이 있었습니다: '{event}'. 감사한 일은 '{gratitude}'였네요."

if __name__ == '__main__':
    app.run(debug=True)
