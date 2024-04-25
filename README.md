# View maker for discord.py (Vm4dpy)

This little program lets you create Views for discord.py more easily using some kind of special language

## Introduction

Vm4dpy vous permet de créer plus rapidement des bases de Views pour discord.py en utilisant une sorte de langage qui peut sembler légèrement similaire au YAML. Ce langage (qui sera appelé "langage de Vm4dpy" dans ce document) est conçu pour être le plus facile possible à mettre en forme et à comprendre, tout en étant suffisamment puissant pour permettre la création de Views complexes.

Tout d'abord, Vm4dpy ne permet **pas** d'exécuter du code directement, il permet de créer des Views plus facilement et surtout plus rapidement en évitant des problèmes de Views qui n'existent pas. Le programme d'exemple du `main.py` vous permet de transformer votre "programme" Vm4dpy en un code Python lisible par discord.py.

Vous devez donc copier le code en sortie du programme et l'inclure à votre bot manuellement.

Ce n'est que le début de ce projet et il reste de multiples fonctionnalités à ajouter, d'autres à modifier, et des bugs à régler. Si vous avez des suggestions, des idées, des problèmes ou des questions, n'hésitez pas à les poser dans les issues de ce projet ou les proposer via un pull request !

## Requirements

- Python 3.8 or higher
- discord.py `pip install discord.py`
- Nothing else!

## Limitations
Currently vm4dpy only supports buttons, SelectMenus will be available soon

## How it works
### Use
To use vm4dpy easily:

1. Create a new file which will be the file with the vm4dpy language (you can call it whatever you want)
2. “Code” your views in this file
3. Open the main.py file then modify the file name (line 22)
4. Run the main.py (py main.py)

That's basically all you need to know about Vm4dpy!

### Syntax

*(there are examples below)*

#### `[name:type]`
Category: class

Allows you to create a new vm4dpy class (View, embed, content...)
- `name` matches the name of the element, it must be unique
- `type` corresponds to the type of the element: `view`, `embed` or `content`

