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
- **2026-11-10 (day 7):**
  - Change 1 (extended $0.75 band): the 12:35 SPY F/E short closed $0.53 past on 2.3× with QQQ the same bar, which would have qualified for the band. It was blocked by F range age (35 < 45 min) and E's bar-range limit. The shadow would have been stopped (−1R), so the band was not the deciding rule. Neutral.
  - Change 3 (1.5R trail): the C-grade F long shadow trailed out at +0.96R. A 1R trail exits at the 2:12 1-min close $748.05, under $748.31 (+1.19R); the target $750.90 was never reached. **Weak signal against** (C-grade shadow; not counted in the tally). Tally stays 1 against.
  - Change 6 (ORB 2× pole): all four ORB sides cancelled before a flag break. Neutral.
  - Changes 2, 4, 5: no signals.
  - **No playbook changes** (no change has 10 signals; 2-week mark 11/16).
- **2026-11-11 (day 8):**
  - Change 1 (extended $0.75 band with ≥ 1.2×):
    - 1:20 F long, $0.43 past on 0.89×: it would have been stopped (reversed to $759.72), so the gate helped.
    - 2:00 F short, $0.32 past on 1.04×: it would have reached its $760.38 target, so the gate cost.
    - Net neutral (one each).
  - Change 6 (ORB 2× pole target): #57/#58's $695.03 target was reached later (QQQ $695.57 at 1:45), after the time-stop exit. **Weak signal for** (the target was right; the trade was gone). Tally: 2 for (weak).
  - Change 3 (1.5R trail): not armed (best close $692.005 vs $692.02). Neutral.
  - Change 2 (swing stop): the 12:13 E long shadow used a $0.64 swing stop and made +2.97R; it was gated by the target R/R rule, not the stop. Neutral.
  - Changes 4, 5: no signals.
  - **Observation (not a change):** the setup-A 30-min time stop cut #57/#58 at +0.57R; QQQ then ran +4.2R. One signal; it needs a replay of past A trades before any proposal. The time stop is an A trade-management rule, so a change to it would be under the standing rule, but it waits on evidence.
  - **No playbook changes** (no change has 10 signals; 2-week mark 11/16).
- **2026-11-12 (day 9):**
  - Change 1 (extended $0.75 band): the 1:45 F short qualified only via the extended band ($0.73 past, 2.56×, QQQ the same bar). It was graded C, so not taken; the shadow made +2.7R. **Signal for** the band (it identified a working entry). Tally: 1 for / 1 against / 1 neutral (11/11).
  - Change 6 (ORB 2× pole target): no A trade. Neutral.
  - Change 3 (1.5R trail): the shadow F short never got a 1-min close at +1.5R before running (wick only), so the trail was irrelevant. Neutral.
  - Changes 2, 4, 5: no signals.
  - **Observation (not a change; needs a replay):** F breakouts come out of chop, so the score card's required ADX ≥ 20 will usually fail on F triggers. The two C-graded F shadows (11/10, 11/12) both won. Before proposing "for F, ADX is measured after the break, or replaced by the range-age condition", replay the F triggers in the journal (≥ 20 sessions). The score-card required factors are in the playbook (section 3); the A/B-only rule is in CLAUDE.md, so a change to which trades qualify will go to the owner.
  - **No playbook changes** (no change has 10 signals; 2-week mark 11/16).
- **2026-11-13 (day 10): new setup A2, the owner's ORB direct read (owner direction, not a Claude tuning change).**
  - The rule: mark 9:30–9:45; on 1-min bars, a break that holds → trade with it; a swoop past a mark that closes back inside → trade the other way; stop behind the confirming mark or the swoop extreme; exit by 11:00 at the latest.
  - It is paper-tracked alongside A (not replacing it). Every signal is logged with its result.
  - Defaults pending the owner: "comes back" = a 1-min close back inside; the break stop = the broken mark.
  - First read (11/13, from the journal): the SPY break-and-hold short at 10:00 (≈ $753.85, stop ≈ $755.98) → the 11:00 exit ≈ $750.5 ≈ **+1.5R**. On the same move, A missed its flag entry by $0.01. One day is not evidence; a replay of ≥ 20 sessions of A vs A2 is queued.
