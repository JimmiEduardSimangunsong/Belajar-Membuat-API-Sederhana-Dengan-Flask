from flask import Blueprint, jsonify, request
from controllers import BookController

book_api = Blueprint('book_api', __name__)
# Pada kode diatas, kita membuat blueprint dengan nama 'book_api' dan __name__ sebagai nama modul
# . 'book_api' akan digunakan sebagai awalan URL untuk semua endpoint yang ada di blueprint ini.

@book_api.route('/books', methods=['GET'])
def get_all_books():
    return jsonify(BookController.get_all())

@book_api.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    book = BookController.get_by_id(id)
    if book:
        return jsonify(book)
    else:
        return jsonify({'message': 'Book not found'}), 404

@book_api.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    book = BookController.create(data)
    return jsonify(book.to_dict()), 201

@book_api.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = BookController.get_by_id(id)
    if book:
        data = request.get_json()
        book.update(data)
        return jsonify(book.to_dict())
    else:
        return jsonify({'message': 'Book not found'}), 404

@book_api.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = BookController.get_by_id(id)
    if book:
        book.delete()
        return '', 204
    else:
        return jsonify({'message': 'Book not found'}), 404
