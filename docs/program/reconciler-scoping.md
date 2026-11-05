# Viewer + Merger GitHub Product — Scoping (Nov 5, 2026)

## Assets found (the build-onto base)

### A. The viewer — `Prekzursil/whatsapp-msgstore-viewer` (GitHub, public fork)
- Fork of absadiki/whatsapp-msgstore-viewer (Kivy desktop app: decrypt + browse msgstore.db)
- Local clone: `BackupFusi\whatsapp-reunion\tools\oss\whatsapp-msgstore-viewer\` (w/ `wmv-venv`)
- Fork state: 1 commit ahead ("fix: installation") — PUSHED; NO PR to upstream yet
- Local uncommitted: `main.py` pythonw/no-console fix + `run_wmv.pyw` launcher — NOT pushed
- **Built exes exist**: `build\WhatsAppArchiveViewer\WhatsAppArchiveViewer.exe`, `build\WavDiag\WavDiag.exe` (= "the app we have")
- No workflows, no releases on the fork

### B. The merger — loose scripts in the reunion corpus (no repo)
- `99-final-bundle\tools\`: convert_iphone.py (ChatStorage→msgstore converter), encrypt_reconciled.py (crypt15 encryptor), rescue_tail.py
- Session-built: build_v4*.py / build_v5.py (set-based live-merge, orphan handling, jid remapping, message_media copy)
- Decryption stack: Whatsapp_Chat_Exporter (mbs2026 venv) + wa-crypt-tools knowledge
- **Proven capability**: full cross-platform merge with 0-missing set-proof, key-recipe encryption (L1+trailer), write-telemetry verification harness

### C. Session history (from D:\agent-sessions-vault + event ledgers)
- `whatsapp-msgstore-viewer-43df9e87` ledger (Oct 18) — viewer work session
- `whatsapp-mcp-ts-fadaed3b` ledger (Jul 21) — an MCP-for-WhatsApp TS project ("push it and PR it"); **no whatsapp repo materialized** (possibly became fb-messenger-mcp, updated Nov 3)
- The broader AI-session corpus (41,877 sessions, tss manifest) — referenced session sess_af5ac296 was the original reunion-commission session
- **No viewer+merger integrated repo or workflow exists yet** — the idea is scoped but unbuilt

### D. The hard-won knowledge (this campaign — the moat)
- Crypt15 format details: header protobuf (IV slot [8:24], static field4), tag+trailer layout, zlib-level acceptance recipe
- The 2.26.42 importer-gate finding (synthetic files loop) — reversable-engineering target for anyone building restore tooling
- ADB UI-automation harness for the whole registration+restore flow (dump/OCR/verify patterns)

## The product shape (proposed)

**One repo: `whatsapp-reunion-suite`** (or extend the viewer fork) with:
1. `viewer/` — the forked Kivy app (merge local fixes; build via PyInstaller in CI)
2. `merger/` — the corpus scripts productized: CLI (`merge --android X --ios Y --live Z --out msgstore.db`), the set-based verifier, the encryptor with the acceptance recipe
3. `.github/workflows/` — build exes on tag; test merge against fixture DBs; (optional) decrypt-verify integration test using the self-test pattern
4. `docs/` — the campaign chronicle + the technical discoveries

## Open decisions for the owner
- New repo vs extending the viewer fork (GPLv3 inheritance — merger scripts must be GPLv3 if integrated)
- Upstream PR for the viewer fixes (pythonw fix is generally useful)
- Whether the mcp-ts idea (Jul) folds in as a third component
