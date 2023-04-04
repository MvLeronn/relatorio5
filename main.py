from database import Database
from model import BookModel
from save_json import writeAJson

db = Database(database="relatorio5", collection="Livros")
db.resetDatabase()

book_model = BookModel(db)

book_id = book_model.create_book("1","Moby Dick","Herman Melville",1851,25.0)

livro = book_model.read_book_by_id(book_id)

book_model.update_book(book_id,"Moby Dick","Herman Melville",1851,50)

book_model.delete_book(book_id)

book_model.read_book_by_id(book_id)