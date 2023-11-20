# ParrishScott_M04apiLab.py     Scott Parrish   SDEV 220    11/19/2023  V: 0.1
# A Flask CRUD API for a database of books with attributes:
# id: number generated by thed database
# book_name: user submitted book title
# author: user submitted book author
# publisher: user submitted book publisher
# / shows a message welcoming the user and linking to the /books page
# each entry has a dict with 4 kv pairs in json format
# {
# 		"book:
#			{
#				"id": int (PK),
#				"author": string(80), 
#				"book_name": string(80),
#				"publisher": string(80)
#			}
# }


from flask import Flask
from flask import request       # Code from tutorial would not work without importing request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.app_context()
db = SQLAlchemy(app)

class Book(db.Model):
    """Book class to store the book information"""
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80))       # consider increasing size of author and publisher fields
    publisher = db.Column(db.String(80))

    def __repr__(self):
        return f'{self.id}: {self.book_name} - {self.author} - {self.publisher}'

@app.route('/')
def index():
	"""Default route displays message with link to /books"""
    return 'Hello!  You will find the books in the <a href="/books">Books page.</a>'

@app.route('/books')
def get_books():
    """Returns a list of books in the database"""
    books = Book.query.all()    
    output = []                 # list to hold book entries from database
    for book in books:          # go through each record and append the data to the output list
        book_data = {'book_name': book.book_name, 'author': book.author, 'publisher': \
                     book.publisher}
        output.append(book_data)

    return {"books": output}

@app.route('/books/<id>', methods=['GET'])
def get_book(id):
	"""returns single book entry by id"""
    book = Book.query.get_or_404(id)  # if the book id doesnt exist gives 404 error
    return {'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}

@app.route('/books', methods=['POST'])
def add_book():
    """Adds a new book to the database using data submitted using POST request json payload"""
    book = Book(book_name=request.json['book_name'], author=request.json['author'], \
                publisher= request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {"id": book.id}

@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    """Update book record in the database if it exists, if not return an error message. 
    if no json data is submitted the server will give a 415 error."""
    book = Book.query.get(id)
    book_data = request.get_json()      # set book data to the json payload
    print(book_data)
    if book is None:
        return {"error": "Book not found"}
    if 'book_name' in book_data:                     # update book book_name
        book.book_name = book_data['book_name']
    elif 'author' in book_data:
        book.author = book_data['author']       # update author
    elif 'publisher' in book_data:
        book.publisher = book_data['publisher'] # update publisher
    else:
        return {"message": "no updates"}        # json data did not have book_name, author or publisher keys
    
    db.session.commit()
    return {"message": "Book updated"}

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    """Delete book record from the database at <id> if it exists, if not return an error message."""
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)             # Delete the record
    db.session.commit()
    return {"message": "deleted"}

if __book_name__ == '__main__':
    app.run(debug=True)
