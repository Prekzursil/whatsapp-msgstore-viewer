# WMV Modernization — Grill Decision Queue

## RESOLVED DECISIONS (owner grill, 2026-09-30)

- G-1 (T0): fork = DAILY DRIVER; upstream PRs bonus-only. LOCKED.
- G-2 (T0): M3 restyle + UX craft pass, Figma-first, KivyMD 2.0. LOCKED.
- Tier-1 scope-inclusion [0.0]-[0.9]: **ALL TEN IN** (owner: 'do all in'). Writer (0.8) + acquisition assistant (0.9) sequenced late; stats after big five; HTML+CSV export first, PDF later.
- IG program redirected separately (untouchable phone account; session-only; rotator; bypass research authorized).


Generated wf_e380d2e5-4c2 (7 lenses + structure, 2026-09-30). Tier 0 status: G-2 LOCKED (M3+UX craft pass); G-1 + IG-1 pending owner.

## Strongest cross-lens signals

- FTS5 search + ONE shared filter grammar + jump-to-context: 4 lenses (L1, L3, L5, L6) — the strongest scope signal in the queue; every lens that touched retrieval independently rejected the commissioned LIKE-scan verb.
- Canonical archive store + idempotent multi-source merge + backup diff: 4 lenses (L1, L2, L3, L6) — includes deleted-for-everyone detection and the pre/post-merge zero-loss proof the owner's live iCloud-to-Android merge loop needs right now.
- Windowed/keyset data access is the load-bearing primitive: L1 explicit, and both L5 (virtualized lists) and L6 (bounded MCP payloads) silently assume it — at 600K messages nothing works without it, so it gates three categories at once.
- Schema-currency: versioned fixtures + doctor coverage gate: 3 lenses (L2, L3, L4) — also the honest precondition for the commissioned 100% coverage, since real archives can never ship into CI.
- Completed message model / typed rendering (sender attribution, reactions, edits, system events): 3 lenses (L1, L2, L5) — every stat, per-sender filter, and 'reads like real WhatsApp' claim silently depends on it.
- Media layer (gallery + integrity audit + perceptual dedupe + organized export): 3 lenses (L1, L3, L5) — the first thing phone merges silently orphan.
- Offline/no-egress as an ENFORCED guarantee rather than a claim: 2 lenses (L4, L7), independently designed from different angles (crash redaction vs frozen-import gates).
- HIGHEST-TENSION FORK (not consensus): L1/L2/L3 designed a plaintext canonical store; L7 independently designed an encrypted vault + portable bundle — never reconciled. The safety-data storage-architecture item exists to force that reconciliation before ingest is built.
- Sequencing divergence inside agreement: three lenses each claim their layer must be built FIRST (L1 pagination, L4 harness, L5 theme tokens) — they agree on substrate-first but conflict on which substrate, so the grill must pick ONE order and lock it.
- Two owner-relayed items sit OUTSIDE the lens outputs and must not be lost in the merge: (1) native install detached from the terminal — pre-decided, start immediately, only the HOW is open; (2) Instagram session persistence — a NEW second-program boundary needing an explicit greenlight + timing decision, with the honest caveat that fast re-access is deliverable but never-logout is not guaranteeable against Meta-side invalidation.

## scope-inclusion

### Q1. Wave-1 blocker: rebuild the data layer as a keyset-paginated windowed core — page by composite (timestamp,_id), bidirectional loads, jump-to-date, jump-to-quoted, virtualized chat list — replacing fetch_chat()'s unbounded fetchall()?
- BEST — Full windowed core + jump-to-date + jump-to-quoted + scrubber/mini-timeline, shared by GUI and CLI (--around-date, --limit). Upside: kills the 50-150K-message freeze/OOM; 'I know it was around March 2023' becomes solvable; MCP bounded payloads and list virtualization consume the same primitive. Downside: touches every data path; timestamp-tie/ms-collision correctness needs the composite key; all three schema adapters must implement it; nothing visually new ships for the first work-units.
- VIABLE — Minimal LIMIT pagination only, no jumps. Upside: small diff, fast. Downside: OFFSET degrades on deep pages; jump navigation gets reworked later.
- WORST — Defer, keep fetchall. Upside: zero effort. Downside: one big group freezes the app; search-jump, reply-jump and agent pagination all build on sand.

**Recommendation:** Option 1, wave 1, before any restyle work — it is the substrate items in three other categories silently assume.

**Downside of rec:** Highest upfront cost with no visible feature to show for it; keyset bugs (ties, millisecond collisions, schema drift across v1/v2/v3) are subtle and only surface on real huge chats; KivyMD list virtualization must be verified to actually release off-screen data, not just hide it.
**Convergence:** L1 explicit; L5 (virtualization) and L6 (bounded MCP payloads) silently assume it

### Q2. Does the app become a cumulative archive system — one canonical store (own SQLite, never writing sources) with idempotent multi-backup ingest, cross-source merge/dedup with per-message provenance, and a diff engine ('what disappeared between two backups', pre/post-merge zero-loss proof) — or stay a single-msgstore viewer?
- BEST — Canonical store + merge (identity key chat_jid + timestamp-bucket + body-hash|media-pHash, report-only dry-run default, sources never mutated) + `diff` verb with 0/1/2 exit-code contract + deleted-for-everyone detection. Upside: memory between weekly backups; proves silent WhatsApp history rewrites; the owner's live iCloud-to-Android merge loop needs exactly the pre/post diff; every downstream stat/search/media feature queries one store. Downside: false merges silently poison all downstream numbers; highest-effort item; schema drift multiplies ingest adapters; store needs a compaction story.
- VIABLE — Store + idempotent ingest + diff, but NO cross-source identity matching (per-source append with provenance only). Upside: removes the false-merge risk entirely; still detects deletions within one source lineage. Downside: overlapping phone-era years stay double-counted; the owner's actual cross-phone merge stays unsolved.
- WORST — Stay a one-db viewer. Upside: smallest scope. Downside: no memory between sessions; 'what disappeared since last time' unanswerable; two open-source competitors already ship merge.

