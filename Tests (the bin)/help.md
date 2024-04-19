# Auto Views for discord.py

## Définir un embed

```
$my_embed
*color=#ff0000
*title=`Mon titre avec {{var}}`
*url=`https://url/du/titre`
*description="""
Contenu de l'embed, si il y a trois fois le symbole " vous pouvez sauter des lignes, le programme attendra d'avoir les trois symboles pour compter ça comme la fin du texte

C'est utile si vous avez plusieurs paragraphes à mettre

C'est possible d'afficher des variables comme ça : (ma_var) et aussi de faire des conditions :
%%IF show_me==True%%
Mbeuh
%%ELIF show_me==None%%
Pas mbeuh ?
%%ELSE%%
ah bah non
%%ENDIF%%

Les boucles c'est pas pour tout de suite désolé"""
```


## Créer une nouvelle view de zéro

Pour créer une nouvelle view :
[Nom de la view]@my_embed
VAR mes_variables=True; je_les_mets=`Yes`; ici=2
    > Bouton numéro 1
        @my_embed_02
        > Bouton numéro 2