# WMV Modernization — Program Plan (v4, post-gate-r3 — SELF-CONTAINED)

Input: converged grill decision log (`decision-queue.md`). Owner verdicts: G-1 daily-driver fork; G-2 M3+UX craft Figma-first; Tier-1 ALL TEN IN; Tier-2 "state of the art".
Prior revisions + full gate verdicts live in `docs/program/archive/` (v1/v2/v3 + gate verdicts). **This document is normatively self-contained — no pointers to superseded revisions.**

## Absorption ledger (itemized; auditable; no blanket claims)

**gate-v1 (17 must / 9 should):** absorbed — windowed core (W1), archive system+diff (W1), FTS engine (W1), message model data-half (W1), pHash primitive (W1), anti-rot fixtures (W0), kivymd-held-until-W3, gate-0 redefinition, storage-layering-first, safety gates, export-matrix breadth (W4), MCP audit log, per-wave checklist, dep re-pins, concurrency unit, keyset-grain fix, watch-daemon→W4, visible-value-first (**token-pass M3 slice at Gate 1b — NOT claimed as F12/CLI absorption**), fixtures-before-refactor. Deferred (dated below): k-anonymity preview. Not adopted: none.
**gate-v2 (14 must / 12 should):** absorbed — F1 share-safe 4.2c; F2 email/txt ingest + labels (1.4); F3 decrypt goldens + `_pb2` regen (0.1/0.2) **[also now committed: fork shim 30e1723]**; F4 SQLCipher Windows spike (1.0); F5 recovery-code/auto-lock/annotation (4.1); F6 IG-track restated (below); F7 tier-scoped coverage; F8 blocking smoothness; F9 immutability test; F10 ledger itemization (this); F11 Gate-5 split; F12 design-before-port (3.1); F13 consumed-keys union (Bar 3). Should-fixes absorbed: bug-ownership, 4.4→before-4.3, contacts-artifact, early-PR-branch, crash-journal+redaction NOW, Gate-1a/1b, accumulated suites, mutation scoping, review-by dating, artifact smoke, poll_events.
**gate-v3 (17 must / 10 should):** absorbed in THIS v4 — Unit-0.0 evidence line (below); **Gate 2 restored**; **tier manifest** (0.4, mechanical); token-pass slice at 1b; Gate 5a/5b split + local-matrix PR evidence; grammar 2-consumer at W2 + stub, 3-consumer at Gate 3; consumed-keys UNION both mechanisms; ledger corrections (this section + Deferred rows for Q25 canary lane, Q23 delta manifest — previously falsely "none not adopted"); self-containedness (this doc); 0.1 seam mechanism (compat shim in 0.1 DoD); shell-port-first (3.1); call-log fix layer corrected (Model/main_screen.py `get_calls` `call.get('raw_string_jid')`); media audit engine 3.3a; Q26 requests audit unit (0.2); pixel/tree-golden lane moved INTO Wave 3; Gate-3 floor numbered (≥80% per-screen, owner-ratified at approval); immutability extended to 4.4; snapshot-harness red-proof (Bar 3); SQLCipher-binding FTS drift probe (4.1); Q25 four lanes named (0.3); decision-log one-liners homed (4.2c/4.5); review-by dates locked (Deferred); IG phrasing aligned to RUNBOOK (below); Gate 0/1a accumulated-suite text; 0.7 off Gate-0 critical path; python-floor decision + cp314 .pyc purge (0.3). **Not adopted: none.**

## Unit 0.0 — windowed native launch: DONE WITH EVIDENCE (pre-program, 2026-09-30)
`run_wmv.pyw` + None-stream shim + AppUserModelID committed in-fork: **30e1723** (shim), **93252f8** (identity+launcher). Interim install live (venv-native `WhatsAppArchiveViewer.exe`, icon embedded; terminal-close acceptance observed 2026-09-30; Apps-list/Desktop/Start entries verified). Remaining in-program: pythonw smoke (launch + decrypt fixture, no crash) added to **0.6**; superseded by the Wave-4 real installer.

## Bars — re-asserted at EVERY gate as an ACCUMULATED suite registry (all prior gates' suites re-run green)

