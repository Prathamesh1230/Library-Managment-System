import os
import pickle

def save_books(books):
    with open("books.dat", "wb") as f:
        pickle.dump(books, f)

def load_books():
    if not os.path.exists("books.dat"):
        return []
    with open("books.dat", "rb") as f:
        return pickle.load(f)
