import TkEasyGUI as eg
import toml

def view_books_window():
    try:
        with open("books.toml", "r", encoding="utf-8") as f:
            books = toml.load(f)
    except FileNotFoundError:
        books = {}

    layout = [[eg.Text("書籍一覧")]]
    for book_name, book_data in books.items():
        layout.append([eg.Text(f"書籍名: {book_name}, 棚番号: {book_data['棚番号']}")])

    layout.append([eg.Button("閉じる")])

    window = eg.Window("書籍一覧", layout)

    while True:
        event, values = window.read()
        if event == "閉じる" or event == eg.WIN_CLOSED:
            break

    window.close()