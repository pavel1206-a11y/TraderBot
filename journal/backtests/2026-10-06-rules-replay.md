# Rules replay: 9/29–10/6 (6 paper days), old vs proposed rules

Owner asked (10/6): "Need to get better and not miss things. Run it."

## Method
- SPY + QQQ 5-min bars, 9/29–10/6 (prior day 9/28 for pivots). Script: `replay_rules.py` (run: `python3 replay_rules.py bars.json`).
- Mechanical versions of setups A (ORB), B (VWAP pullback), E/F (close through a key level or a 45-min range edge < $2.50), and D (sweep then close back across VWAP). Setup C is not modeled.
- Same risk rules for every variant: entries 9:45–2:25, one position at a time, max 3 trades a day, stop after 2 losses, reward/risk ≥ 1.5 at the actual entry, exit by 3:30. If the stop and target are in the same bar, the stop counts.
- Results are in SPY points and R (multiples of risk), not option prices.
- **Caveat:** 6 days, in-sample, small trade counts. One or two trades move every total. Treat these results as direction, not proof.

## Results (net R over 6 days)

| Change tested alone | Exit at next level | Exit at +1R | Exit at +1.5R |
|---|---|---|---|
| Current rules | 2 trades, −1.99R | 2, +0.01R | 2, +0.51R |
| **Volume: ≥ 1.0×, or ≥ 0.7× when QQQ breaks its own range the same bar** | **6, +2.58R** | **7 (5 wins), +3.00R** | **7, +3.03R** |
| Remove the narrow entry band (allow closes up to $0.60 past the level) | 4, −3.99R | — | — |
| Volume rule + band $0.20 / $0.30 / $0.60 (1R exit) | — | +0.02R / −0.98R / −0.98R | — |
| Range-height targets | 2, −1.99R (no change) | — | — |
| D sweep-and-reclaim, mechanical | 4, −2.65R | VOL+D: +2.00R (worse than VOL) | — |
| Wider level stops ($0.60 / $0.80 / $1.00) | worse or no better in every case | — | — |

## Conclusions
1. **Adopt (pending owner OK): the volume change.** It helped in every exit variant and caught the logged 10/2 11:05 breakdown and a 10/5 quiet-trend leg.
2. **Adopt (pending owner OK): take the first target at +1 to 1.5R on SPY**, for fractional trades too. That matches the +50% option exit already in use. Holding for the next level turned winners into stop-outs. The trend-day runner rule (section 7) stays for the second contract.
3. **Reject: removing the narrow entry band.** It was my idea after today's misses, and the data says it is wrong. Chasing closes even $0.20 past the level erased the gain. Keep the tight band; it is the no-chase rule working.
4. **Reject for now:** a mechanical D sweep-and-reclaim, range-height targets, and wider stops.
5. **Not fixed by any variant:** the 10/6 10:30–11:25 rally and the 10/5 10:05 ORB. Some moves will be missed; the rules should not be loosened to chase them.

## Follow-up test (2026-10-08), before applying changes
Owner (10/8): "Adjust to hit target next time." Same script and data, volume rule on:

| Variant | Exit at level | +1R | +1.5R |
|---|---|---|---|
| B close cap VWAP + $0.15 kept, E/F band $0.10 | +2.58R | +3.00R | +3.03R |
| B close cap removed, E/F band $0.10 | +2.58R (no change) | +3.00R | +3.03R |
| B close cap removed, E/F band $0.11 | +0.59R | +1.01R | +1.04R |

Applied to the playbook (owner-approved): volume ≥ 1.0× (≥ 0.7× with a same-bar QQQ break) for E/F; first target +1.5R; no VWAP close cap on B (reward/risk ≥ 1.5 at the actual close instead). Kept: the $0.10 band on E/F/C. On 10/7 the new B rule would have fired the 11:15 near-miss (entry $774.85, stop $774.25, +1.5R = $775.75, hit at 11:35). The 11:45 E miss ($0.01 over the band) would still be a miss.