**Recommendation:** Option 1 with conservative score thresholds, dry-run default, and the diff engine landed before merge ever writes.

**Downside of rec:** Identity matching is heuristic; a wrong merge is worse than no merge because it silently corrupts the historical record the program exists to keep; it is the single highest-effort commitment on this queue and drags a synthetic-fixture factory with it.
**Convergence:** L1 (ingest + deleted-diff), L2 (incremental merge preserving deleted), L3 (merge identity ledger + fixture factory), L6 (diff engine + MCP diff tool)

### Q3. Is search an engine, not a verb: FTS5 sidecar index (diacritic/emoji-tolerant tokenizer + trigram lane for typos/substrings), structured filters (chat, sender, from_me, date range, media type), ONE closed versioned filter grammar shared by CLI, GUI, and MCP, and every hit jumping to the message in context?
- BEST — FTS5 + trigram lane + shared DSL + context-jump deep links (wmv://chat/<id>/jump/<msg_id>, +/-15-message window, highlight pulse). Upside: at 600K messages retrieval IS the app; one parser kills the classic three-transport drift bug class; the deep-link mechanism is reused by reply-jump. Downside: tokenizer choice is load-bearing (wrong pick = silent zero hits for Romanian/Arabic users the README already documents); index build needs progress UI and transactional reindex sync or results go stale silently.
- VIABLE — FTS5 core with basic filters for CLI+GUI only; DSL/MCP sharing deferred. Upside: ships the 80% need fast. Downside: MCP and palette later grow their own query semantics — the drift bug class returns.
- WORST — LIKE-scan search verb as originally commissioned. Upside: trivial. Downside: full-table scan per query at 600K rows is unusable in GUI; grep, not a power tool.

**Recommendation:** Option 1 — one grammar and one index from day one, three consumers.

**Downside of rec:** The versioned grammar is a permanent commitment: every future transport must compile through it; the trigram lane roughly triples index size; FTS5 config drift across SQLite versions needs a pinned pragma check in CI.
**Convergence:** L1 (FTS5 + filters + jump), L3 (faceted FTS5 + conversation pivot), L5 (search-as-you-type + deep link), L6 (closed DSL shared across transports)

### Q4. Complete the message model (per-sender attribution in groups, replies, edits+history, reactions, deleted-for-everyone vs deleted-locally — render BOTH when the row survives, voice notes with waveform, stickers, polls, calls, system events) and render it as real WhatsApp-style bubbles?
- BEST — Full typed render_model layer (kivy-free) + M3 bubble family designed in Figma first + per-schema golden-row fixtures. Upside: biggest single perceived-quality delta; groups stop being anonymous; surfacing delete-for-everyone originals is a viewer superpower the phone UI lacks; every stat and per-sender filter depends on this model. Downside: reactions/edit/system tables are undocumented reverse-engineered surface — coverage varies by schema and must degrade visibly (NOT-CHECKED, never silently absent); PTT waveform blob format is undocumented.
- VIABLE — Model completion in the data layer + minimal rendering (text + replies + sender). Upside: unlocks stats/filters without UI risk. Downside: the 'reads like real WhatsApp' felt win is deferred; two passes over the same tables later.
- WORST — Keep current dump-style rendering. Upside: none. Downside: app stays a database viewer; group archives stay anonymous and useless.

**Recommendation:** Option 1, with scroll smoothness at 50k+ messages made an explicit measured acceptance criterion in the FIRST UI work-unit, not discovered at the end.

**Downside of rec:** Highest UI-risk item: if Kivy virtualization cannot hold smooth scrolling on huge chats, parts of the bubble work must restart on a different widget strategy; sender resolution for legacy messages may be partial (participant hashes rotate), so some history stays less-attributed than the UI implies.
**Convergence:** L1 (completed message model), L2 (row-type coverage incl. reactions/polls/view-once), L5 (typed event rendering)

### Q5. Include the full media layer — per-chat gallery + lightbox (zoom, filmstrip, playback, export-this), cross-chat integrity audit (missing/orphan/duplicate by content hash, reconciled both directions against the WhatsApp media dir), pHash near-dup clusters, organized bulk export (chat/year/month tree + manifest mapping every file to its message id)?
- BEST — Full media layer, phased internally: audit engine first, gallery/lightbox second. Upside: media is most of a 13-year archive's bytes and nearly all its nostalgia value; the audit is the precondition for any sane backup strategy (the owner's documented merge pain); 'hand someone all 2022 photos from that group' is a first-week ask. Downside: hashing tens of GB needs streaming + (path,size,mtime) cache; file_path semantics drift across schema versions; Kivy codec coverage (ffpyplayer pin) and missing-media placeholder design are real work.
- VIABLE — Audit + organized bulk export only; gallery/lightbox in a later wave. Upside: the data-safety half lands early with less UI risk. Downside: the most visible polish item waits; owners judge archives by their photos.
- WORST — Inline media links as today. Upside: none. Downside: broken thumbnails stay undiagnosable; phone merges keep silently orphaning files.

