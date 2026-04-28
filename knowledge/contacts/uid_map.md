# BST Cross-Source UID Map

This file is the authoritative mapping of every active BST employee across all
data sources Jack Bot reads from. The OOO matcher, daily synthesis, and any
future per-person resolver all key off this file rather than fuzzy-matching
names at runtime.

**Source of truth:** `knowledge/contacts/employees.md` (current roster).
**Generated from:** live pulls of Slack / Asana / Toggl / Rippling on 2026-04-27.
**Validation status:** Validated by Jack 2026-04-27.

A sibling `uid_map.json` will be generated from this file once validated; the
runtime reads the JSON. Manual fixes go directly in this `.md` and the
generator preserves them.

---

## Schema

Per person:
- `canonical_name` — the name we display in briefings (matches employees.md)
- `preferred_first` / `formal_first` / `last` — name parts (used to render and
  to disambiguate when a source uses one form vs the other)
- `primary_email` / `email_aliases` — Google Workspace identity
- `slack_user_id` — Slack `Uxxxx` id
- `asana_user_gid` — Asana numeric gid
- `toggl_user_ids` — list of Toggl numeric ids; usually only one is active but
  historical hours may sit under an older id, so we keep all known ids and
  union them when summing time
- `rippling_name` — exact `SUMMARY:` prefix Rippling uses in the PTO ICS
- `quickbooks_id` — TBD (not yet pulled — phase 1.5)

---

## Active Roster (13)

### Jack Elston — CEO
- `preferred_first`: Jack · `formal_first`: Jack · `last`: Elston
- `primary_email`: elstonj@blackswifttech.com
- `email_aliases`: jack.elston@blackswifttech.com
- `slack_user_id`: U01511MEQ90 (Slack display: "Jack")
- `asana_user_gid`: 12805370615958 (Asana display: "Jack Elston")
- `toggl_user_ids`: [1131025, 9847189]
- `rippling_name`: Jack Elston

### Maciej Stachura — CTO
- `preferred_first`: Maciej · `formal_first`: Maciej · `last`: Stachura
- `primary_email`: maciej.stachura@blackswifttech.com
- `email_aliases`: stachura@blackswifttech.com
- `slack_user_id`: U014U9WMK2A (Slack display: "Maciej")
- `asana_user_gid`: 12804950273833 (Asana display: "Maciej Stachura")
- `toggl_user_ids`: [9847188, 9846838]
- `rippling_name`: Maciej Stachura

### Alex Lomis — Software Engineer
- `preferred_first`: Alex · `formal_first`: Alex · `last`: Lomis
- `primary_email`: alex.lomis@blackswifttech.com
- `slack_user_id`: U058LGYMEQ0 (Slack display: "Alex Lomis")
- `asana_user_gid`: 1204607768706937 (Asana display: "Alex Lomis")
- `toggl_user_ids`: [9846764]
- `rippling_name`: Alex Lomis

### Ben Busby — Software Engineer
- `preferred_first`: Ben · `formal_first`: Ben · `last`: Busby
- `primary_email`: ben.busby@blackswifttech.com
- `slack_user_id`: U0151201DMY (Slack display: "Ben")
- `asana_user_gid`: 664838850096143 (Asana display: "Ben Busby")
- `toggl_user_ids`: [4852974]
- `rippling_name`: Ben Busby

### Joshua Fromm — Mechanical Engineer
- `preferred_first`: Josh · `formal_first`: Joshua · `last`: Fromm
- `primary_email`: josh.fromm@blackswifttech.com
- `slack_user_id`: U014ZL9FLE9 (Slack display: "Joshua Fromm")
- `asana_user_gid`: 338088218424389 (Asana display: "Josh Fromm")
- `toggl_user_ids`: [4548909]
- `rippling_name`: Joshua Fromm

### Sam Hild — Software Engineer
- `preferred_first`: Sam · `formal_first`: Sam · `last`: Hild
- `primary_email`: sam.hild@blackswifttech.com
- `email_aliases`: sam.hild@blackswifttechnologies.com
- `slack_user_id`: U06NQAYBLRK (Slack display: "Sam Hild")
- `asana_user_gid`: 1206802602679078 (Asana display: "Sam Hild")
- `toggl_user_ids`: [10582060, 10582079]
- `rippling_name`: Sam Hild

