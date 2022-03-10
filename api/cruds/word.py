from spreadsheet import sheet

# テスト単語一覧取得
def getAllBooks():
    book_name_list_of_list = sheet.get("C2:C")
    book_names = list(map(lambda book_name_list: book_name_list[0], book_name_list_of_list))
    filtered_book_names = list(set(book_names))
    return filtered_book_names

# テスト単語一覧取得
def getTestWords(book_name: str, first: int, last: int):
    list_of_dicts = sheet.get_all_records()
    filtered_list = list(filter(lambda i: i["book_name"] == book_name and first <= i["word_num"] <= last , list_of_dicts))
    return filtered_list