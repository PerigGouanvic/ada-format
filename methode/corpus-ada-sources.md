# Ce que Perig a écrit sur la construction d'un corpus ada

Relevé dans le dépôt PerigGouanvic/JP3 (dernier commit lu : 14 novembre 2026)
et dans ada-format (main). La plupart des fichiers de JP3 sont rédigés par des
agents. **Seuls les passages entre « » sont les mots de Perig.**

## Mots de Perig

1. `content/en/manual/MANUAL.md` §6.3 (aussi `content/fr/research-singularite.md` l. 730) :
   « j'ai l'intention que l'article JP³ devienne non pas un texte mais un contexte pour un agent »
2. Même §6.3 :
   « je dicte cette section pendant que je fais JP³, et c'est même un déclencheur — la dictée m'empêche de tomber dans l'auto-observation qui casserait la modalité »
   Le manuel en tire (texte d'agent) : la dictée en séance est « a production method: the context is co-written with the practice it documents ».
3. `MANUAL.md` §6.7 :
   « c'est l'avantage d'avoir un coach à qui on doit rendre des comptes »
4. `notes/2026-11-04-session-migration-manual.md`, mandat :
   « Ce n'est vraiment pas important d'avoir quelque chose d'homogène l'important c'est que tout le contenu soit dedans. »
   « Un seul fichier pour tout que l'on va parcourir de la manière habituelle avec des sections et une table de matière ou plusieurs tables des matières, par section. Tout copier dedans en effet y compris les fiches mémoires. »
5. Manifeste ada-format (`docs/index.html` sur main, février 2026) :
   « Encoding from origin (not after-the-fact adaptation) », « AI becomes structural interviewer », « Iteration until saturation (all imaginable reader profiles are served) ».
6. Fil du projet, 25 novembre 2026 :
   « c'est avant tout une façon de construire un corpus ada, qui se deballera tout naturellement sous forme d'expérience de lecture ada!! »

## Règles écrites par des agents dans JP3, appliquées par Perig

- `AGENT-MEMORY.md` l. 81 : « Manuel central EN + dérivations ada (2026-09-05). Pivot architectural : un manuel EN ~25k mots = source unique. FR/DE/ES/CN = dérivations ada. [...] Toute évolution doctrinale se fait dans le manuel, jamais dans une dérivation. »
- `AGENT-BRIEFING.md` l. 211 : « Perig est l'auteur. L'IA propose, Perig dispose. »
- `AGENT-BRIEFING.md`, règle 7 : projeter la mémoire des agents dans le dépôt versionné, car « un item non projeté ici n'existe pas pour les agents qui débarquent sans mémoire-sidecar ».
- `PILOTE-refs.md` l. 227-228 : citations avec glose de l'auteur et contre-lecture, à porter dans le manifest `.ada` comme « anti-hallucination natif ».
- Marquage d'importance ★★★ / ★★ / ★ et ⚡ dans `AGENT-MEMORY.md` et `AGENT-BRIEFING.md` (« Noyau non-ratable »).

## Fiches mémoire de Claude Code sur ada-format (backup Google Drive du 23 novembre 2026)

Rédigées par des agents ; elles consignent les décisions de Perig.

- `project_zip_architecture.md` (28 et 31 juillet 2026) : deux modes de création, champ `mode` du manifest. `encoded_from_source` (JP³.ada v1) et **`grown_from_deposits`** : « le `.ada` naît sans document source. Il s'accumule par dépôts éparpillés (idées, intuitions, captures) et cristallise progressivement en `prompt.md` structuré via dialogue socratique avec l'auteur. » Dossier `deposits/` : « dépôts bruts chronologiques (texte, transcription vocale, capture d'écran) horodatés ». `open_questions.md` : « questions socratiques en attente, générées par le LLM en réaction aux dépôts, à représenter à l'auteur à la prochaine session ». Le mode « est un état, pas une identité ». Pourquoi : « transforme `.ada` d'outil d'accès à la littérature en outil de création d'une littérature qui n'aurait pas existé sans lui ». Décision : pas de carnet global, un `.ada` par thème.
- `project_encoder_web_tool.md` (31 juillet 2026) : outil encodeur en HTML + JS statique, JSZip, clé API locale, provider agnostique (Gemini par défaut), mobile-first, PWA. Deux modes séparés : « Dépôt libre, zéro friction » et « "Interroge-moi" à la demande ». « trop de questions à chaud tue l'éclair ».
- `project_ada_encoder_device.md` (26 septembre 2026) : la priorité est « concevoir le dispositif qui permettra de les produire bien ». « Ada comme assistant maximaliste de l'auteur [...] L'agent ada comme partenaire socratique de l'auteur (pas seulement du lecteur). Renversement : ce qui rend le livre réactif aux lecteurs commence par rendre l'auteur réactif à l'étendue complète de ses futurs lecteurs. » Contrainte de méthode : concevoir le protocole « dans une session vierge de tout document source — sinon l'agent reproduit exactement le défaut qu'il cherche à corriger (les "personas universels" deviennent des personas du document en cours) ».
- `feedback_creation_ada_process.md` (26 septembre 2026) : ne jamais générer un `.ada` en une passe ; « Créer directement le zip à partir du source, c'est produire un PDF dans un zip ».
- `project_protocol_interview_personas.md` (27 septembre 2026, nuit) : renversement de Perig, « mesurer le plein, pas le vide ». Le mécanisme est **l'homologie** : le persona comprend s'il trouve un pont vers son vécu. Trois registres : SUIT (« ça ressemble à [homologie dans mon vécu] »), BLOQUE (« le pont manque entre [A] et [B] »), INCERTAIN (« je ne sais pas si quelqu'un comme moi connaîtrait [X] — est-ce que tu l'assumes ? »). Persona « élaboré mais non-spécifique » : structure cognitive, pas biographie (« personne dont la vie professionnelle était organisée autour du maintien de paramètres physiologiques stables dans des corps en état de crise »). Deux modes : Construction (de zéro) et Diagnostic (texte existant, annotations par paragraphe). « L'auteur arrive avec des réponses. Le logiciel l'aide à trouver toutes les questions. Le `.ada` contient les deux. » Brief complet : `ada-format/design/brief-encodeur-2026-09-27.md` (dossier local, absent de GitHub et du backup).
