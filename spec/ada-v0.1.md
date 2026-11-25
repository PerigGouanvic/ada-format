# The .ada format, version 0.1 (draft)

Status: **draft, November 2026.** This specification describes the format as
it was first used in practice, in
[`jp3.ada`](https://github.com/PerigGouanvic/JP3/blob/main/jp3.ada)
(26 September 2026), and makes explicit what that file left implicit.
Points marked **[H]** are hypotheses to test; points marked **[JP³]** describe
what `jp3.ada` actually does.

## 1. Purpose

An `.ada` file lets an author hand a reader a single file that any
general-purpose AI assistant can turn into a conversation with the document:
answering questions, adapting depth, vocabulary and language to the reader,
citing the author's sources, and helping the reader write back to the author.
No software is needed beyond the assistant itself.

## 2. Container

An `.ada` file is a **zip archive** of plain text files, with the extension
`.ada`. **[JP³]** Like a `.docx`, it is a container: the parts are readable one
by one, but the file is meant to be handed whole to an AI.

| Path in the archive | Required | Role |
|---|---|---|
| `manifest.json` | yes | Metadata: format version, subject, author, language, mode, feedback channel, citations. |
| `ada-usage.md` | yes | Instructions for the AI that opens the file (the "host AI"). |
| `prompt.md` | yes, once crystallised | The core content, written for the host AI. May be absent or partial while a file is growing (see §2.3). |
| `open_questions.md` | no | Socratic questions: to the reader in a finished file, to the author while the file grows (see §6). |
| `deposits/` | in `grown_from_deposits` mode | Raw, dated deposits from the author (see §2.3). |
| `source/` | recommended | The original text, unchanged (for example `source/article.md`). See §5.1. |
| `attachments/` | no | Complementary reference documents. |
| `media/` | no | Images, diagrams. |

All text files are UTF-8. Markdown is the expected format for `.md` files.

**[H]** Delivery is a single file because `ada-usage.md` travels inside the
archive. Whether every assistant actually reads `ada-usage.md` first, without
being told to, still has to be tested. Until then, the person sending the file
may add one line such as: *"This is an .ada file: unzip it and follow
ada-usage.md."*

### 2.1 Distribution and file type

Phones and many desktop systems decide how to open a file from its extension
and declared media type, not from its content. An archive named `.ada` is
therefore not recognised as a zip, and no application is offered to open it.
**[JP³]** This happened on a phone with `jp3.ada`. `.epub` and `.docx` have the
same problem, solved by registered media types that `.ada` does not have.

There is a second collision: `.ada` is already the usual extension for source
code in the Ada programming language, and some systems map it to a text or
source-code type.

Until this is settled, v0.1 recommends:

1. **Publish two copies**: `name.ada` (the canonical file) and `name.ada.zip`
   (byte-identical, for phones and for systems that only recognise `.zip`).
   Both are conforming `.ada` files.
2. **Serve with `Content-Type: application/zip`** when publishing on the web.
   **[H]** A dedicated type (for example `application/vnd.ada+zip`) would only
   be useful once registered with IANA and known to operating systems; it is
   not used in v0.1.
3. **Most assistants accept a zip upload directly**, so the reader does not
   need to unzip anything; what matters is that the file can be picked and
   attached.

Whether to keep `.ada` as the extension at all, given the collision with the
Ada language, is an open question for v0.2.

### 2.3 Two ways a file comes into being

The `mode` field of the manifest (§3) records how the content came about.
These two modes were set by the author of the format in July 2026, before the
first file was made; `jp3.ada` uses the first.

- **`encoded_from_source`**: an existing text is turned into an `.ada`. The
  original goes in `source/`; `prompt.md` is written from it.
- **`grown_from_deposits`**: the file is born **without a source text**. The
  author drops ideas, intuitions, voice transcriptions and screenshots into
  `deposits/`, as they come. Between deposits, the AI acts as the author's
  Socratic partner: it reacts to what was deposited with questions, kept in
  `open_questions.md` to be put back to the author at the next session. Over
  these exchanges the material **crystallises** into `prompt.md`.

The mode is a **state, not an identity**: a file grown from deposits can later
be published and read like any other, and an encoded file can keep receiving
deposits. The design rationale is that `.ada` should be a tool for writing a
literature that would not have existed without it, not only a tool for
accessing existing texts. One `.ada` per theme, not one global notebook.

Deposits are named so that their order is clear, for example
`deposits/2026-07-28T14-05_idea.md` or `deposits/2026-07-28_voice.txt`;
images and other files may sit next to them. **[H]** A deposit is never edited
after the fact; corrections are new deposits.

**[H]** A growing file is a working file for its author. It conforms to v0.1
(§7) without `prompt.md`, but should not be handed to readers until
`prompt.md` exists.

## 3. `manifest.json`

Validated by [`manifest-v0.1.schema.json`](manifest-v0.1.schema.json).

### 3.1 Fields used by `jp3.ada`

| Field | Required | Meaning |
|---|---|---|
| `format_version` | yes | `"0.1"`. |
| `subject` | yes | Title or subject of the document. |
| `author` | yes | Author's name (string). |
| `language` | yes | Language of the content, as a BCP 47 tag (`fr`, `en`, `fr-CA`). |
| `created` | no | Date of creation, `YYYY-MM-DD`. |
| `mode` | no | How the content came about (§2.3): `encoded_from_source` **[JP³]** or `grown_from_deposits`. It may change over the life of a file. |
| `feedback` | no | Return channel to the author, keyed by kind of message. **[JP³]** uses `feedback.text = {method: "mailto", target: "<address>"}`. **[H]** `method` may also be `url` (a form or an issue tracker). |
| `citations` | no | Sources the author vouches for: `{id, bibliography, doi?, url?, supports_claims[]}`. |

**About `supports_claims`.** **[JP³]** In `jp3.ada` these are keywords
(`"soléaire"`, `"glycémie"`) that let the host AI match a source to a passage
of `prompt.md`. They are not identifiers of formal claims. v0.1 keeps them as
keywords.

### 3.2 Optional fields added by v0.1 **[H]**

All optional, so `jp3.ada` stays valid as is.

| Field | Meaning |
|---|---|
| `version` | Version of the document itself, independent of the format. |
| `license` | License of the content (for example `CC-BY-4.0`). |
| `source` | `{uri?, citation?}`: where the original text is published. |
| `encoded_by` | `{who, method}` with `method` in `human`, `ai-assisted`, `ai`. Strongly recommended when the encoder is not the author. |
| `claims` | Claims with an explicit epistemic status: `{id, text, status, citations[]}`, `status` in `established`, `argued`, `hypothesis`, `speculative`; `citations` refers to `citations[].id`. |

Unknown fields are allowed, so authors can experiment. Fields starting with
`x_` are reserved for that use.

## 4. `ada-usage.md`

Instructions to the host AI. A reference text, in French, is provided in
[`templates/ada-usage.md`](templates/ada-usage.md); an archive may copy it as
is or adapt it.

**[JP³]** The first version, in `jp3.ada`, asked the host AI to *adapt*
(answer in the reader's language), *answer* (drawing on `prompt.md`), *cite*
(`citations[]`), *question* (`open_questions.md`) and *pass on* (help the
reader write to the author). Testing with a real reader (DeepSeek, November
2026) showed that this wording pushed the AI into a commentator's role: it kept
talking about "the author" and "the manual", gave long answers, and talked more
than it listened.

The reference text therefore sets the following rules.

1. **Speak in the author's place.** The host AI stands in for the author in a
   conversation the author cannot have with every reader. It speaks as the
   author would, in the first person when natural, and does not refer to "the
   author", "the document" or "the manual".
2. **Listen first, answer short.** Open with a sentence or two and a short
   question about who the reader is and what they want. Keep answers to a few
   sentences unless the reader asks for more. The reader should talk more than
   the AI.
3. **Invite to try, never require.** When the content is something one can do
   (a movement, an exercise, a method), offer to try it right away, during the
   conversation. A reader who is only curious, or has technical questions,
   can stay in the conversation without trying anything.
4. **Stay faithful, in the author's voice.** Draw on `prompt.md` and
   `source/`; when going beyond them, say so in the author's voice ("I haven't
   written about that, but…"). A hypothesis stays a hypothesis. Sources from
   `citations[]` are mentioned when they matter, not at every sentence.
5. **Be honest about what it is.** If the reader asks who they are talking to,
   or seems to believe they are talking with the author in person, the AI says
   it is an AI speaking on the author's behalf from this file, and offers the
   feedback channel to reach the author.
6. **Adapt and pass on**, as in `jp3.ada`: answer in the reader's language;
   offer `open_questions.md` one question at a time; offer once to help draft a
   message to the author, which the reader alone decides to send.

**[H]** Rule 1 is the default. An author who prefers a guide speaking *about*
the work (for example for a third-party encoding, where speaking in the
author's place would be presumptuous) says so in `prompt.md`.

## 5. `prompt.md`

The core content, written by the author (or encoder) for the host AI, not for
the reader directly. It is free Markdown. **[JP³]** `prompt.md` in `jp3.ada` is
organised as follows, and v0.1 recommends that shape without requiring it:

- **What it is**: a summary and the central idea, in plain terms.
- **Reader profiles**: one section per anticipated reader ("for the reader who
  has no time", "for the scientist", "for the health practitioner"...), each
  saying what matters to that reader, what to start with and what to avoid.
  These are hints; the host AI will meet readers the author did not imagine.

  The author's interview protocol (September 2026) recommends defining
  readers by **cognitive structure rather than biography**: not "a retired
  nurse", but "someone whose working life was organised around keeping
  physiological parameters stable in bodies in crisis". What makes such a
  reader understand is **homology**, a bridge from the text to something in
  their own experience. While preparing `prompt.md`, each simulated reader
  reports in three registers: *follows* ("this is like [something I have
  lived]"), *blocked* ("the bridge between [A] and [B] is missing") and
  *unsure* ("I don't know if someone like me would know [X]: do you assume
  it?"). The protocol measures what is there, not only what is missing.
- **What it is not**: the misreadings the author has already met.
- **Destination**: where the author hopes the reader ends up.

Other elements v0.1 recommends including when they apply **[H]**:

- **Intent**: what the reader should come away with, including points no
  adaptation may drop.
- **Concepts and prerequisites**: key terms and what must be understood first.
- **Objections and replies**: questions the author has met, with the author's
  answers.
- **Voice**: how the author speaks (tone, words they use or avoid), what
  must be kept, what may be adapted (vocabulary, length, examples, language),
  and what must never be said in the author's name.
- **Difficult passages**: where readers are likely to get stuck, and what
  helps (a diagram, an example, a timeline).

### 5.1 `prompt.md` and the original text

`prompt.md` is a rewriting of the work for the AI. Since a rewriting can drift,
an archive **should** also carry the original text, unchanged, in `source/`
(Markdown or plain text preferred; one file per part of a long work). The host
AI then has both: `prompt.md` says how to approach the work and its readers,
`source/` says exactly what the author wrote, and the reader can ask to see the
original passage.

**[H]** When the two differ on what the author claims, the original wins, and
the host AI tells the reader about the difference. `jp3.ada` does not yet
include its original article; adding it is the first update to make.

## 6. `open_questions.md`

Socratic questions, whose addressee depends on the state of the file.

- **In a finished file** **[JP³]**: a numbered list of questions addressed
  **to the reader**, meant to open the dialogue ("Which activity of your daily
  life could become a session without any change on your part?"). They are not
  FAQ entries: they invite the reader to think, not to receive an answer.
- **While the file grows** (`grown_from_deposits`): questions the AI generated
  in reaction to the deposits, waiting to be put **to the author** at the next
  session. Once answered, they feed `prompt.md`.

**[H]** When a file holds both kinds, the author's questions go under a
separate heading (for example `## For the author`), which the host AI never
puts to readers. The author arrives with answers; the AI helps find all the
questions; the file keeps both.

## 7. Conformance

A file conforms to v0.1 if:

1. it is a valid zip archive with the extension `.ada` or `.ada.zip`;
2. it contains `manifest.json` and `ada-usage.md` at its root, and either
   `prompt.md`, or (in `grown_from_deposits` mode) a non-empty `deposits/`;
3. `manifest.json` validates against `manifest-v0.1.schema.json`;
4. every `claims[].citations` entry, if present, names an existing
   `citations[].id`.

An archive without `source/` still conforms; the validator notes its absence.

[`tools/validate_ada.py`](../tools/validate_ada.py) checks all four:

```
python3 tools/validate_ada.py path/to/file.ada
```

`jp3.ada` passes, with a note that it has no `source/`.

## 8. Open questions for v0.2

- **Source precedence.** Test on real readings whether the rule of §5.1
  (the original wins over `prompt.md`) holds, or whether some rewritings are
  meant to correct the original.
- **Structured layer.** Should a machine-readable `structure.yaml`
  (sections, concepts, claim status, anticipated questions) sit next to
  `prompt.md`? A first draft is in
  [`proposals/v0.2-structured/`](proposals/v0.2-structured/).
- **Encoding device.** v0.1 says what a file contains, not yet how an author
  produces it. The author's own design (July and September 2026) sets the
  direction: never produce an `.ada` in one pass ("creating the zip directly
  from the source is making a PDF in a zip"); a deposit mode with zero
  friction, separate from an "interview me" mode on demand; simulated readers
  defined by cognitive structure. Its full brief has not been published yet.
- **Extension and media type.** Keep `.ada` despite the Ada language, or
  move to another extension; register a media type or not (see §2.1).
- **Long works.** One archive per work, or per chapter with an index?
- **Integrity.** How a reader can check that the file matches what the author
  published (a hash, a signature).
- **Third-party encodings.** What credit and permission `encoded_by` should
  imply when the encoder is not the author.
