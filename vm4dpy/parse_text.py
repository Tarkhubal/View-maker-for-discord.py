def parse_view(text: str, views: dict):
    for line in text.split('\n'):
        if line.isspace():
            continue

        if "[" in line and "]" in line:
            name = line.strip("[]").split(":")[0]
            views[name] = {
                "type": "view",
                "components": []
            }
        
        if line.startswith("> "):
            button_name = line.strip("> ").replace(" ", "")
            calls = None
            if "{" in button_name and "}" in button_name:
                button_name, calls = button_name.strip("}").split("{")
                calls = calls.split(',')
            
            views[name]['components'].append({'type': 'button', 'name': button_name, 'action': calls[0] if len(calls) > 0 else None})
        
        if line.startswith(" | "):
            key, value = line.strip(" | ").split(":", 1)
            if value.startswith(' '):
                value = value.replace(' ', '', 1)
            if len(views[name]['components']) == 0:
                raise Exception(f"Vous devez définir un élément avant de définir ses valeurs. Ligne: \"{line}\"")
            views[name]['components'][-1][key] = value
        
        if line.startswith(" *"):
            if not "with" in views[name]['components'][-1].keys():
                views[name]['components'][-1]["with"] = []
            views[name]['components'][-1]["with"].append(line.split(" *")[1].replace(" ", ""))

    return views

def parse_embed(text: str, views: dict = {}):
    cat = None
    field_active = False
    field = {}
    lines = [l for l in text.split("\n") if l not in ('', ' ')]
    lines.append('') # idk but shht it's working

    for i, line in enumerate(lines):
        if i == len(lines)-1 and field_active:
            if field != {}:
                views[name]["fields"].append(field)
            continue

        if line.isspace():
            continue

        if "[" in line and "]" in line:
            name = line.strip("[]").split(":")[0]
            views[name] = {"type": "embed"}

        if line.startswith(" | "):
            if cat is None:
                raise Exception(f"Vous devez définir une catégorie pour les valeurs de l'embed. Ligne: \"{line}\"")
            
            key, value = line.strip(" | ").split(":", 1)
            if value.startswith(' '):
                value = value.replace(' ', '', 1)
            
            if field_active:
                if key == "inline" and value in ("True", "False"):
                    value = True if value == "True" else False
                field[key] = value
                continue

            views[name][cat][key] = value

        if line.startswith("$ "):
            if field_active:
                field_active = False

                if field != {}:
                    views[name]["fields"].append(field)
                field = {}

            cat = line.replace("$ ", "", 1).replace("$", "", 1)
            if "field" in cat:
                cat = "fields"
                if not "fields" in views[name].keys():
                    views[name]["fields"] = []
                field_active = True
                field = {}
                continue

            views[name][cat] = {}

    return views

def parse_content(text: str, views: dict):
    start_collecting = False
    for line in text.split('\n'):
        if line.isspace() and not start_collecting:
            continue
        
        if "[" in line and "]" in line:
            name = line.strip("[]").split(":")[0]
            views[name] = {
                "type": "content",
                "content": None
            }
        
        if line.startswith(":start"):
            views[name]['content'] = ""
            start_collecting = True
            continue
        
        if line.startswith(":end"):
            views[name]['content'] = views[name]['content'].strip()
            start_collecting = False
            continue
        
        if start_collecting:
            views[name]['content'] += line + '\n'

    return views


def parse_text(text: str):
    views = {}
    for part in text.split('---'):
        for line in part.split('\n'):
            if line.isspace():
                continue
            
            if line.endswith(':view]'):
                views = parse_view(part, views)
                break
            
            
            elif line.endswith(':embed]'):
                views = parse_embed(part, views)
                break
                
            elif line.endswith(':content]'):
                views = parse_content(part, views)
                break
    
    return views
