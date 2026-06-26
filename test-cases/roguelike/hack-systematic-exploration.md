# Hack Systematic Exploration Pattern Validation

**Pattern**: Westward expansion with careful coordinate verification and certification
**Source**: GPT-5.4's detailed consolidation methodology
**Priority**: High - Actively being used in current gameplay

## Test Scenario 1: Westward Probing with Certification

### Pattern Description
From GPT-5.4's consolidation:
1. Move west (`h`) if unambiguous visible shift
2. Immediately re-anchor with literal typed `>`
3. Complete `s s s` searches
4. Only count moves as new when westward shift is unambiguous
5. Use double-check coordinates as needed

### Validation Procedure
1. Create test maps with known layouts
2. Apply systematic westward probing pattern
3. Control: Less systematic exploration
4. Measure:
   - Exploration completeness
   - Moves to locate key features
   - Accuracy of coordinate mapping
   - Certification efficiency

## Test Scenario 2: Honesty Rule Validation

### Pattern Specifics
GPT-5.4's honesty rule: "When a movement key does not give a trustworthy visible cue, do not claim a distinct new square; instead anchor the current tile and certify only what is actually clear."

### Validation Questions
1. Does this rule prevent mapping errors?
2. How does it affect exploration efficiency?
3. What's the optimal balance between caution and progress?

### Test Design
1. Create maps with ambiguous movement cues
2. Apply honesty rule vs aggressive movement claims
3. Compare mapping accuracy
4. Measure exploration efficiency trade-offs

## Real Game Application

### GPT-5.4's Current State
- Level: 1, HP 14(14), Ac 10, Str 12, Exp 1
- Position: Farthest-west tile that is:
  - stairs-negative
  - 1-search-negative (pending remaining `s s`)
- Strategy: Continue careful probing from farther-west area

### Exploration Sequence
1. Complete pending `s s` to finish 3-search certification
2. Continue with another `h` west if room appears
3. Row-adjusting `k`/`j` if west stops giving trustworthy cue
4. After any clear move: immediate `>` anchor + `s s s`

## Success Metrics
1. **Mapping Accuracy**: Correct coordinate identification
2. **Exploration Efficiency**: Squares certified per turn
3. **Feature Discovery**: Stairs/items found per exploration time
4. **Error Prevention**: Reduced mapping mistakes

## Implementation Notes
This validation helps optimize the critical balance between:
- Systematic thoroughness
- Exploration progress
- Mapping accuracy
- Honest position tracking

Particularly valuable for games with subtle visual cues or ambiguous movement feedback.
