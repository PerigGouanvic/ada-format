# Construire un corpus ada

> **Sous réserve (25 novembre 2026).** Perig a déjà travaillé ces questions sur un serveur auquel il n'a pas accès en ce moment. Ce texte est provisoire et sera confronté à ce travail dès qu'il sera disponible.

Brouillon, 25 novembre 2026. Ce texte rassemble des décisions que Perig a
déjà prises (fiches mémoire de juillet et septembre 2026) et la façon dont
JP³ s'est réellement construit (dépôt PerigGouanvic/JP3). Sources et verbatim
dans [`corpus-ada-sources.md`](corpus-ada-sources.md). Les points marqués
**[H]** restent à décider.

## La thèse

Un `.ada` est d'abord une façon de construire un corpus. L'expérience de
lecture (une IA qui parle à la place de l'auteur, à chaque lecteur) se déballe
ensuite de ce corpus presque toute seule. Le travail principal, c'est le corpus.

> « j'ai l'intention que l'article JP³ devienne non pas un texte mais un
> contexte pour un agent » (manuel JP³, §6.3)

Le format prévoit depuis juillet 2026 deux façons de naître, indiquées par le
champ `mode` du manifest. Ce champ décrit un état, pas une identité : un `.ada`
passe de l'un à l'autre.

- **`encoded_from_source`** : un texte existe déjà, on l'encode. C'est le cas
  de `jp3.ada` en septembre.
- **`grown_from_deposits`** : le `.ada` naît sans texte. Il s'accumule par
  dépôts et cristallise peu à peu en `prompt.md`, par dialogue socratique avec
  l'auteur. La fiche du 31 juillet dit que ce mode fait passer le `.ada`
  « d'outil d'accès à la littérature en outil de création d'une littérature
  qui n'aurait pas existé sans lui ».

C'est le second mode qui définit le format. Le premier en est un cas
particulier : un texte déjà écrit n'est qu'un très gros dépôt.

## Comment un corpus pousse

**1. Déposer, sans friction.** Une idée, une dictée, une capture, une
transcription vocale, datées, dans `deposits/`. Pas de question, pas de
reformulation. « Trop de questions à chaud tue l'éclair. » JP³ montre que la
dictée faite pendant la pratique est un des meilleurs dépôts :

> « je dicte cette section pendant que je fais JP³, et c'est même un
> déclencheur » (§6.3)

**2. Se faire interroger, à la demande.** L'auteur lance lui-même une passe
socratique. L'IA lit les dépôts et pose une ou quelques questions sur ce qui
reste flou ou sur ce qu'un lecteur ne pourrait pas suivre. Les réponses
deviennent de nouveaux dépôts. Les questions non traitées attendent dans
`open_questions.md`, pour la séance suivante. Le protocole de l'entretien est
décrit plus bas.

**3. Cristalliser.** Les dépôts et les réponses se condensent en `prompt.md` :
ce que l'auteur sait, comment il parle, ce qu'il ne faut pas perdre. Dans JP³,
c'est le manuel central qui joue ce rôle, et les règles du dépôt en tirent
trois exigences :

- **une seule source**, qui accumule sans souci d'homogénéité (« l'important
  c'est que tout le contenu soit dedans », 4 novembre 2026) ;
- **l'auteur dispose** : l'IA propose, range, consolide, et rien n'entre sans
  lui ;
- **le statut et le poids sont écrits** : vécu, sourcé ou supposé ; central
  (« noyau non-ratable ») ou accessoire. Les sources sont glosées par l'auteur,
  avec une contre-lecture (`PILOTE-refs.md`).

**4. Dériver.** Les lectures (une langue, un résumé, un article, un `.ada`
d'une section) sont régénérées depuis la source, jamais corrigées à part.
Chaque `.ada` porte une langue source, et l'IA du lecteur s'adapte à la
sienne.

**5. Recevoir.** Le canal `feedback` ramène ce que disent les lecteurs, et ce
retour redevient un dépôt. La boucle se ferme.

Un `.ada` par thème, jamais un carnet global (décision du 31 juillet).

## L'entretien : trouver les questions

> « L'auteur arrive avec des réponses. Le logiciel l'aide à trouver toutes les
> questions. Le `.ada` contient les deux. » (fiche du 27 septembre 2026)

Le protocole arrêté le 27 septembre ne demande pas à l'IA d'oublier ce qu'elle
sait. Il mesure si l'explication **accroche** : un lecteur comprend s'il trouve
un pont vers quelque chose qu'il vit ou a vécu. Chaque lecteur simulé répond
dans un de trois registres :

- **SUIT** : « je te suis parce que ça ressemble à… » ;
- **BLOQUE** : « je me perds, le pont manque entre A et B » ;
- **INCERTAIN** : « je ne sais pas si quelqu'un comme moi connaîtrait X. Est-ce
  que tu le supposes ? » La question revient à l'auteur au lieu d'être comblée
  en silence.

Les lecteurs sont décrits par une structure cognitive, pas par une biographie.
Deux modes : **Construction** (l'auteur part de zéro) et **Diagnostic** (les
lecteurs lisent un texte existant et l'annotent paragraphe par paragraphe).
Les objections sont de deux sortes : un pont manque (compréhension), ou le
lecteur veut une autre forme, comme une image, un exercice ou une capsule à
écouter (format).

Le brief complet de ce protocole est dans `design/brief-encodeur-2026-09-27.md`,
dans le dossier local d'ada-format. Le prompt
[`../encoder/entretien-auteur.md`](../encoder/entretien-auteur.md) en est un
premier jet qui **ne suit pas encore ce protocole** (lecteurs biographiques,
tirés du texte) et doit être réécrit.

## Ce qui reste à décider **[H]**

- **Le `.ada` ouvert par son auteur.** Puisque `deposits/` et
  `open_questions.md` sont dans l'archive, le même fichier peut servir à
  continuer le corpus. `ada-usage.md` pourrait dire à l'IA : si la personne
  dit être l'auteur, propose de déposer ou de l'interroger plutôt que de lui
  parler à sa place.
- **Où vivent les dépôts de JP³.** Aujourd'hui ils sont dispersés entre
  `notes/`, `facts/`, les fiches mémoire des agents et des conversations sur
  un serveur. Les rassembler dans `deposits/` ferait de JP³ le premier corpus
  ada complet.
- **`open_questions.md` a deux destinataires.** Dans `jp3.ada`, ce sont des
  questions au lecteur. Dans `grown_from_deposits`, ce sont des questions à
  l'auteur. Il faut soit deux sections, soit deux fichiers.
- **L'outil encodeur** (page web statique, mobile, clé API locale, « dépôt
  libre » et « interroge-moi » séparés, conçu le 31 juillet) n'est pas encore
  construit.
- **Les médias.** Le corpus JP³ ne contient qu'une image et aucun son. Un
  corpus ada doit accueillir des photos, des sons et des vidéos aussi
  facilement que des dictées, ce que `media/` et les dépôts par capture
  permettent déjà sur le papier.
