Interface d'administration pour vallorem.fr
===========================================

TL;DR
-----

This project offer an frontend for the static site generator Pelican.
The core is a plugin teaching pelican how to get pages out of the
database and an exporter offering the user to download all the data from
the db as csv files in a zip archive.

I plan to document and extract that core at some point to make it easily
available and reusable.

The project was a school assignment for a group of 4 french students for
a french laboratory. That's why not everything is in english.


Vallorem.fr
-----------

Ceci est le projet tutoré d'un groupe de quatre étudiants en licence
professionnel réseau et télécommunication à l'IUT d'Orléans. Le
laboratoire de recherche en management de l'université de Tours n'avait
plus de contrôle sur son site [vallorem.fr](https://vallorem.fr). Il
nous a donc été demandé de mettre en place une alternative, avec la
possibilité de réutiliser la base de donnée pour répondre à des enquêtes
régulière sur les résultats du labo.

Le choix le plus cohérent pour le site aurait été wordpress. Mais la
situation semblait indiquer que l'installation ne serait jamais mise à
jour, faisant craindre des failles de sécurités à venir. De plus,
personnes dans le groupe ne savait comment exploiter la base de donnée
de wordpress pour faire des requêtes arbitraire et la majorité n'avait
jamais utilisé wordpress.

Il a donc été choisi de créer une interface pour
[Pelican](https://blog.getpelican.com/) écrite avec
[Flask](http://flask.pocoo.org/). Le résultat serait deux site
distincts. Un dynamique, celui en flask, qui pourrait être protégé de
manière à n'être accessible que par les membre du labo depuis le réseau
de l'univeristé. Un second statique, accessible au publique mais ne
présentant aucun risque de sécurité.

Interface avec Pelican
----------------------

L'idée est de proposer une interface web utilisable sans connaissance
préalable. Les générateurs de site statique comme pelican et jekyll ont
de nombreux avantage au point de vue du résultat final. Mais modifier
des fichiers texte avant de lancer un programme en ligne de commande et
de deployer le résultat sur un serveur web n'est pas vraiment une option
pour nous.

Nous avons donc du trouver une solution pour présenter à l'utilisateur
de simple page web, avec des formulaire et des boutons. Dans le pire des
cas, il est possible de créer les fichiers dont pelican à besoin et de
d'executer le programme avec python. Cependant, la solution n'est pas
idéal. Exécuter un programme tiers rend le code plus complexe et soit
les fichiers devront être recréé à chaque modification des articles en
abse de donnée, soit être lu avant d'afficher un formulaire pour
modifier un article.

Heureusement, une solution plus simple a pu être trouvé. Pelican est un
programme python. L'executable fait appel à des functions python et il
est possible d'appeler directement ces functions. Par ailleurs, Pelican
propose un système de plugin. Nous avons pu l'utiliser pour ajouter les
articles directement depuis la base de donné dans le processus de
création des pages.

Exportation de la base de donnée
--------------------------------

L'un des impératifs du projet été d'avoir accès aux donnés de la base de
donnée. Plus exactement, pouvoir répondre à une série de questions
composant une enquête qui est envoyé tout les 3 ans au laboratoire. Les
questions pouvant changer, nous avont préféré ne pas simplement
introduire une page répondant à chaque question. Par manque de temps et
d'expérience, le projet n'inclut pas non plus d'interface pour composer
une requète manuellement et la définition du client exclu de proposer un
language de requète.

La solution qui a été choisis est d'exporter directement les
informations de la base de donnée sous la forme de fichier csv dans une
archive zip. Il est alors possible d'ouvrir ces fichiers dans un tableur
et d'utiliser des functions du programme pour répondres aux différentes
questions de l'enquête.

Techniquement, aucun fichier n'est créé du coté du serveur. Python
propose nativement de manipuler des fichiers zip et csv et par ailleurs
propose l'objet BytesIO qui se comporte comme un fichier mais réside en
mémoire. Un objet de se type est créé pour contenir le contenu de
l'archive zip, puis un autre pour chaque fichier csv qui va recevoir le
contenu d'une des tables de la base de donnée. Chacun des csv est inséré
dans l'archive qui est transmise directement au client. Le fichier ne
prend forme que lorsqu'il est téléchargé.

Évolutions possible
-------------------

Le projet n'est pas totalement aboutie. Le déploiment du site statique
n'a pas été traité proprement, seulement sa création. Un seul type de
contenue est supporté, les pages, l'interface n'est pas capable de
généré des articles daté ni des contenues plus spécifique tel que des
parutions du laboratoire. Par ailleurs, acceder aux donnée nécessite de
télécharger une archive zip et de l'ouvrir avec un tableur, dans un
monde de plus en plus nomade.

De nombreuse pistes d'évolutions sont possible, pour spécialiser le site
et répondre au mieux aux demandes du client. Les limitations mentionnées
précédemment donne de bonne piste de travails.

Par ailleurs, le projet pourrait être généralisé et simplifié afin de
simplement répondre à la problématique d'un générateur de site statique
accessible au plus grand nombre.
