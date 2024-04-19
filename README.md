# View maker for discord.py (Vm4dpy)

This little program lets you create Views for discord.py more easily using some kind of special language

## Introduction

Vm4dpy vous permet de créer plus facilement des (bases de) Views pour discord.py en utilisant une sorte de langage qui peut sembler légèrement similaire au YAML. Ce langage (qui sera appelé "langage de Vm4dpy" dans ce document) est conçu pour être le plus facile possible à mettre en forme et à comprendre, tout en étant suffisamment puissant pour permettre la création de Views complexes.

Ce n'est que le début de ce projet et il reste de multiples fonctionnalités à ajouter, d'autres à modifier, et des bugs à régler. Si vous avez des suggestions, des idées, des problèmes ou des questions, n'hésitez pas à les poser dans les issues de ce projet ou les proposer via un pull request !

## Requirements

- Python 3.8 or higher
- discord.py `pip install discord.py`
- Nothing else!

## How to use

Pour voir un exmeple :
1. Clonez ce dépôt
2. Exécutez `python main.py` dans le dossier cloné

### Syntax

Je vais essayer de faire simple et rapide avec des exemples :

```yaml
[view1:view]        ## Permet de créer une nouvelle View appelée "view1". Les noms doivent être uniques
> button1 {view2}   ## Ajoute un nouveau bouton à la View "view1" qui affiche la View "view2" lorsqu'il est cliqué
 | label: Button 1  ## Ajoute une propriété "label" au bouton
 | emoji: 🔴        ## Ajoute un émoji au bouton  
 | row: 2           ## Ajoute le bouton à la troisième (oui 3ème, comme avec discord.py) ligne de la View
 * embed1           ## Quand il sera cliqué, afficher l'embed "embed1"... (voir ci-dessous)
 * content1         ## ... et le contenu "content1" (voir ci-dessous)
> button2 {view3}   ## Ajoute un nouveau bouton à la View "view1" qui affiche la View "view3" lorsqu'il est cliqué
 | row: 1           ## Ajoute le bouton à la deuxième ligne de la View
 * embed2           ## Quand il sera cliqué, afficher l'embed "embed2"... (voir ci-dessous)
```

NB : pour la row (la ligne), la ligne 0 correspond à la ligne la plus haute dans discord.py, il peut y avoir un maximum de 5 lignes (row 4)

Vm4dpy respecte l'ordre hiérarchique des éléments. Par exemple, le bouton le plus haut dans le code sera le plus à gauche dans la View. Les arguments à fournir sont les mêmes que pour un bouton basique de discord.py, voir la documentation de discord.py pour savoir lesquels sont disponibles.

```yaml
[embed1:embed]      ## Permet de créer un nouvel embed appelé "embed1". Les noms doivent être uniques
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

```yaml
[content1:content]         ## Permet de créer un nouveau contenu appelé "content1"
:start                     ## Permet de définir le début du contenu
Bonjour je suis le contenu ## Ici vous pouvez écrire tout votre contenu, avec des sauts de ligne, etc...

Avec un saut de ligne
:end                       ## Permet de définir la fin du contenu. Le programme ne comptera pas ce qui suit comme faisant partie du contenu
```

Pour finir, vous devez délimiter chaque "item" (embed, view, content...) par "---" précédé et suivi, ou non, d'un saut de ligne. Par exemple :

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

Voilà c'est en gros tout ce que vous avez besoin de savoir sur Vm4dpy !

## Autres utilisations

Vous pouvez également utiliser certaines fonctions de Vm4dpy pour créer par exemple des embeds "plus rapidement". La fonction "parse_embed" de "parse_text.py" vous permet d'analyser un texte au format vm4dpy et de vous renvoyer un dictionnaire qui peut être traité par "generate_embed" de "render_view.py" pour créer un embed discord.py. Exemple :

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
