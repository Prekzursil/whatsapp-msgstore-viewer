# WhatsApp Reunion — Restore Campaign Chronicle (Oct 21 → Nov 5, 2026)

The complete record of the long attempt: from the first phone tap to the working phone.

## 1. The estate (what everything sits on)

- `D:\BackupFusi\` — 171,709 files / 96.4 GB; all FUSI data consolidated Oct 21 (contacts, both phones, AI-chat corpus)
- `whatsapp-reunion\` — the reunion project: Android1+Android2 corpus, iPhone ChatStorage, Mate transfers, all tools
- **The archive-of-record**: `99-final-bundle\` — v4-complete (615,676 msgs, merge-proven zero-missing) + v5-native-base + all candidates, hashed in MANIFEST-SHA256.txt
- Runbook: `out\whatsapp-restore-research.md` (37KB cited research); memory: zcode project memory + vault checkpoint

## 2. The reunion (how the archive was built)

| Phase | What happened |
|---|---|
| Corpus | Android1 (pre-iPhone era) + Android2 merged: 605,117 msgs → decrypted via E2E key `f007…3bfc` (32-byte key material, hex; proven = the real displayed key by the owner's screenshot) |
| iPhone merge | 7,311 msgs from ChatStorage.sqlite inserted by converter (Phase B), 16,525-msg Jul–Sep 2026 window |
| Tail rescue | 5 post-transfer msgs (Sep 30, incl. the key transmission + IBAN) rescued from the Mate live DB → v2: 612,433 msgs |
| v3 (scrub) | sort_id=0 poison found+fixed on all 7,316 converter rows |
| v4-complete | + 3,243 new post-login msgs from the Honor live pull → **615,676 msgs, 0-missing set-proof** |
| v5-native-base | same delta on the phone-native schema (615,235) — built for the final attempt |

## 3. The restore campaign (every attempt)

| # | Date | What | Result |
|---|---|---|---|
| 1 | Oct 21 AM | User manual first-run | No restore prompt — all storage perms were false; fixed + pm clear |
| 2 | Oct 21 PM | Autonomous drive; EULA→number | **Prefill trap**: my field-clear silently failed; the Google-autofilled 726260241 got submitted — turned out to be the CORRECT number (user-confirmed) |
| 3 | Oct 21 PM | OTP verified by user → key screen | Owner typed the hex key manually → garbled across 16 boxes → "cheie incorectă" ×2 |
| 4 | Oct 21 | Scripted key entry (tap box0 → input text → dump-verify all 16 → ÎNAINTE) | **KEY ACCEPTED** → "Se restabilesc mesajele…" → ran 13.5h overnight = LOOP (6.4 MB written in 10h; ~190 CPU-min) |
| 5 | Nov 4 | A/B: staged the MATE's ORIGINAL backup | **Restored perfectly** (38% → done, 243 MB/90s) — proved our re-encryption format, not the key, was the difference |
| 6 | Nov 4–5 | v2/v4 attempts | Key REJECTED on new build 2.26.42 |
| 7 | Nov 5 | Root-caused acceptance: **zlib level 1 (78 01) + original's 16-byte trailer** | Key ACCEPTED again (candidates v4L1/T6/L1T banked) — but importer still loops (no %, KB-trickle) |
| 8 | Nov 5 | v5 (native-schema base + delta) | Key accepted; import loops identically → **undocumented importer gate on synthetic files; exhausted** |
| 9 | Nov 5 | **FALLBACK executed** (as owner-directed) | Staged the phone's own app-made backup → auto-restored + fresh 02:31 Drive backup → "Restabilire finalizată" → phone WORKING |

## 4. Final state (Nov 5)

- **Phone**: Honor, WhatsApp working, **603,486 messages** (full history + ALL new messages through Nov 4 23:30 UTC), media re-downloading, fresh Drive backup exists
- **PC archive**: complete superset — 615,676 msgs (adds the 11,749-msg delta: iPhone-era + tail, incl. vama grup's 305 missing Aug 5–Sep 19)
- **The gap** (unrecoverable from our sources): messages sent Oct 1–4, 2026 while no device was registered (30-day queue expiry) — exists only on other members' phones

## 5. Key technical discoveries (the reusable knowledge)

1. **Crypt15 acceptance recipe on 2.26.42**: zlib **level 1** (header `78 01`) + original's 16-byte trailer after the GCM tag → key validation passes
2. **The importer gate**: build 2.26.42 imports WhatsApp-made files but silently loops on ANY synthetic file (schema-agnostic — even native-schema bases with merged rows)
3. **Key-entry automation**: programmatic `input text` into box0 + dump-verify 16 boxes; Google autofill sheet truncates mid-box9 → complete the remainder
4. **Number-field injection is blocked** on Honor registration screens (input text, keyevents, SwiftKey, ADBKeyboard IME-commit all silently dropped) — physical typing required
5. **ADBKeyboard install**: `adb install --bypass-low-target-sdk-block` defeats Play Protect's old-app block
6. **Write-telemetry**: `df /data` deltas distinguish healthy import (MB/s + % shown) from loop (KB/min, no %) in minutes
7. **Honor suspend behavior**: backgrounded WhatsApp drops to ~8% duty; screen-on foreground = 30%; doze-off + whitelist prevents death, not throttling

## 6. What remains (owner-decision queue)

- Delta on phone (blocked by importer gate; paths: Mate 2.26.40 test → device-transfer, or future build)
- Perf-knob revert (stayon/doze/thermal), ADBKeyboard removal
- 16 GB media push, SIM2 name-swap, Drive backup scheduling
- The viewer+merger GitHub product (see 23-repo-plan/SCOPING.md)