#### ` | key: value`
Category: arguments
Allows you to set a key (key = an argument) to a value depending on the function (specified before the key)
- `key` represents the value to set in the sub-part, for example for a button, a `key` can be `label` (which corresponds to what will be written on the button)
- `value` corresponds to the value to assign to the key. This value (and its type) depends on the key (in most cases you must refer to [the discord.py documentation](https://discordpy.readthedocs.io/en/stable/index.html))

#### `> button_name {action}`
Category: view button
- Only if the class type is `view` (otherwise it will be ignored)
- `>` allows you to create a new button (only for Views)
- `button_name` matches the name of the button (it must not have spaces or special characters, like a Python function) and must be unique **for the view**
- `{action}` is the view that the button should display, it can be set to `{}` to not display any View. `action` must be the name of a view

#### ` * show_class`
Category: class to display
- Only for buttons
- Allows you to display `content` or `embed` when the button is clicked
- `show_class`: `content` or `embed` classes to display
- Example :
```yaml
> button2 {}
  [...]
  * embed2 ## Displays the embed2
  * content1 ## Displays content1
```

#### `$name`
Category: embed part
- Only for `embed`
- It allows you to create part of an embed. All parts, keys and values are specified here:
```yaml
$happy
  | title: text
  | description: text
  | color: hexadecimal code (type "#ff0000")
  | url: https://site.com/path
  | timestamp: 2024-04-17 20:46:21.343038
$media
  | thumbnail: https://site.com/path
  | video: https://site.com/path
  | image: https://site.com/path
$footer
  | img: https://site.com/path
  | text: Text
$author
  | text: Text
$field
  | name: Text
  | value: Text
  | inline: True or False
$field     ## Another field
  | name: Text
  | value: Text
  | inline: True or Flase
```

### Examples

In this subsection you will see examples of use

#### Views (buttons...)

```yaml
[view1:view]        ## Allows you to create a new View called "view1". Names must be unique
> button1 {view2}   ## Adds a new button to View "view1" that displays View "view2" when clicked
  | label: Button 1 ## Adds a "label" property to the button with value "Button 1"
  | emoji: 🔴       ## Adds an emoji to the button
  | row: 2          ## Adds the button to the third (yes 3rd, like with discord.py) row of the View
  * embed1          ## When clicked, display the embed "embed1"... (see below)
  * content1        ## ... and the content "content1" (see below)
> button2 {view3}   ## Adds a new button to View "view1" that displays View "view3" when clicked
  | row: 1          ## Adds the button to the second row of the View
  * embed2          ## When clicked, display the embed "embed2"... (see below)
```

NB: for the row, line 0 corresponds to the highest line in discord.py, there can be a maximum of 5 lines (row 4)

The arguments to provide for the button are the same as for a basic discord.py button, [see the discord.py documentation](https://discordpy.readthedocs.io/en/stable/interactions/api.html? highlight=button#discord.ui.Button) to see which ones are available.

Vm4dpy respects the hierarchical order of elements. For example, the topmost button in the code will be the leftmost in the View.

#### Embeds

```yaml
[embed1:embed]      ## Permet de créer un nouvel embed appelé "embed1".
$ content           ## Permet de créer le "corps" de l'embed
 | title: help      ## Ajoute une propriété "title" à l'embed
 | description: yes ## Ajoute une propriété "description" à l'embed
 | color: #ff0000   ## etc...
 | url: https://google.com
 | timestamp: 2024-04-17 20:46:21.343038
$ medias            ## Permet de créer les "médias" de l'embed (images, vidéos, etc.)
 | thumbnail: https://img/img.png ## Pas besoin de préciser ce que ça fait...
 | video: https://video/video.mp4 ## À noter : vous ne pouvez pas pour le moment utiliser
 | image: https://img/img.png     ## des fichiers locaux pour les médias
$ footer
 | img: https://img/img.png
 | text: bruh
$ author
 | text: nope
$ field                 ## À noter : les fields sont rangés dans l'ordre croissant, ce qui signifie
 | name: field1         ## que le field le plus haut sera le field le plus haut et le plus à gauche
 | value: value1 ok     ## sur Discord.
 | inline: True
$ field
 | name: field2
 | value: value2 yay
 | inline: False
$ field
 | name: field3
 | value: value3 mbeuuuh
 | inline: False
```

#### Contents

```yaml
[content1:content]         ## Permet de créer un nouveau contenu appelé "content1"
:start                     ## Début du contenu à la ligne suivante
Bonjour je suis le contenu ## Ici vous pouvez écrire tout votre contenu, avec des sauts de ligne, etc...

Avec un saut de ligne
:end                       ## Fin du contenu
```

#### Délimitations de classes

Pour finir, vous devez délimiter chaque classe (embed, view, content...) par "---" précédé et suivi, ou non, d'un saut de ligne. Par exemple :

```yaml
[embed2:embed]
$ content
 | title: help
 | description: yes
 | color: #ff0000

---                  ## ici

[view2:view]
> button1 {view3}
 | row: 1
 | label: Button 1
 * embed2
---                  ## ici
[view3:view]
> button1 {view1}
 | row: 1
 | label: Bouton 1
 * content1
```

## Other uses

You can also use certain Vm4dpy functions to create embeds "faster", for example. The "parse_embed" function of "parse_text.py" allows you to parse text in vm4dpy format and return you a dictionary which can be processed by "generate_embed" of "render_view.py" to create a discord.py embed. Example :

```python
from vm4dpy.parse_text import parse_embed
from vm4dpy.render_view import generate_embed


text = """
[embed1:embed]
$ content
 | title: help
 | description: yes
 | color: #ff0000
"""

parsed = parse_embed(text)
embed = generate_embed(parsed)
```
