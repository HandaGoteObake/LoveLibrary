import TkEasyGUI as eg
import toml
import os
import shutil

def add_book_window():
    layout = [
        [eg.Text("書籍名:"), eg.InputText(key="-BOOK_NAME-")],
        [eg.Text("画像:"), eg.FileBrowse(key="-IMAGE-")],
        [eg.Text("棚番号:"), eg.InputText(key="-SHELF-")],
        [eg.Button("保存"), eg.Button("キャンセル")],
    ]

    window = eg.Window("書籍の追加", layout)

    while True:
        event, values = window.read()

        if event == "保存":
            book_name = values["-BOOK_NAME-"]
            print(values)
            image_path = values["-IMAGE-"]
            shelf = values["-SHELF-"]

            if not book_name or not image_path or not shelf:
                eg.popup_error("すべての項目を入力してください。")
                continue

            # 画像ファイルをData/imgフォルダにコピー
            img_filename = os.path.basename(image_path)
            new_image_path = os.path.join("Data", "img", img_filename)
            shutil.copy(image_path, new_image_path)

            # tomlファイルに保存
            book_data = {
                "書籍名": book_name,
                "画像": new_image_path,
                "棚番号": shelf,
            }

            try:
                with open("books.toml", "a", encoding="utf-8") as f:
                    toml.dump({book_name: book_data}, f)
                eg.popup("保存しました。")
            except Exception as e:
                eg.popup_error(f"保存に失敗しました: {e}")

            break
        elif event == "キャンセル" or event == eg.WIN_CLOSED:
            break

    window.close()