# Playbook changelog

Every playbook change: date, what changed, why, evidence, and the later
verdict (keep or revert after 10 signals or 2 weeks). Owner-approved changes
are marked; the rest are Claude's under the CLAUDE.md tuning rule.

| Date | Change | Approved by | Evidence | Verdict |
|---|---|---|---|---|
| 2026-11-02 | 1. E/F close band: $0.31–0.75 past the level also fires on ≥ 1.2× volume and a same-bar QQQ break (section 10) | Owner | 10/22–10/30 band-skips: some real moves, some reversals (journal/missed-moves.md) | Pending |
| 2026-11-02 | 2. Swing stop: farther of breakout bar + $0.10 and last 5-min swing + $0.05, minimum $0.40 (setup E, section 10) | Owner | Fixed $0.40 stops hit by noise 10/21 ×2, 10/23, 10/30 (#48 by $0.07) | Pending |
| 2026-11-02 | 3. Trail 1.5R behind the best price instead of 1R (section 7, section 9) | Owner | 10/16–10/20 trails did better at 1.5R; 10/27 did better at 1R | Pending |
| 2026-11-02 | 4. Setup D: next level within 0.5R → measure to the level after it, enter on the close through the first | Owner | 10/23 D long skipped at 0.4R ran +$4.3 | Pending |
| 2026-11-02 | 5. SPY/QQQ: same direction allowed when the setups differ, within the 3-position and 20% caps | Owner | 10/27 QQQ ORB-flag winner blocked (+0.74R shadow) | Pending |
| 2026-11-02 | 6. ORB flag: reference target = next mapped level, else 2× pole; 2-bar counter-drift flags count | Owner | 0 ORB entries 10/27–10/30 under the 1× pole gate | Pending |

## Observations (not verdicts yet)

- **2026-11-02 (day 1 of the six changes):**
  - Change 1 (extended band): not tested; the 10:15 SPY close was $0.90 past, beyond $0.75.
  - Change 2 (swing stop): **one signal against.** The 2:00 E short passed every trigger condition but failed R/R with the swing stop (0.47R); with the old $0.40 stop it was 2.0R and SPY fell $3.55 more. Track: count E/F signals the swing stop blocks vs the losses it prevents.
  - Change 3 (1.5R trail): #51 exited at its target before the trail mattered (a 1R trail would have exited at $757.725, the target at $757.13). Neutral.
  - Change 4 (D reward to the next level): the 10:55 D short was still skipped (0.76R); price fell $4. Neutral to slightly against (the old rule skipped it too).
  - Change 5 (different setups per direction): QQQ's A long was the same setup as SPY's, so not tested.
  - Change 6 (ORB reference target): #50 passed under both the old and new rule; the 10:00 flag break failed under both. Neutral.
- **2026-11-03 (day 2):**
  - Change 1 (extended band): one near-miss; the 10:55 SPY close was $0.35 past (band $0.30) on 1.01× (extended band needs 1.2×). The next bar fired inside the normal band. Neutral.
  - Change 2 (swing stop): #53/#54 used a $2.38 swing stop; the trade was time-stopped, not stopped. The option lost $42 (−52%); a $0.40 stop would have cut it at about −$25. **One signal against** (stop width hurt the option leg). Running tally: 2 against, 0 for.
  - Change 3 (1.5R trail): not reached. Change 4 (D): no signal. Change 5: not tested (QQQ's E long was the same setup). Change 6 (ORB target): the SPY ORB long cancelled before any flag. Neutral.
- **2026-11-04 (day 3):**
  - Change 2 (swing stop): the 11:58 E long above the day high was gated (0.4R with the swing stop). With the old $0.40 stop it would have fired at 1:00 (close $768.85) and been stopped at 1:05 (low $768.44 < $768.45): **one signal for** (the swing stop avoided a loss). Running tally: 2 against, 1 for.
  - Change 4 (D): the 10:15 D short at the 20-day failed R/R under both the old and new measurement. Neutral.
  - Change 6 (ORB): both ORB long breaks cancelled before a flag break (SPY 10:02, QQQ 10:23). Neutral.
  - Changes 1, 3, 5: not tested.
- **2026-11-05 (day 4):**
  - Change 3 (1.5R trail): **one signal against.** #55 trailed out at +1.32R (QQQ $660.82). A 1R trail would have exited at $659.21 (+1.82R), and holding to the reference target $653.32 would have made +3.66R (hit at 10:46). Running tally: 1 against, 0 for.
  - Change 6 (ORB reference target, 2× pole): the QQQ target $653.32 (2× pole) was reached: **one signal for** (the old 1×-pole target $659.22 would have capped it). The SPY flag failed R/R under both rules (0.35R to $750.36). Running tally: 1 for.
  - Change 2 (swing stop): no E/F signal reached the stop question (every close was outside the band). Neutral.
  - Changes 1, 4, 5: change 1 (extended band) gated two near-misses on volume (11:40 at 0.8×, 2:00 at 1.11×), both of which fell further and then reversed; neutral. Change 4: no D signal. Change 5: not tested.
  - **No playbook changes today** (no change has 10 signals yet; the trail evidence is one trade).
- **2026-11-06 (day 5, Friday; weekly summary in journal/paper-trades.md):**
  - Change 1 (extended band): the 1:30 F long closed $1.14 past (beyond $0.75); not tested. Neutral.
  - Change 6 (ORB target): no ORB break on volume; not tested.
  - Changes 2–5: no signals.
  - Running tallies: change 2: 2 against / 1 for; change 3: 1 against; change 6: 1 for. **No verdicts yet** (none has 10 signals; 2-week mark 11/16). No playbook changes this week.
- **2026-11-09 (day 6):**
  - Change 3 (1.5R trail): #56 exited at +3.34R; a 1R trail would have exited on the same 11:04 bar (both trails were above the 11:04 close). Neutral. Tally: 1 against.
  - Change 6 (ORB 2× pole target): #56's $680.94 target wasn't reached (high $678.85); the trail exited first. Neutral. Tally: 1 for.
  - Change 5 (different setups same direction): not tested (no second setup fired).
  - Change 1 (extended band): the 12:05 SPY E close $0.33 past didn't qualify (0.8× volume, no QQQ break). Neutral.
  - **No playbook changes** (no change has 10 signals; 2-week mark 11/16).
