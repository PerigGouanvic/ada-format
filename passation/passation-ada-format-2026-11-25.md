# Passation : soirée ada-format du 24 novembre 2026

Pour : l'agent qui travaille avec Perig sur son serveur (`~/projects/ada-format`,
`~/projects/jp3`).
De : un projet Claude (claude.ai) mené le 24 novembre 2026, de 21 h 43 à
23 h 47, heure de Montréal. Ce projet est maintenant fermé.

## Comment lire ce document

Perig, à la fin de la soirée : « toute cette aventure m'a permis de
redécouvrir que je redécouvrais mes idées parce qu'en fait j'en ai tellement
que je me perds ». Puis : « Il faut lui fournir le résultat de ton travail, une
chronique de ce qu'on a vécu ».

Le projet n'avait accès ni au serveur ni à `design/brief-encodeur-2026-09-27.md`.
Il a travaillé à partir des dépôts GitHub publics (ada-format, JP3) et, en fin
de soirée seulement, du backup Google Drive des fiches mémoire (23 novembre).
**Ce qui est sur le serveur prime.** Traite ce document comme un dépôt
(`grown_from_deposits`) : une matière datée à confronter à ce que tu sais déjà,
pas comme une décision.

Les phrases entre « » sont de Perig. Le reste est écrit par des agents.

## Chronique

**21 h 43. Diagnostic.** Un premier fil lit le site ada-format : un manifeste
ambitieux, mais aucun fichier `.ada`, une feuille de route dépassée (T1 à T4
2026) et deux affirmations contradictoires (« illisible par design » contre
« lu nativement par les IA »). JP³ n'apparaît que dans une note du README. Le
coordinateur lance trois fils : la spec, la page principale, une démo JP³.

**21 h 49. Trois premiers jets, tous à côté.** La spec propose un format YAML
(texte source découpé en sections). La page présente le `.ada` comme du YAML
brut. Aucun des deux ne connaît `jp3.ada`.

**21 h 52. Découverte de `jp3.ada`.** Le fil démo trouve dans le dépôt JP3
l'archive zip du 26 septembre (manifest.json, ada-usage.md, prompt.md,
open_questions.md). C'est la seule spécification réelle du format. Perig
tranche : **recaler la v0.1 sur ce zip**. Le brouillon YAML devient une
proposition v0.2 (`structure.yaml` dans le zip). La page s'aligne.

**21 h 56. L'original voyage dans le zip.** À la question « l'article
original doit-il voyager dans le zip ? », Perig : « Oui, et ouvre là si c'est
là que tu es rendu ». La spec recommande un dossier `source/` ; en cas d'écart,
l'original l'emporte. **PR #1** ouverte sur ada-format.

**21 h 56. Démo JP³.** Encodage du §2 du manuel (Les trois P) en
`jp3-trois-p.ada`. Il passe le validateur de la spec. Deux erreurs de sources
relevées : le DOI de Hamilton 2022 dans `jp3.ada` est faux (le bon :
10.1016/j.isci.2022.104869) ; la référence « Bosch » sur le transfert
d'entraînement renvoie à San-Millan & Bosch 2020, qui porte sur la flexibilité
métabolique.

**22 h 00 à 22 h 07. Le téléphone.** Perig : « On devra pousser mais pas dans
main. Il y a beaucoup de discussions auxquelles tu n'as pas accès qui sont sur
le serveur. » Son Android ne reconnaît pas `.ada` comme un zip et ne propose
aucune application. Après renommage, l'extraction marche. Conséquence pour la
spec (§2.1) : publier deux copies identiques, `nom.ada` et `nom.ada.zip`, et
servir en `application/zip`. Autre problème relevé : `.ada` est déjà
l'extension des sources du langage Ada.

**22 h 14. Test réel avec DeepSeek.** Perig : « c'est vraiment un problème que
tu mentionnes toujours le manuel et l'auteur alors que le robot doit se
substituer à moi. De plus les réponses sont bien trop longues ; pour s'adapter
à plein de lecteurs il faut d'abord être à l'écoute au lieu de parler sans
arrêt. Aussi quand il faut inciter la personne à faire l'essai tout de suite et
à parler en même temps. Mais ce n'est pas obligatoire parce qu'il y a des
lecteurs qui seraient juste curieux ». La spec (§4) et un `ada-usage.md` de
référence en français sont réécrits : l'IA parle à la première personne à la
place de l'auteur, écoute d'abord, répond court, invite à essayer sans
l'imposer. Une règle d'honnêteté reste : si on le lui demande, elle dit
qu'elle est une IA qui parle au nom de l'auteur.