### Nate Straus — Shop Technician
- `preferred_first`: Nate · `formal_first`: Nathaniel · `last`: Straus
- `primary_email`: nate.straus@blackswifttech.com
- `slack_user_id`: U06B7GNFV0W (Slack display: "Nate")
- `asana_user_gid`: 1206232492438833 (Asana display: "Nate Straus")
- `toggl_user_ids`: [10187361]
- `rippling_name`: Nathaniel Straus  ← the mismatch that caused the 2026-04-27 OOO miss

### Meredith Needham — Office Admin
- `preferred_first`: Meredith · `formal_first`: Meredith · `last`: Needham
- `primary_email`: meredith.needham@blackswifttech.com
- `slack_user_id`: U06KRHPQSRH (Slack display: "Meredith Needham")
- `asana_user_gid`: 1206646853646674 (Asana display: "Meredith O'hara Needham"; we display as "Meredith Needham")
- `toggl_user_ids`: [10410463]
- `rippling_name`: Meredith Needham

### Kareem Ahmed — Graphics & Communications
- `preferred_first`: Kareem · `formal_first`: Kareem · `last`: Ahmed
- `primary_email`: kareem.ahmed@blackswifttech.com
- `slack_user_id`: U07SN02GM5K (Slack display: "Kareem")
- `asana_user_gid`: null (intentional — no Asana seat for Kareem)
- `toggl_user_ids`: [11418820]
- `rippling_name`: Kareem Ahmed (inferred — no PTO event yet to verify exact string; will auto-verify on first event)

### Paige Smith — Communications & Digital Marketing
- `preferred_first`: Paige · `formal_first`: Paige · `last`: Smith
- `primary_email`: paige.smith@blackswifttech.com
- `slack_user_id`: U083AAM8E9Y (Slack display: "Paige Smith")
- `asana_user_gid`: 1208887458958663 (Asana display: "Paige Smith")
- `toggl_user_ids`: [11568823]
- `rippling_name`: Paige Smith

### Ethan Domagala — Intern
- `preferred_first`: Ethan · `formal_first`: Ethan · `last`: Domagala
- `primary_email`: ethan.domagala@blackswifttech.com
- `slack_user_id`: U06CCFTNBS6 (Slack display: "Ethan")
- `asana_user_gid`: 1206276365680911 (Asana display: "Ethan Domagala")
- `toggl_user_ids`: [10186372]
- `rippling_name`: Ethan Domagala

### Beck Cotter
- `preferred_first`: Beck · `formal_first`: Beck · `last`: Cotter
- `primary_email`: beck.cotter@blackswifttech.com
- `slack_user_id`: U07FN4QSNDN (Slack display: "Beck")
- `asana_user_gid`: 1208001716965280 (Asana display: "Beck Cotter")
- `toggl_user_ids`: [11266515]
- `rippling_name`: Beck Cotter

### Dan Prendergast
- `preferred_first`: Dan · `formal_first`: Daniel · `last`: Prendergast
- `primary_email`: daniel.prendergast@blackswifttech.com
- `slack_user_id`: U04CZK4K7P0 (Slack display: "Daniel Prendergast")
- `asana_user_gid`: 1203468561261344 (Asana display: "Dan Prendergast")
- `toggl_user_ids`: [9846878]
- `rippling_name`: Daniel Prendergast

---

## Decisions of record (validated 2026-04-27)

- Multi-Toggl-ID people (Jack, Maciej, Sam): keep all ids and union their
  hours when summing time. Usually one is dormant, but historical entries can
  live under the older id.
- Kareem has no Asana seat (intentional — no Asana-driven tasks expected).
- Kareem's Rippling name is currently inferred; auto-verify on first PTO event.
- Meredith displays as "Meredith Needham" even though Asana stores
  "Meredith O'hara Needham".
- Dan Prendergast displays as "Dan" (preferred), not "Daniel".
- Alec Mallinger is a former employee — excluded from the active map even
  though his Toggl and Rippling records still exist.

---

## Roster sanity check
- 13 names in `employees.md` → 13 entries above.
- All 13 have Slack + Toggl ids confirmed.
- 12 of 13 have Asana ids (Kareem flagged above).
- 12 of 13 have a known Rippling name (Kareem inferred).
