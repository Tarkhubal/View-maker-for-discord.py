! DEF:
!    ">"    : Button
!    ":"    : Modal "(FIELD1, FIELD2)"
!    "@"    : Select "(content)"
!    "{x}"  : Return to x
!    "#"    : Define embed content
!    "<br>" : New line
!    "."    : Define other parameters
!    "(x)"  : Use var x
!    "$"    : Define an embed

$

[Admin]
VAR show_key=False; api_key; url
    > Configurer le bot # Voici les différentes options pour configurer le bot<br><br>Clé d'API: %%IF show_key==True%%`(api_key)`%%ELSE%%`Cliquez sur "Afficher la clé d'API" pour afficher la clé d'API`
        > :Modifier l'URL (URL) | url=URL
        > :Modifier la clé d'API (KEY) | api_key=KEY
        > Afficher la clé d'api
            => {Configurer le bot}$show_key=True

        > Système de niveaux
            > :Ajouter un niveau (Nom du niveau, Emoji du niveau, )
                > Modifier

            > Supprimer un/des niveau(x)
                > @(niveaux de la guild)
                    => {Système de niveaux}
    > Gérer...
        > ...les utilisateurs
        > ...les panels

[Support]