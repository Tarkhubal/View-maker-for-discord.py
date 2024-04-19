import discord

def generate_embed(data: dict):
    _data = data['content']
    _data['footer'] = data['footer']
    _data['author'] = data['author']
    if 'color' in _data:
        _data['color'] = int(_data['color'].replace('#', ''), 16)

    return discord.Embed().from_dict(_data)

def generate_views(views_data: dict):
    views = []
    for view_data in views_data:
        if views_data[view_data]["type"] in ["embed", "content"]:
            continue

        view_code = f"""
class {view_data}(discord.ui.View):
    def __init__(self, bot: commands.Bot, author: Union[discord.User, discord.Member]):
        if isinstance(author, discord.Member):
            author = author._user
        self.bot = bot
        self.author = author
        super().__init__()

    async def interaction_check(self, interaction: discord.Interaction):
        return (interaction.user == self.author)
"""
        
        for component in views_data[view_data]['components']:
            if component['type'] == "button":
                view_code += f"""
    @discord.ui.button("""
                args = []
                if 'label' in component:
                    args.append(f"label=\"{component['label']}\"")
                if 'style' in component:
                    args.append(f"style=discord.ButtonStyle.{component['style']}")
                if 'emoji' in component:
                    args.append(f"emoji=\"{component['emoji']}\"")
                if 'row' in component:
                    args.append(f"row={component['row']}")
                if 'disabled' in component:
                    args.append(f"disabled={component['disabled']}")
                
                new_msg = {"content": None, "embed": None}
                for with_ in component['with']:
                    with_data = views_data[with_]

                    if with_data['type'] == "embed":
                        with_data['content']['type'] = "rich"
                        new_msg['embed'] = f"generate_embed({with_data})"
                    elif with_data['type'] == "content":
                        new_msg['content'] = f'"""{with_data["content"]}"""' if with_data['content'] is not None else "None"
                    else:
                        raise Exception(f"Type \"{with_data['type']}\" not recognized")

                view_code += ', '.join(args) + f""")
    async def {component['name']}(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = {new_msg['embed']}
        view = {component['action'] + "(self.bot, interaction.user)" if component['action'] not in (None, '') else "None"}
        content = {new_msg['content']}
        await interaction.response.edit_message(content=content, embed=embed, view=view)
        self.stop()
    """
    
        views.append(view_code)

    return views


def write_views_to_file(views, output: str):
    with open(output, 'w', encoding="UTF-8") as file:
        file.write("""import discord
from discord.ext import commands
from typing import Union


def generate_embed(data: dict):
    _data = data['content']
    if 'medias' in data:
        if 'thumbnail' in data['medias']:
            _data['thumbnail'] = {'url': data['medias']['thumbnail']}
        if 'video' in data['medias']:
            _data['video'] = {'url': data['medias']['video']}
        if 'image' in data['medias']:
            _data['image'] = {'url': data['medias']['image']}
    if 'fields' in data:
        _data['fields'] = data['fields']
    if 'footer' in data:
        _data['footer'] = {}
        _data['footer']['icon_url'] = data['footer']['img']
        _data['footer']['text'] = data['footer']['text']
    if 'author' in data:
        _data['author'] = {}
        _data['author']['name'] = data['author']['text']
    if 'color' in _data:
        _data['color'] = int(_data['color'].replace('#', ''), 16)

    return discord.Embed().from_dict(_data)

""")
        for i, view_code in enumerate(views):
            file.write(view_code)
            file.write("\n")