**Recommendation:** Option 1 with the internal audit-first phasing; hold the line at audit+gallery+export — no media ML, no graphs-of-graphs.

**Downside of rec:** It is a scope-creep magnet (EXIF, re-share graphs, reclaim lists each beg to join); pHash false-pairs on generic screenshots mean clusters must stay advisory and never auto-delete; newer crypt15-without-folder backups keep media inside encrypted packages, capping coverage for some users.
**Convergence:** L1 (triage workbench), L3 (integrity index + dHash/pHash dedupe), L5 (lightbox + gallery)

### Q6. Build the anti-rot moat: per-WhatsApp-era synthetic fixture DB generator, versioned schema adapters, a doctor/schema-report verb that fingerprints any db and reports parse-coverage %, and a golden-master CI gate where any parser change altering coverage must update the golden file in the same PR?
- BEST — Fixtures + adapters + doctor + golden gate + Hypothesis round-trip invariants + a corrupt-db fuzz lane asserting typed errors under a timeout budget. Upside: converts 'app silently broke on a 2028 backup' into a readable diff; the incumbent died of exactly this; doctor doubles as per-file user-facing trust proof. Downside: synthetic fixtures can drift from real backups and breed false confidence — generator configs must be seeded from real anonymized dumps per era; permanent maintenance overhead.
- VIABLE — Doctor verb only, no corpus or gate. Upside: cheap diagnostics now. Downside: no regression net; per-version coverage claims untestable; the 100% coverage mandate keeps no honest fixture strategy since real archives can never ship into CI.
- WORST — Status quo adapters. Upside: none. Downside: schema rot repeats the incumbent's death.

**Recommendation:** Option 1 — it is also the honest precondition for the commissioned 100% coverage claim.

**Downside of rec:** Fixture honesty is the load-bearing risk: a golden gate nobody maintains becomes noise, and generating representative locales/mojibake/edge-timestamps is its own mini-project; a new real WhatsApp v4 still needs a human to capture and seed the first sample before the gate helps.
**Convergence:** L2 (schema-currency moat + doctor), L3 (fixture factory as prerequisite), L4 (drift harness + schema-report gate)

### Q7. Include the stats engine (per-chat/per-dyad/per-group: activity heatmaps, volume timelines, top talkers, initiation ratio, median response latency, dormancy/revival, group lifecycle, ghost/deleted audit) as pure SQL aggregations exposed as GUI tab + CLI JSON/CSV + self-contained HTML report?
- BEST — Full stats family over the unified store with the triple output. Upside: at 13 years, stats ARE a retrieval interface ('when was this group actually active, who carried it'); pure data-layer code keeps the coverage mandate attainable; JSON composes with the agent goal. Downside: sequencing dependency — numbers silently lie if merge/dedup or the sender model are wrong; dashboard scope creeps fast.
- VIABLE — CLI/JSON only, no GUI tab yet. Upside: cheapest path to the data product. Downside: the visible 'wow' of the archive stays hidden behind a terminal — contrary to the owner's native-app direction.
- WORST — Skip. Upside: none. Downside: 'how did traffic change after March' stays unanswerable.

**Recommendation:** Option 1, strictly sequenced AFTER the store+merge item and the message-model item land.

**Downside of rec:** Every chart amplifies upstream data errors: wrong dedup or missing senders produce confident-looking WRONG history, which is worse than no history; system-message parsing for group metrics is locale-variable and needs structural (not locale) classification with golden fixtures.
**Convergence:** L1 (analytics dashboard), L3 (stats engine)

### Q8. How wide does the export matrix go: WhatsApp-styled HTML with FULL media (joined from the phone's media dir, not db thumbnails), PDF, XLSX/CSV, RSMF for e-discovery, Telegram-import JSON (real migration path off WhatsApp), vCard, legal mode (dual UTC+local timestamps + SHA-256 manifest)?
- BEST-balanced — One pluggable writer engine; wave A: HTML + CSV/XLSX + Telegram JSON + txt; wave B: PDF + RSMF + vCard + legal mode. Upside: RSMF + Telegram JSON in one free offline tool is a combination no free competitor has; the engine keeps later writers cheap. Downside: the legal/e-discovery differentiator waits a wave; HTML template upkeep is permanent.
- ALL NOW — every format in the first pass. Upside: maximum immediate differentiation. Downside: RSMF fidelity needs validation against a real review tool; PDF size explodes with media; breadth before the reading core works is polish on a frozen app.
- WORST — txt/html parity with upstream. Upside: least work. Downside: no differentiation; no migration path.

**Recommendation:** Option 1 (two-wave pluggable engine).

**Downside of rec:** Deferring RSMF/PDF postpones the unique-combo claim that most justifies the fork upstream; Telegram-JSON correctness only proves out against real Telegram imports, so expect an iteration cycle the plan does not show.

### Q9. Include a msgstore WRITER — schema-valid row inserts + media placement + crypt14/15 re-encryption (wa-crypt-tools already implements encryption), producing an Android-restorable backup: the free WazzapMigrator, and the endgame of landing the merged archive back on the daily phone?
- BEST — In scope as a gated FINAL phase: only after the diff engine proves zero-loss on real archives, behind explicit opt-in, with an emulator restore test matrix. Upside: the only free path to actually land the merged archive on the phone; highest-value unique capability (no open-source tool does conversion today). Downside: highest blast radius of the program — a bad restore can damage the live phone's history; WhatsApp app-version coupling can break it wholesale; the test matrix is sustained effort.
- VIABLE — Out of scope for this program; keep using paid WazzapMigrator for the final land step. Upside: removes the riskiest surface; the read-side program stays clean. Downside: the endgame stays paid and iPhone-to-Android-only; productized local merge of two msgstores stays manual DB-browser surgery.
- WORST — Build now, early. Upside: none. Downside: write-side work before read-side correctness is proven inverts the risk order.

