from flask import Flask, render_template, request
from googlesearch import search


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
# def perform_search():
def search():
    search_query = request.args.get('q', '')
    results = list(search(search_query, num=10, stop=10))

# for result in search(search_query, num=10):
# results.append(result)
    return f'Google search results: {results}'


if __name__ == '__main__':
    app.run(debug=True)
