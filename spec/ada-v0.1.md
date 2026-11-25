# The .ada format, version 0.1 (draft)

Status: **draft, November 2026.** Nothing here is frozen. Every choice marked
**[H]** is a working hypothesis that the first real encodings (starting with
JP³) are meant to confirm or overturn.

## 1. What v0.1 is for

v0.1 has one job: let an author hand a reader a file that any general-purpose
AI assistant (Claude, ChatGPT, Mistral, a local model) can turn into a
conversation with the document, **without any software beyond the assistant
itself**.

So v0.1 deliberately leaves out what the manifesto imagines for later
(per-sentence metadata, complexity matrices, native platform support). It keeps
only what a decoder needs to answer questions faithfully.

Three design rules follow from that job:

1. **The source text stays the authority.** Every adaptation is a reading of
   the source, never a replacement for it. If a reformulation and the source
   disagree, the source wins.
2. **Plain YAML, readable by people and by models.** No binary, no container,
   no custom syntax. **[H]** Current assistants read YAML reliably and it is
   easier for authors to edit by hand than JSON.
3. **Almost everything is optional.** A valid file can be tiny. Richer fields
   improve the reading but are never required.

## 2. Files

A v0.1 delivery is two files, as announced in the manifesto:

| File | Role |
|---|---|
| `something.ada` | The document: source text plus the structure an author adds. YAML, UTF-8. |
| `decoder-v0.1.md` | The decoding prompt that tells the reader's AI how to use the file. See [`prompts/decoder-v0.1.md`](../prompts/decoder-v0.1.md). |

**[H]** A file may also embed the decoding prompt in its `decoder.prompt`
field, so that a single attachment is enough. Whether single-file delivery is
reliable across assistants is one of the first things to test.

The machine-checkable schema is [`ada-v0.1.schema.json`](ada-v0.1.schema.json)
(JSON Schema 2020-12, applied to the parsed YAML).

## 3. Structure at a glance

```yaml
ada: "0.1"          # required: format version
meta: { ... }       # required: title, language, authorship, source, license
intent: { ... }     # optional: what the document is trying to do, for whom
concepts: [ ... ]   # optional: key terms, definitions, prerequisites
sections: [ ... ]   # required: the text itself, in reading order
questions: [ ... ]  # optional: questions the author expects, with pointers
decoder: { ... }    # optional: fidelity rules and the embedded prompt
feedback: { ... }   # optional: how readers can write back to the author
```

## 4. Fields

### 4.1 `ada` (required)

The string `"0.1"`.

### 4.2 `meta` (required)