**Recommendation:** Option 1 (gated, last, opt-in).

**Downside of rec:** The owner's actual merge-back-to-phone goal stays blocked behind the entire read-side program; restore strictness is community-reported (MEDIUM confidence), so the investment can dead-end late if WhatsApp tightens validation — the gate must include a real emulator restore proof before any user sees the verb.

### Q10. Build a local acquisition assistant — auto-detect iTunes/Finder backup dirs, ADB pull wiring for rooted devices, WhatsApp-Key-DB-Extractor integration (Android 4.0-13 only), first-class E2E 64-hex-key crypt15 flow — with Google Drive/iCloud cloud acquisition explicitly excluded?
- BEST — Detection + wiring + E2E key flow only, CLI-first (`acquire` verb), no hand-holding GUI wizard; accept EXWA/iMazing/Reincubate output files as inputs. Upside: removes the #1 onboarding friction for every free tool in this niche at low cost. Downside: ADB backup is deprecated on Android 12+ and non-root key extraction is effectively dead on modern Android — the tool must be honest and steer to the hex-key path; Windows driver flakiness creates support burden.
- VIABLE — Documentation-only runbook, no code. Upside: zero maintenance. Downside: friction stays; acquisition remains the paid competitors' whole headline.
- WORST — Full cloud acquisition too. Upside: none. Downside: heavy auth + ToS surface; explicitly the paid lane; contradicts the estate's local-only doctrine.

**Recommendation:** Option 1 (thin, local-only, CLI-first), late in the program.

**Downside of rec:** Narrow upside for the owner personally (the files are already in hand); every third-party extractor wired in rots on its own schedule and becomes a maintenance liability the reading core does not have.

## sequencing

### Q11. Which build order: substrate-first (theme tokens, paginated core, schema fixtures, canonical store) before visible features, or visible-features-first to show progress early?
- BEST — Substrate-first wave 1: (a) Figma token/theme system, (b) paginated core + virtualization, (c) schema fixtures + doctor, (d) canonical store. Wave 2: typed rendering + search + jumps. Wave 3: media + stats. Wave 4: agent surfaces (MCP/watch) + export matrix. Safety rails (vault, no-egress) land continuously alongside. Upside: nothing user-visible is built on the old fetchall path; tokens keep later waves visually consistent. Downside: first visible wins arrive a wave later; a wrong substrate bet (e.g. Kivy virtualization fails) means deep rework.
- VIABLE — Hybrid: pagination + fixtures strictly first, rendering/search start as soon as their primitives exist (overlapping waves). Upside: earlier visible progress. Downside: parallel tracks on a moving substrate produce merge churn and rework.
- WORST — Features-first (restyle + lightbox now, substrate later). Upside: instant gratification. Downside: restyling a UI whose data layer freezes on big chats is polishing the blocker.

**Recommendation:** Option 1, with ONE deliberate overlap: the native-install interim fix (see process-maintenance) runs in parallel from day zero.

**Downside of rec:** The owner sees little shiny progress in wave 1 and must hold the discipline to refuse feature requests that skip the queue; three lenses each claim THEIR layer must be first, so this ordering will be re-argued at every planning session unless locked now.
**Convergence:** L1 (pagination-first), L4 (harness-first), L5 (theme-first) — three lenses independently claim priority; convergence on 'substrate first', divergence on WHICH substrate

## effort-ceiling

### Q12. Which high-effort (multi-wave) items are allowed at all: archive store+merge (high), restore writer (high), ingest watcher daemon (high), full media workbench (medium-high), semantic layer (heaviest dependency)?
- BEST — Allow high effort for the two owner-critical chains (merge/store, media); gate restore-writer and watcher behind explicit mid-program go/no-go reviews with evidence in hand; semantic stays an optional extra evaluated only after FTS5 proves out. Upside: effort concentrates on the archive's actual purpose; the riskiest surfaces get a decision point instead of a blank check. Downside: gated items may never survive their review — the phone-merge endgame and the live-agent archive could legitimately slip out of the program.
- VIABLE — All five greenlit now. Upside: no re-litigation later; parallel planning. Downside: program bloat; the failure mode is five half-built high-effort systems instead of two finished ones.
- WORST — Medium ceiling only. Upside: tight program. Downside: the merge/store chain — the owner's live project — cannot fit under it.

**Recommendation:** Option 1.

**Downside of rec:** Mid-program gates need the owner's continued attention; a deferred go/no-go that never gets reviewed rots in OPEN-LOOPS — each gate needs a named review-by date at lock time.
**Convergence:** cross-cutting synthesis: triages the high-effort items from L2 (restore, corpus), L3 (merge, semantic), L6 (watcher)

## safety-data

