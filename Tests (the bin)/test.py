import discord


part = {'type': 'embed', 'content': {'title': 'help', 'description': 'yes', 'color': '#ff0000'}, 'footer': {'img': 'https://img/img.png', 'text': 'bruh'}, 'author': {'text': 'nope'}}

def generate_embed(data: dict):
    _data = data['content']
    _data['footer'] = data['footer']
    _data['author'] = data['author']
    if 'color' in _data:
        _data['color'] = int(_data['color'].replace('#', ''), 16)

    return discord.Embed().from_dict(_data)

print(generate_embed(part))