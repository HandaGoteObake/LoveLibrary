import TkEasyGUI as eg
import toml
import os
import shutil

def edit_book_window():
    try:
        with open("books.toml", "r", encoding="utf-8") as f:
            books = toml.load(f)
    except FileNotFoundError:
        books = {}

    book_names = list(books.keys())
    if not book_names:
        eg.popup("書籍が登録されていません。")
        return

    layout = [
        [eg.Text("編集する書籍を選択してください:")],
        [eg.Combo(book_names, key="-BOOK_SELECT-")],
        [eg.Button("編集"), eg.Button("キャンセル")],
    ]

    window = eg.Window("書籍の編集", layout)

    while True:
        event, values = window.read()

        if event == "編集":
            selected_book = values["-BOOK_SELECT-"]
            edit_book_details(selected_book, books)
            break
        elif event == "キャンセル" or event == eg.WIN_CLOSED:
            break

    window.close()

def edit_book_details(book_name, books):
    book_data = books[book_name]

    layout = [
        [eg.Text("書籍名:"), eg.InputText(default_text=book_name, key="-BOOK_NAME-")],
        [eg.Text("画像:"), eg.FileBrowse(default_path=book_data["画像"], key="-IMAGE-")],
        [eg.Text("棚番号:"), eg.InputText(default_text=book_data["棚番号"], key="-SHELF-")],
        [eg.Button("保存"), eg.Button("キャンセル")],
    ]

    window = eg.Window("書籍の編集", layout)

    while True:
        event, values = window.read()

        if event == "保存":
            new_book_name = values["-BOOK_NAME-"]
            image_path = values["-IMAGE-"]
            shelf = values["-SHELF-"]

            if not new_book_name or not image_path or not shelf:
                eg.popup_error("すべての項目を入力してください。")
                continue

            # 画像ファイルをData/imgフォルダにコピー
            img_filename = os.path.basename(image_path)
            new_image_path = os.path.join("Data", "img", img_filename)
            shutil.copy(image_path, new_image_path)

            # tomlファイルを更新
            updated_book_data = {
                "書籍名": new_book_name,
                "画像": new_image_path,
                "棚番号": shelf,
            }

            if new_book_name != book_name:
                del books[book_name]
            books[new_book_name] = updated_book_data

            try:
                with open("books.toml", "w", encoding="utf-8") as f:
                    toml.dump(books, f)
                eg.popup("保存しました。")
            except Exception as e:
                eg.popup_error(f"保存に失敗しました: {e}")

            break
        elif event == "キャンセル" or event == eg.WIN_CLOSED:
            break

    window.close()