1. **Coverage (tier-manifest-mechanical):** 0.4 emits a **checked-in tier manifest** (module → NEW / REWRITTEN / LEGACY + baseline %) the coverage gate reads mechanically; any tier flip auto-tightens the threshold in the same PR. NEW/REWRITTEN = 100% line+branch immediately; LEGACY = baseline + never-below ratchet + 100%-on-rewrite; **core+cli 100% line+branch at Gate 5a per manifest**; View allowlist shrink-only since Gate 4.
2. **CI:** windows-latest primary + ubuntu lane; matrix 3.11/3.12/3.13 (cp314 banned — no kivy wheels; **0.3 records the python-floor decision and purges committed cp314 .pyc**); headless lane (`KIVY_GL_BACKEND=mock` + `KIVY_USE_DEFAULTCONFIG=1` + `KIVY_NO_ARGS=1`); non-gating angle_sdl2 render lane; import-guard + offline-guard (import-linter); ruff banned-API; per-test timeouts; FTS5 pragma pin check (sqlite_version + tokenizer smoke); golden-master parse-coverage gate; install-smoke (uv-locked env on all three Pythons) before test lanes. **Scheduled NOW:** socket-patch egress attempt in CI (offline-by-construction proof); telemetry-free crash journal with zero message bytes in crash dumps (redaction test) — after 0.2's requests-audit unit decides the socket consumer's fate, so neither stays permanently red.
3. **Zero regressions:** characterization goldens; per-screen snapshot/tree-golden regression **including a defect-as-fixture red-proof for the snapshot harness itself** (harness fires on a seeded visual defect before it is trusted); **consumed-keys contract pinning the UNION of keys across ALL View consumers, BOTH mechanisms** (explicit `refresh_view_attrs` at chat_screen.py:103 AND implicit RecycleView property matching in chat_message.kv incl. txt_data/msg_quoted_text_data; plus main_screen list-builders' 8 further keys) — generated by a Kivy-free AST/index-scan test keyed to fixture shapes.
4. **Zero data loss:** never-write-sources enforced by a **source-immutability property test** (checksum every source file before/after each ingest, dry-run, merge-write, **and writer operation**) — 1.4 acceptance + checklist items for 1.5/1.6/4.1/**4.4**.
5. **Per-wave gate checklist:** core+cli coverage headless green (accumulated) · View allowlist delta with line-count reported, shrink-only ratchet from audited baseline, reviewer = **gate panel** · per-screen behavioral inventory ≥ **80%** (numbered floor; owner may ratify a different number at plan approval) reported at Gates 3/4 · mutation on each wave's new **kivy-free** logic · import/offline guards · ALL accumulated suites from prior gates green.
6. **Scroll smoothness — BLOCKING for UI-touching units:** p95 frame time ≤ 33ms (target 16) scrolling a fixed 50K-message chat with a fixed script on the angle_sdl2 lane; re-baselined once at 3.1; mock-GL per-window data-provider latency proxy = gating headless signal; runner unavailable = NOT-CHECKED, never pass.

## Package architecture (D3)
`wviewer/{core (kivy-free, no socket), cli (Typer, no kivy), view (only kivy tree), mcp ([mcp] extra), semantic ([semantic] extra)}`; entry points `wmv` + `wv`; deterministic schema registry; cwd-independent resource loading.

## Known-bug ownership (in-tree BEFORE Wave 5)
- **call-log display names:** bug is `Model/main_screen.py get_calls` reading `call['raw_string']` with KeyError swallowed → fix = `call.get('raw_string_jid')` one-liner in 1.1 (adapters already alias it; changing the alias would break `build_calls_list` which reads `raw_string_jid` — the v3-plan fix was wrong-layer, corrected here). 0.1 golden pins current broken behavior; re-baseline at 1.1.
- emoji-font validation copy-paste (login_screen.py:205) → 0.6.
- os.remove-in-except crash paths (Controller/login_screen.py:114,125) → 0.2, red-proof first.
- f-string SQL in all three fetch_chat adapters → 0.5.
- **Decrypt path (proven broken):** bare `proto.*` imports (prefix_pb2.py:14-17, C14_cipher_pb2.py:14) → every in-app decryption silently degrades to `guess_offsets`. 0.1 decrypt goldens assert `parse_protobuf` NOT `guess_offsets` (red-proof on the broken import); 0.2 regenerates package-correct `_pb2`.

## Waves

**Wave 0 — Characterize, then restructure**
- 0.1 Golden fixtures FIRST (v1/v2/v3 shapes + decrypt goldens + email/txt fixture shapes + the `jid.raw_string` divergence pinned + call-log broken-behavior pin). **DoD includes the seam: a `wviewer/compat` shim re-exporting old import paths, created HERE, so characterization tests import stably across the 0.2 rename.**
- 0.2 Restructure + wheel metadata + cwd-independence + bug fixes (**pure-rename commits split from behavior-fix commits; every fix pins TARGET behavior with red-proof first**) + `_pb2` regen + **requests-socket consumer audit** (requests~=2.28.2 sits in both declarations; decide remove vs first-use justification — the Bar-2 egress test depends on this) + dead-dep drops (watchdog/pygame if truly unused) + crash-journal/redaction implementation.
- 0.3 Dependency re-pins: kivy==2.3.1, **kivymd==1.2.0 (HELD to Wave 3)**, PyInstaller 6.x pinned; pycryptodomex/protobuf cp313-compatible re-pins (regen `_pb2` if protobuf 5.x); ffpyplayer pin decision; python 3.12 primary; uv lock; **python-floor decision + cp314 .pyc purge**; **Q25 four lanes: single-declaration consolidation (here), Renovate (4.6), canary pre-release lane (4.6, dated Deferred if cut), lowest-resolution job in CI (0.4)**.
- 0.4 CI skeleton: all Bar-2 lanes + import/offline guards + **coverage in the allowlisted-red list with subject waves** + **tier manifest emitted**.
- 0.5 Schema registry + parameterized SQL.
- 0.6 App-launch smoke (1.x KivyMD) **+ pythonw smoke (launch + decrypt fixture, no crash)**.
- 0.7 Courtesy-PR branch `courtesy/upstream-fixes` off upstream/main (1.1.2) with the four fixes as separate commits — **bonus-only; NOT on Gate-0's critical path.**
- **Gate 0:** characterization + unit + install-smoke green; app smoke green; pythonw smoke green; allowlisted-red exactly as expected; bug-fix units landed with red-proofs; accumulated-suite registry starts here.

**Wave 1 — Data core**
- 1.0 ENTRY (blocks all): storage layering design + **SQLCipher Windows distribution spike** (vcpkg/choco amalgamation or vendored DLL; assert FTS5+trigram+remove_diacritics compiled in; if no acceptable Windows path → alternative at-rest design decided HERE, before schema freeze) + transient-cache path spec (all decrypt outputs routed there).
- 1.1 Typed message model + adapter queries + attribution labels + contacts promoted to first-class schema artifact (from runtime wa.db side-load) + call-log one-liner fix.
- 1.2 Concurrency unit (thread-confined connections; shared-cursor design replaced).
- 1.3 Windowed keyset pagination (message-grain composite (timestamp_ms,_id); media/quoted attached after windowing; **fixtures include same-second-burst and multi-media message rows**).
- 1.4 Canonical store + idempotent ingest (Android/iOS/WCE/**email+txt**) + per-message provenance + **source-immutability property test**.
- **Gate 1a:** store+ingest+immutability+diff-ready green **+ all accumulated Gate-0 suites**.
- 1.5 Diff engine (before merge writes). 1.6 Cross-source merge + core pHash primitive. 1.7 FTS5 + versioned grammar (**Wave 2 delivers parser contract + CLI/MCP 2-consumer drift + kivy-free GUI-palette adapter stub; full 3-consumer drift is Gate 3 acceptance**). 1.8 doctor + Hypothesis invariants + corrupt-db fuzz. 1.9 `wv` thin slice on the real archive. **Token-pass M3 slice on kivymd 1.2.0** (theme tokens only — first owner-visible change; Figma-token pipeline per G-2).
- **Gate 1b:** full accumulated checklist + merge/diff mutation backstop + real-archive demo + token slice visible.

**Wave 2 — CLI + agent surfaces**
- Typer CLI (info/chats/export/search/verify/decrypt/diff/doctor/stats/vault; --json contract; decrypt→cache path); MCP server (read-only, cursor-paginated, **hard-cap invariant mutation tests — whole-chat dump on default args must go RED**, privacy profiles full/masked/metadata-only, **append-only audit log + property test: applied profile == logged profile** incl. wa.db contact-join leak path); grammar parser contract + 2-consumer drift suite + palette stub; semantic extra (CI smoke lane).
- **Gate 2:** accumulated checklist + **cli-tier coverage 100%** + in-process FastMCP contract tests + the mutation/property tests above + real-archive CLI demo + semantic smoke.

**Wave 3 — Design first, shell first, then screens**
- 3.1 **Figma design phase** (tokens, flagship screens) → **shell port FIRST** (hotreload MDApp→kivymd.app, login-screen components, toast/MDFileManager/MDDropdownMenu/MDTabsBase/mainthread; main.py + component widgets added to pre-bump 1.x goldens) → **atomic kivymd 2.0.0 bump with app-launch smoke green on 2.0.0 BEFORE any screen port counts** → then screens, measured smoothness from the first ported screen. **Pixel/tree-golden lane runs DURING the restyle (Q24), not after** — visual correctness checked while the M3 change happens.
- 3.2 Remaining screens + density/dark + keyboard nav + deep links (wmv://…). **Full 3-consumer grammar drift suite = Gate 3 acceptance.**
- 3.3a **Kivy-free media audit engine** (streaming content-hash + (path,size,mtime) cache + missing/orphan/duplicate reconciliation) + organized bulk export (chat/year/month tree + manifest) — consumes 1.6's pHash.
- 3.3b Media UI (gallery/lightbox/dedupe view). 3.4 Stats.
- **Gate 3:** accumulated checklist + snapshots re-baselined (audited delta) + per-screen behavioral inventory ≥80% + real-render smoothness numbers + integrity-audit assertion green + 3-consumer drift green.

**Wave 4 — Safety + distribution**
- 4.1 Vault (SQLCipher, Argon2id, DPAPI option) + archive→vault migration + **FTS-in-vault parity + drift probe under the actual SQLCipher binding (a third SQLite flavor)** + .wams + import-verify-shred (defect-as-fixture refusal proof) + **recovery-code enrollment precondition + idle auto-lock + annotation sidecar (property test: annotations never write source DBs)**.
- 4.2 Export engine: 4.2a HTML-full-media/CSV/XLSX/txt/Telegram-JSON (+real-Telegram-import validation); 4.2b PDF/RSMF/vCard/legal mode; 4.2c share-safe core (pseudonyms, phone/email/PAN/URL scrub, EXIF strip, redaction-report.json beside every export, --bug-report synthetic-db mode, **per-chat opt-in scopes**).
- 4.3 Acquisition + ADB/emulator rail (BEFORE the writer).
- 4.4 Writer (dry-run default; **gate: emulator restore matrix green + source-immutability on originals incl. media dirs + go/no-go review-by 2026-11-15**).
- 4.5 PyInstaller ONEDIR + Inno Setup + watch daemon (**poll_events MCP tool, profile-aware**; no webhooks — dated Deferred) + **go/no-go review-by 2026-11-15**.
- 4.6 Release pipeline (tag→build→release; SBOM + attestation + **per-release delta manifest (Q23)**; Renovate; weekly drift snapshot; canary pre-release lane (Q25, dated); packaged-artifact smoke as publish precondition).
- **Gate 4:** accumulated checklist + installer smoke on clean profile + vault unlocked via recovery code on fresh profile + emulator matrix + shred-refusal red-proof + allowlist baseline audited.

**Wave 5 — Close-out**
- **5a Commissioned close-out (gates only on OUR evidence):** final release tagged via 4.6; self-reflect + knowledge capture committed; L-55 closed; **core+cli 100% per tier manifest; View allowlist shrink-only since Gate 4**.
- **5b Non-gating courtesy-PR tracker:** PRs from 0.7. Evidence: upstream CI if it exists (upstream has NO .github/workflows today — checks:NONE is a fail-open trap) **ELSE each PR branch run in a locally-pinned matrix (py3.8 + kivymd==1.2.0 + protobuf==4.21.12 + pycryptodomex==3.17), results recorded**. 30-day no-response → fork-as-deliverable (Deferred row).

## Parallel track — Instagram program (firewalled)
Deliverable = **fast RE-ACCESS** (achieved 2026-09-30: g1 app-grade + g2 web, verified; keepalives operational). "Never logged out" is NOT guaranteeable against Meta-side invalidation. Boundary per RUNBOOK (artifact: `D:\vault-or-docs path pending owner option D/A/C choice`): **keepalives are human-paced manual read-only touches (sanctioned; RUNBOOK operations); what is BANNED is automated re-login/refresh/retry loops and credential use.** Phone account untouchable; rotator = manual switcher. Lane A (linked-account switch) awaits owner phone toggle + probe green-light.

## Deferred (dated, reviewed at named gates)
| Item | Review-by |
|---|---|
| Code signing | Gate 4 |
| k-anonymity / re-ID preview | Gate 4 |
| Q18 webhooks | Gate 5a |
| Q25 canary pre-release lane (if cut from 4.6) | Gate 4 |
| IG Q2 scheduler / Q3 / Q4 | IG program |
| 5b courtesy-PR 30-day timers | 2026-12-15 |
| 4.4/4.5 writer + watcher go/no-go | 2026-11-15 (locked at approval) |
