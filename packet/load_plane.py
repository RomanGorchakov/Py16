def load_plane(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)