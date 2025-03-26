import TkEasyGUI as eg
import display.add_book as add_book
import display.view_books as view_books
import display.edit_book as edit_book

def main():
    layout = [
        [eg.Button("書籍の追加", key="-ADD-"), eg.Button("書籍一覧", key="-VIEW-"), eg.Button("書籍の編集", key="-EDIT-")],
        [eg.Button("終了", key="-EXIT-")],
    ]

    window = eg.Window("書籍管理ツール", layout, size=(800, 600))

    while True:
        event, values = window.read()

        if event == "-ADD-":
            add_book.add_book_window()
            
        elif event == "-VIEW-":
            view_books.view_books_window()
        elif event == "-EDIT-":
            edit_book.edit_book_window()
        elif event == "-EXIT-" or event == eg.WIN_CLOSED:
            break

    window.close()

if __name__ == "__main__":
    main()