### Q13. How many stores does this app have — a plaintext working canonical archive.db, an encrypted-at-rest vault (SQLCipher, DPAPI-wrapped key), and/or a portable .wams bundle — and which is the source of truth? (L1/L2/L3 designed a plaintext store; L7 independently designed a vault + bundle; the two camps were never reconciled.)
- BEST — Layered, built in order: archive.db as derived working store -> vault as the app-owned encrypted home (supersedes plaintext residency) -> .wams bundle last as the portable/share unit (content-addressed, zstd, optional age-encryption, verifier needs zero vault deps). One source of truth = the vault; archive.db is rebuildable. Upside: each layer answers a different need (work, safety, portability); no single format is forced to do everything. Downside: three formats = three migration paths and real concept load in the UI; users will expect the DPAPI-bound vault file to just work on another machine and it will not.
- VIABLE — Single encrypted store only (the vault IS the archive). Upside: one format, least concept load, safest default. Downside: every analytical/agent workload pays decryption overhead; FTS and derived indices inside the encrypted store complicate watcher and MCP paths; portability still unsolved.
- WORST — No store; operate directly on decrypted msgstore files. Upside: least code. Downside: plaintext residue next to sources stays the standing hazard; no memory between sessions.

**Recommendation:** Option 1, with the layering written down BEFORE ingest is designed (it changes the ingest schema).

**Downside of rec:** The most engineering-expensive answer; the vault/bundle boundary gets re-argued at every sharing feature, and a derived-store bug means the rebuild path must be flawless or the working archive silently diverges from the vault.
**Convergence:** L1+L2+L3 (canonical store) vs L7 (vault + .wams bundle) — independent designs in direct tension; the highest-tension cross-lens fork in the queue