- **2026-11-13: A2 entry clarified by the owner:** enter at the break (first 1-min close beyond the high or low after 9:45), not after a hold bar. The 5-min re-run (23 days): the mark stop goes 5 W / 18 L, the range-midpoint stop 9 W / 14 L. The stop choice is pending the owner; a 1-min replay is queued.
- **2026-11-13: A2 stop set to the range midpoint ∓ $0.10** (owner OK). A 1-min replay of the 23 sessions is scheduled for 11/14.
- **2026-11-13 (day 10, EOD):**
  - Change 3 (1.5R trail): F shadow #2 (C) trailed out at +0.59R from a +2.4R best; a 1R trail exits ≈ +1.0R. **Weak against** (C shadow; not counted). Tally: 1 against + 2 weak against.
  - Change 1: today's F trigger closed inside the normal $0.30 band → neutral.
  - Changes 2, 4, 5, 6: no signals.
  - A2 entry/stop/exit set by the owner (see the entries above).
  - **No standing-rule playbook changes today.** Verdicts are due 11/16.
- **2026-11-16 (day 11): two-week verdicts for the six owner-approved changes of 11/02** (none reached 10 signals):
  - **1. Extended $0.75 band: KEEP.** 2 for (11/12 F short +2.7R shadow; 11/16 F short +1.46R shadow), 1 against (11/11 1:20 gate helped / 2:00 cost), 3 neutral.
  - **2. E swing stop: RECOMMEND REVERT (owner's call).** 2 against (11/02 R/R gate blocked a 2R winner; 11/03 the stop width cost the option leg), 1 for (11/04), rest neutral. It underperformed at 2 weeks. The previous rule was a fixed $0.40 stop.
  - **3. 1.5R trail: RECOMMEND REVERT to 1R (owner's call).** 1 against (#55: 1R +1.82R vs 1.5R +1.32R), 2 weak against (C shadows 11/10, 11/13), 0 for.
  - **4. D next-level measure: KEEP** (no deciding signal; neutral).
  - **5. Same direction with different setups: KEEP.** 1 against today (A2 #59 + A #60/#61 together hit the daily limit). The owner's A2-vs-A comparison depends on it, so the decision is the owner's.
  - **6. ORB 2× pole / next-level target: KEEP.** 1 for (#55), 2 weak for, rest neutral.
  - Because all six were owner-approved, the two reverts are proposed, not applied. **No playbook edits today.**
  - New observation: F-break shadows are now 5/5 winners (11/10, 11/12, 11/13 ×2, 11/16).

## 2026-11-17 — Owner: stop fractional trades; options only, A2 first

- **Owner instruction (not a tuning change):** "Stop the fractional share
  trades going forward. And focus on options trading and my rules."
- CLAUDE.md trade rule 8 now reads "options only"; rule 1 no longer mentions
  alert stops for fractional shares; the Strategy section names A2 as the
  primary setup.
- Playbook: section 9 (fractional) marked retired; A2 marked primary and
  checked first each morning; SPY/QQQ notes and scoreboard are options-only.
- Fractional track closed at 30 trades, +$6.17.
- Effect this week: the weekly loss budget left is $34.04, below an A2
  contract's $75–125 premium, so A2 and other option signals are logged as
  shadows until Monday 11/23 unless the owner says otherwise.

## 2026-11-17 — Owner: combine SPX, SPY and QQQ for A2

- Owner: "Can we combine SPY SPX QQQ" (and confirmed the 9:47 SPX
  opening-range alert task is theirs).
- A2 is now read on SPX, SPY and QQQ as one signal: the trade is SPXW when
  SPX crosses and holds (stop the SPX midpoint ∓ 1.0 point); SPY/QQQ crosses the
  same way are logged as confirmation, not required; one A2 trade per day per
  direction across all three.
- The 9:47 alert task now reports all three ranges in one push.
- To measure: whether the trades where SPY/QQQ confirmed did better than the
  ones where they didn't (decide after 10 signals).

## 2026-11-17 EOD — observations (no tuning change today)

- **A2:** 2nd straight day the owner's read caught the morning move (11/17 put +50% shadow; the owner's SPXW 7270P likely +50%). The A2 track is still at 1 counted trade; keep collecting.
- **A R/R gate:** skipped another winner (10:18 flag, R/R 1.20 → target hit, +1.2R). Now 2 skips that would have won, 0 that would have lost. Watch this; a change needs ≥ 10 signals.
- **Armed-line hygiene (process, not a setup rule):** every armed line now carries a VWAP-side condition and an R/R ≥ 1.5 check, and the no-chase band is ≤ 25% of the stop distance. The 12:05 and 1:25 fires showed the gap.
- **Flat-VWAP chop:** the only afternoon shadow (the QQQ F long against a flat VWAP) lost −1R. Supports the existing checklist item 1; no change.
- Pending owner decisions unchanged: revert change 2 (E swing stop) and change 3 (1.5R trail); the F-break ADX gate; A2 half-off at +50% with a breakeven stop; this week's weekly-budget override.

## 2026-11-17 — A2 exit: half at +50%, trail the rest 1 bar, out by 11:00 (owner-requested test)

- **Change:** A2 step 4. Old: take everything at +50%, else out at 11:00. New: sell half at +50%, trail the other half one 5-min bar behind (never looser than entry), out by 11:00.
- **Evidence:** `journal/backtests/2026-11-17-a2-exits-9mo.md`, 125 modeled trades over 187 sessions. New exit −$83 vs old −$725. It won in all four periods (Feb–Jun −$317 vs −$427; Jul–Oct −$1 vs −$107; Oct 9–Nov 17 +$235 vs −$190) and had the smallest drawdown (−$741 vs −$1,029).
- **Not chosen:** hold everything to 11:00 (+$816). It lost Feb–Oct; all of its profit came from the last 6 weeks, mostly from 11/5.
- **Caveat:** no exit makes the mechanical A2 entry clearly profitable over 9 months. The exit change cuts losses; the edge question is about entries and the owner's discretion.
- **Review:** after 10 A2 signals or 2 weeks (by 12/1), compare against the old rule on the same signals.

## 2026-11-18 EOD — observations (no tuning change)

- **A2 swoop rule:** the first live test. The 9:47–9:52 poke-and-return flipped to a call that ran to the opposite mark (shadow +$55.50; the owner +$118). Keep it.
- **A2 exit (new, half +50% + 1-bar trail):** on the call, the trail exited the 2nd half at $1.83. The owner's "sell at the opposite mark" got $2.73 on the whole contract. Queued for the next backtest as variant f: "after a swoop reversal, target the opposite mark". No change yet (1 signal).
- **E/F volume bar (1.5×):** missed today's 11:55–12:30 rally (0.88× at the trigger) and fell short at 1:30 (1.44×). 2 signals; no change. Track whether midday triggers should use 1.25× (needs ≥ 10 signals or a replay).
- **Process:** 3 armed lines today lacked the VWAP-side condition; the 2:00 fire was rejected for it. Every line now states its VWAP side.
- **High-IV day:** $0.75–1.25 SPXW contracts were 100–170 points out of the money (the 7260P was $15.40). The bot priced the put shadow on SPY instead. Worth asking the owner whether A2 should allow up to the $125 cap closer to the money on IV > 40% days.
- Pending owner decisions unchanged (change 2/3 reverts, the F ADX gate, the weekly-budget override).
