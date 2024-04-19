import json

from vm4dpy.parse_text import parse_text
from vm4dpy.render_view import generate_views, write_views_to_file

def main(file: str, output: str):
    with open(file, encoding="UTF-8") as f:
        text = f.read()
    
    views = parse_text(text)

    
    with open('vm4dpy/JSON_data/views.json', 'w', encoding="utf-8") as file:
        json.dump(views, file, indent=4, ensure_ascii=False)
    
    views = generate_views(json.load(open('vm4dpy/JSON_data/views.json', encoding="UTF-8")))

    write_views_to_file(views, output)


if __name__ == "__main__":
    main("test.dpyview", "views.py")