### Q14. Vault mechanics: import-verify-shred (delete the plaintext source ONLY after verified reopen + rowcount/checksum match), Argon2id passphrase wrapped by Windows DPAPI, printed one-time recovery code, idle auto-lock, and an annotation sidecar (notes/redactions never mutate source dbs)?
- BEST — All of it, with --shred-source behind the verify gate. Upside: closes the standing plaintext-residue hole (decrypted db + key file sitting wherever they were extracted — a hazard class this estate has measured before); annotations become possible without touching sources. Downside: passphrase loss = vault loss unless the recovery code was actually printed/saved; shred on SSDs is best-effort (wear-leveling) and must be documented honestly, not sold as multi-pass theater.
- VIABLE — Vault without shred (import-and-keep-source). Upside: no destructive path at all. Downside: the residue hazard the vault exists to close stays open; relies on user discipline.
- WORST — No vault (covered by the storage-architecture item's option 3).

**Recommendation:** Option 1.

**Downside of rec:** Any verify-then-shred bug is catastrophic and irreversible — defect-as-fixture tests proving shred REFUSES on verify-failure must exist before the flag is ever allowed to run against a real archive; DPAPI binding also makes the vault deliberately non-portable, which must be stated in UX or users will assume otherwise.

### Q15. Share-safe export pipeline: deterministic per-contact pseudonyms, phone/email/PAN/URL structured scrubbing, per-chat opt-in scopes, EXIF strip, a mandatory redaction-report.json beside every export — and at what depth: baseline scrub only, or full k-anonymity enforcement plus built-in re-identification attack preview that can FAIL the export?
- BEST — Baseline now (pseudonyms + structured detectors + EXIF strip + mandatory report + a --bug-report mode emitting a schema-true content-synthetic minimal db); k-anonymity + re-ID preview gate as a later phase gated on real sharing need. Upside: sharing (family/legal/upstream issues) stops meaning 'hand over everything raw'; bug-report mode kills the single most likely accidental-leak channel — real dumps attached to GitHub issues. Downside: regex redaction gives false confidence; free-text leaks survive line-scrubbing.
- VIABLE — Full stack now incl. k-anon + re-ID preview. Upside: 'previews re-identification risk before export' is a genuine differentiator no tool in class has. Downside: research-grade effort; built-in attacks are a floor not a ceiling; delays the baseline.
- WORST — Raw export only. Upside: none. Downside: every share is a full-PII dump; line coverage on redaction paths lies — the gate must be behavioral.

**Recommendation:** Option 1; the residual-risk statement ships attached to every export and the output is never marketed as anonymous.

**Downside of rec:** Early shares carry more risk than the full design would allow; a prominent masked export will still over-trusted by recipients unless the report is read — the tool cannot make people read reports.

### Q16. When agents get archive access: enforce transport-boundary privacy profiles (full | masked: pseudonymous ids + no media bytes | metadata-only: counts/timestamps/participants, zero content) plus an append-only audit log of every agent-visible read (transport, tool, params-hash, profile applied)?
- BEST — Both, built in the same work unit as the MCP server. Upside: agent scoping becomes one flag; 'what did the agent actually see' becomes mechanically answerable; cheapest trust-per-effort in the program. Downside: every transport grows a redaction tax; masked profiles still leak via context (quoted messages, nicknames) — property tests must cover the wa.db contact-join path.
- VIABLE — Audit log only, no profiles. Upside: observability without gating complexity. Downside: 'the agent CAN read everything' stays the default — a decision the owner never actually made.
- WORST — Neither. Upside: none. Downside: unrestricted, unlogged agent reads of a private-message archive.

**Recommendation:** Option 1 — profiles at the transport boundary only, never in the core, so the GUI keeps full fidelity.

**Downside of rec:** Profiles add a permanent maintenance surface: every MCP tool added later must be profile-aware from day one or the guarantee silently holes; enforcement adds latency to every agent read.
**Convergence:** L6 (transport-boundary profiles), L7 (masked/metadata redaction ethos)

## platform-reach

### Q17. Ship the archive as an MCP server (optional [mcp] extra, `wmv serve-mcp`, FastMCP stdio): read-only, cursor-paginated tools (archive_info incl. schema_version, list_chats, get_messages, search_messages, get_chat_media, resolve_participants, export_slice sandboxed to --export-dir, list/use_archive for multi-archive sessions), one pydantic model shared with CLI --json?
- BEST — Yes: optional extra, namespaced tool names (wa_* prefix) to avoid collisions where search_messages already collides in the estate's social-hub multiplexer. Upside: MCP is the native agent transport on this estate; near-zero new logic (thin adapter over the core); bounded payloads (default page 50, hard cap 200) are a survival requirement — oversized MCP outputs get killed here (measured). Downside: a second transport kept in schema parity forever via drift tests; every core change now has three consumers.
- VIABLE — CLI --json only, no MCP transport yet. Upside: one surface to maintain. Downside: agents must shell out; the commission's 'CLI-drivable (human+agent)' is only half-honored.
- WORST — MCP in the core install. Upside: none. Downside: dependency bloat; upstream PR friction.

**Recommendation:** Option 1, as an optional extra with in-process FastMCP contract tests + pagination-cap invariant tests in CI.

**Downside of rec:** Pagination contracts are easy to get subtly wrong (a whole-chat dump on a default argument) — the cap invariant tests are load-bearing, not polish; tool-name namespacing conventions must be decided before mounting next to existing servers, not after.

### Q18. Make the archive live: `wmv watch` daemon on the backup dir (size-stability gate for partial copies, decrypt into a SHA-256-keyed cache, refresh the FTS index, append typed events to events.jsonl consumed by agents via poll) — with outbound webhooks explicitly demoted to a default-off plugin extra?
- BEST — Watcher + pull-based event tail (poll_events MCP tool + `wmv events --since`); webhooks demoted. Upside: MCP/CLI/GUI always serve the latest backup with zero manual re-runs; pull beats push for a single-user local tool (no URL/credential config surface, no push-egress behavior). Downside: a second long-running component in what is becoming a native app (process lifetime management); Windows file locks and partial-copy heuristics are fragile — needs a --poll-interval fallback.
- VIABLE — Manual `wmv rescan` verb only. Upside: no daemon at all. Downside: 'auto-refresh on new backups' quietly means manual forever.
- WORST — Webhooks in core. Upside: none. Downside: push infrastructure nobody calls = complexity and exfil-adjacent surface for nothing.

**Recommendation:** Option 1, but scheduled only AFTER the native-install/process-lifetime story exists — a daemon hidden in a closing terminal window is the exact failure the owner just complained about.

**Downside of rec:** Daemon bugs surface as stale data that looks fresh — the event log must carry enough provenance (source hash, reindex duration) for staleness to be noticeable; the size-stability gate heuristic will misfire on slow network copies.

### Q19. Which ingest sources are in scope beyond Android msgstore: WhatsApp's own email/txt exports (+WCE result.json), and iOS ChatStorage.sqlite from iTunes/Finder backups (incl. optional encrypted-backup decryption)?
- BEST — Android msgstore + WhatsApp txt exports + WCE json now; iOS ChatStorage as a fast-follow adapter family. Upside: txt ingestion is cheap and covers the no-root majority; iOS closes the gap both open-source competitors already cover; serves iPhone-history users without paid tools. Downside: two more adapter families under the same schema-drift regime; iOS encrypted-backup decryption drags a heavy optional dependency; dedup heuristics must handle timezone-shifted duplicates.
- VIABLE — iOS native ingest in wave 1 too. Upside: biggest capability jump (archive hub). Downside: doubles wave-1 adapter surface before the drift harness proves itself; the owner's own iOS history already arrives as WazzapMigrator-produced msgstore, so owner-value here is lower than competitor-value.
- WORST — Android-only forever. Upside: tightest scope. Downside: the tool stays an 'Android db browser'; iPhone-era users unserved.

**Recommendation:** Option 1.

**Downside of rec:** iPhone-to-Android users without WazzapMigrator wait an extra wave; txt-export sender inference (--assume-first-as-me style) is heuristic and can mis-attribute messages silently — it must be labeled per-chat in the UI.
**Convergence:** L2 (iOS + txt ingestion + incremental merge), L3 (multi-source ingest incl. iOS-era extractions)

### Q20. Include an optional local semantic layer ([semantic] extra: local sentence-transformer embeddings over rolling per-chat windows into sqlite-vec, natural-language recall like 'the conversation about the Cluj apartment lease', topic drift, sentiment arcs) — fully offline, no server, no API calls?
- BEST — Optional extra, built only after FTS5 + store prove out, labeled experimental, strictly dependency-isolated from the frozen build. Upside: the only mechanism answering non-keyword questions — over 13 years those are most questions; 100-500K messages embed locally in minutes on this hardware; opt-in keeps the core upstreamable. Downside: heaviest dependency in the stack (model download, bloat risk); recall quality on mixed Romanian/English chats unproven; likely stays fork-only.
- VIABLE — Defer the decision entirely until post-FTS5. Upside: zero commitment now. Downside: the store schema may need vector columns later — a migration.
- WORST — Core feature now. Upside: none. Downside: dependency weight lands on every install for a speculative win.

**Recommendation:** Option 1 (fall back to Option 2 if the grill wants fewer irons in the fire).

**Downside of rec:** An optional extra that rots untested is worse than none — it needs its own smoke lane in CI or it will ship broken and nobody will notice until the owner tries it.
**Convergence:** L3 (semantic recall), L6 (optional semantic backend behind the filter DSL)

### Q21. Owner-relayed NEW scope (not from any lens): greenlight a separate ultracode wave for the Instagram app account on the phone — account saved locally on this PC, persistent login/re-access that survives session expiry ('save means to reaccess')?
- BEST — Greenlight as a separate wave AFTER WhatsApp scope-lock, scoped strictly to the owner's OWN account on the owner's OWN phone/PC: local session vault (cookies/tokens at rest, DPAPI-protected like the app vault), periodic freshness refresh, re-access = re-inject into a browser context via the estate's cookie-bridge pattern (never the profile-corrupting force-kill), with a one-spike entry gate (extract session from phone, prove one re-access, measure decay interval). Upside: matches the estate's existing own-session bridge doctrine; no credential ever transits the agent; re-access becomes a file operation, not a login. Downside: ToS/ban risk sits with the account; Meta actively fights session porting via device fingerprinting, so persistence WILL break on app/web updates and need maintenance; a live session token at rest is a high-value target file; easily scope-creeps into a second full program.
- VIABLE — Probe-only first: run the e2e spike, report decay interval and fingerprint tolerance, THEN decide the wave. Upside: evidence before commitment. Downside: a spike that works once proves little about week-scale persistence; decision defers again.
- WORST — Start now, in parallel with the WhatsApp program. Upside: none. Downside: two greenfield programs competing for the same waves; both dilute.

**Recommendation:** Option 1, using Option 2's spike as the wave-entry gate — and correct the expectation at greenlight: the honest deliverable is fast RE-ACCESS (restore from vault + refresh), not immunity from logout; no local save can guarantee never-logged-out against Meta-side invalidation.

**Downside of rec:** Even the honest version carries account-level risk the program cannot control (device-fingerprint rotation, forced re-auth, security holds); custody of a live session token adds a standing security obligation on this PC; and scheduling it after WhatsApp scope-lock means it waits behind the entire queue above.
**Convergence:** none — owner-relayed new scope; flagged because it adds a second program boundary the grill must explicitly accept or defer

## process-maintenance

### Q22. OWNER-DIRECTED, starts immediately (the only pre-decided item — the question is HOW, not WHETHER): make the app a native install that lives independent of any terminal, because today closing the visible terminal closes the app. Which route?
- BEST — Two-step: (a) TODAY: launch via pythonw.exe / windowed shortcut so closing the terminal cannot kill the app (kills the exact complaint same-day); (b) DURABLE: PyInstaller windowed onedir build + Inno Setup installer (Start-menu shortcut, version single-sourced from version.py), gated by the packaged-artifact smoke test. Upside: complaint dies immediately; the durable fix rides the release pipeline instead of a parallel hack. Downside: PyInstaller+Kivy is the canonical hidden-import/.kv-data-file trap — an unsmoked exe is worse than none; unsigned onedir builds draw AV false positives.
- VIABLE — pythonw/shortcut only; defer real packaging. Upside: zero new build surface. Downside: stays a source-tree app; 'native install' unfulfilled for any non-owner machine.
- WORST — MSIX/store-style package now. Upside: cleanest install story. Downside: signing + sandboxing overhead before the app has a release cadence.

**Recommendation:** Option 1 — do step (a) today as the 'meanwhile' the owner asked for, wire step (b) into the release pipeline item.

**Downside of rec:** Two release artifacts (run-from-source + installer) must both be kept honest until the pipeline exists; the interim pythonw route can still flash a console window on some setups unless the entry point is a true windowed build; PyInstaller spec drift (a new dep adds a data file) is only caught by the smoke gate, not by green source CI.
**Convergence:** L4 (release pipeline/packaging) + explicit owner directive relayed this run

### Q23. One-tag release pipeline now: tag v* triggers CI builds (Windows/macOS/Linux) publishing a GitHub Release, version single-sourced from version.py into PyInstaller + Inno metadata, CycloneDX SBOM + artifact attestation + per-release delta manifest, and a post-build smoke gate that launches the ACTUAL packaged exe against fixture DBs (exit-0 probes, non-empty export file) before publish is allowed?
- BEST — Full pipeline, Windows tier-1; macOS/Linux artifacts-only until proven. Upside: 'green from source, broken exe' is the #1 packaged-Python failure mode — only exercising the built artifact catches silently dropped hidden imports; releases are where 5-year ownership cost concentrates. Downside: CI time; macOS notarization is the classic time sink (explicitly deferred); spec-file churn on every new dependency.
- VIABLE — Manual tagged builds + a smoke script run by hand. Upside: no CI config to rot. Downside: the smoke gate is the first thing skipped under time pressure.
- WORST — Source-only releases. Upside: none. Downside: directly contradicts the owner-directed native install.

**Recommendation:** Option 1, Windows-first, wired to the native-install item as its enabling rail.

**Downside of rec:** A publish-attached smoke gate adds real minutes per release and can block an urgent fix on a flaky probe — probe determinism matters more than probe coverage; SBOM/attestation tooling on Windows runners has its own quirks.

### Q24. Adopt GUI snapshot regression: headless Kivy GuiDriver instantiating each screen from the real .kv files against fixture DBs, dumping normalized widget-tree JSON goldens per screen x M3 theme x locale into CI, plus exactly ONE pinned pixel lane (single Windows runner, fixed framebuffer, pixelmatch tolerance) — never cross-OS pixels?
- BEST — Tree goldens in core CI + single pinned pixel lane + a local `wmv ui-snapshot` regen verb + the tier policy documented (GUI snapshots Windows tier-1; Linux/macOS run the kivy-free core suite). Upside: with a 100% UI restyle in scope, this is the only thing keeping future visual changes reviewable; tree-over-pixels is the anti-flake choice — cross-OS pixel diffs are a flake factory, and a flaky snapshot harness gets deleted within a year. Downside: Kivy headless rendering and .kv loading from an installed wheel have real quirks; golden updates must be same-PR discipline.
- VIABLE — Tree goldens only, no pixel lane. Upside: fully deterministic. Downside: the theme/token system then claims visual correctness with zero visual check.
- WORST — None; eyeball verification. Upside: none. Downside: the restyle and every later UI change ship unaudited.

**Recommendation:** Option 1.

**Downside of rec:** Must be proven against an intentionally-broken screen first (defect-as-fixture) or it silently tests nothing — a harness riding an unfixed defect is a measured failure mode on this estate; golden churn will annoy contributors and needs a one-command regen path or it gets bypassed.

### Q25. Dependency hygiene program: consolidate to ONE dependency declaration (kill the requirements.txt/pyproject duplication, multitasking listed twice), uv lockfile, Renovate (grouped weekly minor/patch, isolated majors with full test runs, immediate security patches), a weekly canary lane compiling against latest+pre-release of Kivy/KivyMD/protobuf/pycryptodomex (fail-VISIBLE: auto-opened dated issue, never a merge block), and a lowest-resolution job forcing the honest Python-floor decision (3.8 is EOL)?
- BEST — All four lanes. Upside: current pins are already stale enough to bite (kivymd 1.2.0 vs the 2.0 target, protobuf/pycryptodomex prebuilt-wheel risk on future Pythons); decay becomes a weekly visible ticket at near-zero cost instead of a crisis at the next feature. Downside: canary noise becomes a permanently ignored red X unless the fail-visible policy is held strictly advisory; the lowest job forces the Python-floor decision the grill must then actually make.
- VIABLE — Lockfile + Renovate only. Upside: covers the common rot. Downside: no early warning on the four high-churn deps that specifically break packaged builds.
- WORST — Status quo pins. Upside: none. Downside: the CI matrix validates only today's pins — green while the install rots.

**Recommendation:** Option 1.

**Downside of rec:** Four CI lanes of maintenance for dependencies we do not control; canary failures will sometimes be upstream bugs we can only document, not fix — and the dated-issue mechanism must be pruned or it becomes its own backlog.

### Q26. Make offline-by-construction an enforced negative guarantee: core package forbidden from importing socket/urllib/http/requests (import-linter + a CI walk of the FROZEN binary's import graph failing on any transitive network module), a socket-patch regression asserting zero egress across every CLI verb, telemetry-free crash capture (structured local crash records with a redaction test proving zero message-body bytes) + `doctor --bundle` privacy-safe diagnostics zip, and an audit of the existing requests dependency (likely an update check or font fetch) made opt-in or bundled?
- BEST — All of it, plus TEMP hygiene (plaintext never spills to disk) and recent-files/window titles stored inside the vault. Upside: the input is decrypted private chat history — 'we don't phone home' becomes a CI invariant instead of a README claim; the crash journal makes a 2029 'it crashed on my backup' issue diagnosable from a pasted bundle. Downside: over-constrains future legitimate features (any cloud sync needs an explicitly-audited opt-in module behind a build flag); the requests audit may force bundling an asset or dropping a nicety.
- VIABLE — Crash-redaction tests + one blocked-network CI run only; no import-graph gates. Upside: catches the big leaks cheaply. Downside: a transitive dependency can reintroduce egress silently — exactly the feared path for a packaged personal-archive tool.
- WORST — README claim only. Upside: none. Downside: an unverifiable trust statement on the most trust-sensitive axis this app has.

**Recommendation:** Option 1.

**Downside of rec:** The frozen-binary import walk is version-sensitive CI machinery of its own that must track PyInstaller output-format changes; a future legitimate feature (e.g. link-preview fetch) must fight the gate rather than quietly ship — which is the point, but also permanent friction.
**Convergence:** L4 (egress-free lane + telemetry-free crash capture), L7 (offline-by-construction distribution guarantee)


## CONVERGED — FINAL DECISION LOG (owner, 2026-09-30)

Tier-2 + process verdict: **'state of the art'** — the SOTA option on every remaining fork:
- Storage: encrypted-at-rest vault (SQLCipher/DPAPI-wrapped key) + plaintext working store ONLY as transient ingest cache; import-verify-shred on vaulting.
- Share-safe export: deterministic pseudonyms, structured scrubbing (phone/email/URL), EXIF strip, mandatory review manifest. IN.
- Agent access privacy profiles (full | masked | metadata-only) enforced at the MCP boundary. IN.
- MCP server ([mcp] extra, read-only, cursor-paginated). IN.
- Watch daemon (size-stability gate, SHA-keyed decrypt cache, FTS auto-refresh). IN.
- Ingest beyond Android: iOS ChatStorage.sqlite + email/txt exports + WCE result.json. IN.
- Semantic layer ([semantic] extra: local embeddings, sqlite-vec, natural-language queries). IN.
- Process (auto-decided, stated): hybrid sequencing (short substrate wave then visible features); one-tag release pipeline; GUI snapshot regression; ONE dependency declaration (kill duplication) + uv lock; offline-by-construction enforced via import-linter + CI (no socket/urllib/http/requests in core).
- Effort ceiling: unlimited (all high-effort items authorized by all-IN + SOTA).

GRILL COMPLETE. This log is the input to the build plan (docs/program/PLAN.md).