**22 h 30. Le matériau, pas le protocole.** Perig : « je pourrais décider de
mieux développer le protocole Ada mais en réalité il est pas si mal comme ça
c'est plutôt le matériau de JP3 qui n'est pas encore assez mordant et assez
polyvalent. [...] nous n'avons pas d'image ni de vidéo. Nous n'avons pas de
capsule pour distraire la personne qui est en train de courir [...] il n'y a
pas de lecteur idéal parce que tout le monde est différent ». La page s'ouvre
désormais sur l'absence de lecteur idéal. Un fil dédié à l'entretien de
l'auteur est lancé.

**22 h 33. Un prompt d'entretien, puis une lecture de JP³.** Premier jet :
`encoder/entretien-auteur.md`. Préparation sur JP³ : la physiologie existe
déjà (§4.1.1 : soléaire 80 à 90 % de fibres de type I ; §7.1 : perte des
fibres de type II avec l'âge), mais pour des initiés. « Phasic-glycolytic »
revient une dizaine de fois sans jamais être défini. Le manuel ne contient
qu'une seule image (la courbe x³). Le §6.3 (*ego and echo*) range l'écoute en
pratiquant en « zero cost, high benefit » : les capsules sont justifiées par
la doctrine, mais aucune n'existe. Le §4.3.2 parle de « toxic byproducts »
sous le seuil lactique, ce qu'un lecteur en physiologie contesterait.

**22 h 37 à 22 h 40. Un prompt qui supposait trop.** Perig : « est-ce que le
fichier Ada peut servir autant à l'auteur que lecteur », puis : le prompt
« mentionne Ada sans jamais le définir [...] c'est obscur pour une machine qui
n'a aucune idée ». Le prompt est rendu autonome.

**23 h 15. Le recadrage central.** Perig : « Ada est peut-être présenté par
son résultat, et son manifeste que nous avons fait, mais c'est avant tout une
façon de construire un corpus ada, qui se deballera tout naturellement sous
forme d'expérience de lecture ada!! C'est ça qu'il faut développer. Et j'ai
écrit des choses sur ça dans le dépôt... » Relevé dans JP3 : « j'ai
l'intention que l'article JP³ devienne non pas un texte mais un contexte pour
un agent » (manuel §6.3), la dictée en pratique comme méthode de production,
le mandat du 4 novembre (« l'important c'est que tout le contenu soit
dedans »), la source unique et ses « dérivations ada ». Un texte de méthode
est écrit sur ce modèle. La page prend pour sous-titre *Not a text, but a
context*.

**23 h 18 à 23 h 20. Le backup Drive.** Perig : « Ça doit être sur le serveur
dans les discussions ou mémoires », puis « Ce serait dans ce cas dans le
backup drive ». Les fiches mémoire ada-format du backup du 23 novembre
montrent que l'essentiel avait déjà été conçu :
- `project_zip_architecture.md` (31 juillet) : le mode **`grown_from_deposits`**,
  le dossier `deposits/`, `open_questions.md` comme questions à l'auteur pour
  la séance suivante, un `.ada` par thème ;
- `project_encoder_web_tool.md` (31 juillet) : l'outil encodeur web, mobile,
  avec « dépôt libre » et « interroge-moi » séparés ;
- `project_ada_encoder_device.md` (26 septembre) : l'agent ada comme
  « partenaire socratique de l'auteur (pas seulement du lecteur) », et la
  contrainte de méthode : concevoir le protocole dans une session vierge de
  tout document source ;
- `project_protocol_interview_personas.md` (27 septembre) : l'homologie, les
  trois registres SUIT / BLOQUE / INCERTAIN, des personas cognitifs et non
  biographiques, les modes Construction et Diagnostic.

Le prompt d'entretien de la soirée **contredit** ce protocole : ses lecteurs
sont biographiques (« Marguerite, 78 ans ») et tirés du texte, dans une
session qui avait lu tout JP3. Il n'a pas été réécrit. La spec (PR #1) et la
page ont intégré `grown_from_deposits` et les personas cognitifs. Le texte de
méthode a été réécrit autour de ces décisions.

**23 h 44. Le constat.** Perig : « je redécouvrais mes idées parce qu'en fait
j'en ai tellement que je me perds. Donc en fait tout ce qu'on a fait devrait
être sous toutes réserves de ce que j'ai déjà accompli dans le serveur ».

**23 h 47. Fermeture.** Perig demande cette passation et ferme le projet.

## Ce que la soirée a produit

Tout est dans `PerigGouanvic/ada-format`, sur des branches. Rien n'est dans
main.

| Branche | Contenu | État |
|---|---|---|
| `claude/project-thread-x0szul` | `spec/ada-v0.1.md` (zip de jp3.ada, `source/`, `.ada.zip`, voix à la première personne, `grown_from_deposits`, personas cognitifs), `spec/manifest-v0.1.schema.json`, `spec/templates/ada-usage.md` (français), `tools/validate_ada.py`, proposition v0.2 `structure.yaml` | **PR #1 ouverte**, non fusionnée |
| `claude/project-thread-fvb4zf` | `docs/index.html` réécrit : *Not a text, but a context*, absence de lecteur idéal, parcours en quatre gestes, limites, polémique en annexe E, gabarit retiré (environ 9 Mo) | pas de PR |
| `claude/project-thread-17s2eb` | `docs/examples/jp3/` : `jp3-trois-p.ada` et `.ada.zip` (§2 Les trois P, prompt.md à la première personne), page avant/après | pas de PR |
| `claude/project-thread-2r9un5` | `encoder/entretien-auteur.md` (premier jet, **ne suit pas** le protocole du 27 septembre), `docs/examples/jp3/entretien/preparation-entretien.md`, `methode/construire-un-corpus-ada.md`, `methode/corpus-ada-sources.md` (verbatim et chemins) | pas de PR, marqué « sous réserve » |

Les branches ont été créées à des moments différents et se recoupent. Il
faudra choisir un ordre de fusion (spec d'abord, puis page, puis exemples).

## Ce qu'il faudrait confronter au serveur

1. Le brief `design/brief-encodeur-2026-09-27.md` : le projet ne l'a jamais lu.
   La spec et la méthode s'appuient seulement sur la fiche qui le résume.
2. La conversation Perplexity du 2 février 2026 sur Socrate et les livres
   (origine du format), et celle du 17 septembre sur les formats d'empaquetage
   pour contexte et instructions. Elles sont dans le backup Drive, mais n'ont
   pas été lues.
3. `open_questions.md` a deux destinataires selon le mode : le lecteur dans
   `jp3.ada`, l'auteur dans `grown_from_deposits`. Il faut deux sections ou
   deux fichiers.
4. Le `.ada` ouvert par son auteur : `ada-usage.md` pourrait faire passer
   l'IA en mode dépôt ou entretien quand la personne dit être l'auteur.
5. Les dépôts de JP³ sont dispersés (`notes/`, `facts/`, fiches mémoire,
   conversations du serveur). Les réunir dans `deposits/` ferait de JP³ le
   premier corpus ada complet.
6. Le matériau JP³ qui manque : images et vidéos de gestes (talon qui tombe,
   forme furtive, bande avant-arrière), capsules audio pour le coureur,
   définition de « phasic-glycolytic », nuance sur le lactate « toxique »,
   DOI Hamilton et référence Bosch.
7. L'extension `.ada` : collision avec le langage Ada, et l'absence de type
   reconnu par les téléphones.

## La leçon de la soirée

Quatre fils ont redécouvert en deux heures, à partir des seuls fichiers
publics, ce que Perig avait déjà conçu entre juillet et septembre. Ils ont
retrouvé le zip, les dépôts, l'entretien et l'auteur comme premier
interlocuteur. Une fois, ils ont même fait le contraire de ce qu'il avait
décidé (les personas). L'auteur lui-même ne retrouvait plus ses idées. C'est
exactement le cas que `grown_from_deposits` veut traiter : un corpus qui
réponde aussi à son auteur, et des agents qui consultent ce corpus avant de
concevoir.
