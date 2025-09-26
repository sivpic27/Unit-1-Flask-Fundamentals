from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    return f'''<h2>Query Parameters </h2>
    <ul>
        <li>Searching:
            <ul>
                <li><a href="/search?q=python&page=2">/search?q=python&page=2</a></li>
                <li><a href="/search?q=python&page=2">/search?q=python&page=2</a></li>
            </ul>
        </li>
        <li>Products:
            <ul>
                <li><a href="/products">/products</a></li>
                <li><a href="/products?q=python&page=3">/products?q=python&page=3</a></li>
            </ul>
        </li>
    </ul>
    '''

@app.route('/search')
def search():
    query = request.args.get('q', 'Nothing!')
    page = request.args.get('page', '1')
    return f"Searching for: '{query}' on page{page}"


@app.route('/products')
def products():
    page = request.args.get('page', 1, type=int)
    price = request.args.get("max_price", type=float)
    return escape(f"Page:{page} (Type:{type(page)}), Max Price: {price} (type: {type(price)})")



if __name__ == '__main__':
    app.run(debug=True)