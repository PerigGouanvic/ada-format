# Construire un corpus ada

Brouillon, 25 novembre 2026. Tiré de la façon dont JP³ s'est réellement
construit (dépôt PerigGouanvic/JP3, août à novembre 2026). Les points marqués
**[H]** sont des hypothèses ; les passages entre « » sont les mots de Perig,
relevés dans [`corpus-ada-sources.md`](corpus-ada-sources.md).

## La thèse

Un `.ada` ne se fabrique pas à la fin, en convertissant un texte fini. Il se
**déballe** d'un corpus construit dès l'origine pour être lu par une IA :

> « j'ai l'intention que l'article JP³ devienne non pas un texte mais un
> contexte pour un agent » (manuel JP³, §6.3)

Le manifeste disait déjà « Encoding from origin (not after-the-fact
adaptation) ». La pratique de JP³ montre ce que ça veut dire concrètement.
L'expérience de lecture ada (une IA qui parle à la place de l'auteur, à chaque
lecteur) n'est pas le travail principal. Elle en découle presque toute seule
quand le corpus est bon. Le travail, c'est le corpus.

## Ce qu'est un corpus ada, d'après JP³

**1. Une source unique, qui accumule.** Tout va dans un seul texte central
(pour JP³, `content/en/manual/MANUAL.md`, environ 300 Ko). L'homogénéité n'est
pas le but :

> « Ce n'est vraiment pas important d'avoir quelque chose d'homogène
> l'important c'est que tout le contenu soit dedans. » (4 novembre 2026)

Un humain ne lirait pas ce texte d'une traite. Une IA, si. C'est ce qui permet
de garder ensemble des registres qu'un livre devrait séparer.

**2. Des apports de toutes natures, datés.** Dans JP³, la matière arrive par :
des dictées faites *pendant* la pratique ; des notes de terrain datées ; des
conversations avec des IA, gardées en transcription (`facts/`) ; les fiches
mémoire des agents qui travaillent avec l'auteur ; des sources lues et glosées.
La dictée en pratique est une méthode à part entière :

> « je dicte cette section pendant que je fais JP³, et c'est même un
> déclencheur » (§6.3)

Le corpus est donc co-écrit avec ce qu'il décrit. Chaque apport garde sa date
et son origine, ce qui permet plus tard de dire « j'ai remarqué, le 7 août… »
au lieu de « il est établi que… ».

**3. L'auteur dispose.** Les IA proposent, rangent, consolident, signalent les
tensions ; l'auteur valide (« L'IA propose, Perig dispose », règle du dépôt
JP3). Rien n'entre dans la doctrine sans lui.

**4. Le statut et le poids de chaque chose sont écrits.** JP³ marque ce qui est
vécu, sourcé ou supposé, et ce qui est central (« noyau non-ratable », ★★★) ou
accessoire. Les sources sont glosées par l'auteur, avec une contre-lecture
(`PILOTE-refs.md`). C'est ce qui permettra à l'IA du lecteur de simplifier
sans trahir : elle sait ce qu'elle ne doit pas perdre.

**5. Ce qui reste dans la tête d'un agent n'existe pas.** Ce qu'une IA a appris
en travaillant avec l'auteur doit être projeté dans le corpus versionné, sinon
il est perdu pour la suivante (règle 7 de `AGENT-BRIEFING.md`).

**6. Tout le reste est dérivation.** Les traductions, l'article, les résumés,
les `.ada` d'une section sont **régénérés** à partir de la source, jamais
corrigés à part : « Toute évolution doctrinale se fait dans le manuel, jamais
dans une dérivation » (`AGENT-MEMORY.md`). Un `.ada` est une dérivation parmi
d'autres, empaquetée pour une IA de lecteur.

## Les gestes

Construire un corpus ada, c'est répéter quelques gestes, dans n'importe quel
ordre :

| Geste | Ce qu'on fait | Dans JP³ |
|---|---|---|
| **Verser** | Dicter, noter, garder une conversation. Brut, daté. | dictées en séance, `notes/`, `facts/` |
| **Consolider** | Faire entrer l'apport dans la source unique, à sa place. | migrations vers `MANUAL.md` |
| **Marquer** | Dire le statut (vécu, sourcé, supposé) et le poids (noyau ou non). | ★★★, « Noyau non-ratable » |
| **Gloser** | Lire une source, dire ce qu'elle soutient et ce qu'elle ne soutient pas. | `PILOTE-refs.md` |
| **Interroger** | Faire venir les lecteurs absents et laisser l'auteur leur répondre. | [`../encoder/entretien-auteur.md`](../encoder/entretien-auteur.md) |
| **Dériver** | Régénérer une lecture : une langue, un résumé, un `.ada`. | article FR, `jp3.ada`, démo des trois P |
| **Recevoir** | Faire revenir ce que les lecteurs disent, et le verser. | canal `feedback` du `.ada` |

L'entretien n'est donc pas une étape préalable unique. C'est un geste parmi
d'autres, qu'on refait chaque fois que le corpus parle à trop peu de lecteurs.

## Ce que ça change pour le format **[H]**

- **`source/` devient le cœur de l'archive.** Ce n'est plus « le texte original,
  recommandé », c'est le corpus (ou la partie qui concerne ce `.ada`). `prompt.md`
  en est une dérivation : la façon de parler, le noyau, ce qu'il ne faut pas
  perdre.
- **Le `.ada` peut servir à l'auteur.** Si celui qui ouvre l'archive dit être
  l'auteur, l'IA peut passer en mode entretien plutôt que de lui parler à sa
  place. L'archive devient un outil pour continuer le corpus, et ce que
  l'entretien produit se verse dans la source.
- **Le format de sortie de l'entretien** (matière verbatim datée, registre des
  manques, questions ouvertes, corrections) est aussi celui des apports en
  général. Un seul gabarit pour tout ce qu'on verse.

## Ce que JP³ montre qui manque encore

Le corpus JP³ est riche en doctrine et en physiologie, mais il parle surtout
aux initiés, et seulement par le texte : une image en tout, pas de geste
montré, pas de capsule à écouter en pratiquant, alors que le §6.3 dit que
l'écoute en pratiquant ne coûte rien et rapporte beaucoup. Le relevé est dans
[`../docs/examples/jp3/entretien/preparation-entretien.md`](../docs/examples/jp3/entretien/preparation-entretien.md).
Un corpus ada doit pouvoir contenir des images, des sons et des vidéos aussi
naturellement que des dictées.

## Questions pour l'auteur

1. Est-ce que « corpus ada » désigne la source unique seule, ou la source plus
   tout ce qui l'alimente (dictées, fiches, conversations) ?
2. Le `.ada` doit-il transporter le corpus entier, ou seulement la partie
   utile et un lien vers le reste ?
3. As-tu écrit ailleurs (sur ton serveur) sur cette façon de construire ? Je
   n'ai trouvé que ce qui est dans le dépôt JP3.