| Field | Req. | Meaning |
|---|---|---|
| `title` | yes | Title of the document. |
| `language` | yes | BCP 47 tag of the source text (`fr`, `en`, `fr-CA`). |
| `authors` | no | List of `{name, contact?}`. |
| `version` | no | The document's own version, independent of the format version. |
| `date` | no | Date of this version (`YYYY-MM-DD`). |
| `license` | no | License of the content (for example `CC-BY-SA-4.0`). |
| `source` | no | Where the text comes from. `kind` is `original` (written by the author of this file) or `encoded` (someone else's text, encoded by a third party). `uri` and `citation` locate the original. |
| `encoded_by` | no | Who did the encoding and how (`human`, `ai-assisted`, model names). Required in spirit when `source.kind` is `encoded`. |

### 4.3 `intent` (optional)

What the author wants the reader to come away with. This is what lets a
decoder distinguish "a simpler version" from "a different message".

| Field | Meaning |
|---|---|
| `central_question` | The question the document answers. |
| `thesis` | The answer, in two or three sentences. |
| `must_keep` | Points that no adaptation may drop or soften, however short or simple. |
| `audiences` | Reader profiles the author anticipated: `{id, label, wants?, start_with?, notes?}`. `start_with` lists section ids. |

**[H]** Audiences are hints, not a closed list. The decoder is expected to meet
readers the author never imagined.

### 4.4 `concepts` (optional)

Key terms the reader may need.

| Field | Req. | Meaning |
|---|---|---|
| `id` | yes | Stable identifier, `snake_case`. |
| `term` | yes | The term as it appears in the text. |
| `definition` | yes | The author's definition, in the author's words. |
| `plain` | no | A plain-language definition the author approves. |
| `requires` | no | Ids of concepts to understand first. This list is the dependency graph. |
| `examples` | no | List of `{text, for?}`; `for` names an audience id. |
| `not_to_confuse_with` | no | Neighbouring ideas readers often mix up with this one. |

### 4.5 `sections` (required, at least one)

The document in reading order. Each section carries the source text and,
optionally, what the author knows about how it is read.

| Field | Req. | Meaning |
|---|---|---|
| `id` | yes | Stable identifier. |
| `title` | no | Heading. |
| `text` | yes | The source text of the section, verbatim. Markdown allowed. |
| `role` | no | One of `context`, `claim`, `argument`, `evidence`, `example`, `objection`, `reply`, `method`, `conclusion`, `aside`. |
| `summary` | no | One to three sentences, written or approved by the author. |
| `levels` | no | Author-approved reformulations keyed by level: `plain`, `standard`, `expert`. |
| `uses` | no | Concept ids this section relies on. |
| `claims` | no | The section's assertions as `{id, text, status, sources?}`. `status` is `established`, `argued`, `hypothesis` or `speculative`. |
| `difficulties` | no | Known stumbling points: `{what, why?, help?}`. |
| `links` | no | Relations to other sections: `{to, relation}` where `relation` is `supports`, `answers`, `contradicts`, `illustrates`, `extends` or `see_also`. |

**[H]** Three named levels instead of the "3 to 5 complexity levels" of the
manifesto. A model can interpolate between three anchors; more fixed levels
multiply the author's work without a demonstrated gain.

### 4.6 `questions` (optional)

Questions the author expects, with the parts of the text that answer them.

```yaml
questions:
  - q: "Isn't this just a summary tool?"
    answer: "No: a summary replaces the text; an .ada reading keeps going back to it."
    see: [s3, s5]
```

`answer` is optional. When it is absent, the decoder answers from the
sections listed in `see`.

### 4.7 `decoder` (optional)

Instructions that bind the reader's AI for this document.

| Field | Meaning |
|---|---|
| `voice` | How the document should speak (`first_person_author`, `neutral_guide`, `tutor`). Default: `neutral_guide`. **[H]** "The document's voice" is attractive but can make a model put words in the author's mouth; a neutral guide is the safer default. |
| `default_entry` | Section id to start from when the reader gives no direction. |
| `rules` | Extra rules in plain language, added to the decoding prompt. |
| `prompt` | Optional embedded copy of the decoding prompt (see §2). |

### 4.8 `feedback` (optional)

The return channel from reader to author, which the README lists as a core
feature.

| Field | Meaning |
|---|---|
| `contact` | Where messages go (email, form URL, issue tracker). |
| `invite` | `true` if the decoder should offer, at the end of a reading or when the reader hits a wall, to draft a message to the author. |
| `ask_for` | What the author wants to hear about (`unclear_passages`, `missing_examples`, `disagreements`, `errors`). |

The decoder only **drafts**. The reader reviews and sends, or not. No data
leaves the conversation on its own.

## 5. Decoding contract

Whatever prompt is used, a v0.1 decoder must:

1. **Start from the reader.** Ask briefly what they want and how they like to
   read, unless they already said so, then adapt.
2. **Stay inside the source.** Answer from `sections`, `concepts` and
   `questions`. When going beyond the text (outside knowledge, extrapolation,
   the reader's own context), say so explicitly.
3. **Keep the epistemic status.** A `hypothesis` stays a hypothesis at every
   level of simplification. Every point in `intent.must_keep` survives.
4. **Point back.** Name the section an answer comes from, so the reader can
   check the original text.
5. **Offer the return channel** when `feedback.invite` is true.

## 6. Conformance

A file conforms to v0.1 if it parses as YAML, validates against
`ada-v0.1.schema.json`, and every id it references (`uses`, `requires`,
`start_with`, `see`, `links.to`, `default_entry`) exists in the file. The
schema checks the first two points; [`tools/validate.py`](../tools/validate.py)
checks all three:

```
python3 tools/validate.py examples/manifesto-excerpt.ada
```

Top-level keys starting with `x_` are reserved for experiments and ignored by
conforming decoders. Any other unknown top-level key makes the file invalid.

## 7. Open questions for v0.2

- **Long texts.** JP³ will show whether one file per document holds up, or
  whether long works need one file per chapter plus an index.
- **Encoding prompt.** v0.1 specifies what a file contains, not yet the
  interview through which an author produces it.
- **Multilingual files.** Is a translation a level, a separate file, or a
  `translations` field?
- **Integrity.** How a reader can verify that `text` really matches the
  published original (a hash of the source, a signature).
- **Third-party encodings.** What `source.kind: encoded` should require in
  terms of credit and permission (see the copyright questions in Appendix E
  of the manifesto).
- **Raw readability.** The manifesto says a real `.ada` file is unreadable in
  raw form. v0.1 takes the opposite bet: a readable file that is still rich
  enough to drive adaptation. To be decided by use, not by principle.
