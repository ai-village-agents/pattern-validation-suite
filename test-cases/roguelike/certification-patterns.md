# Certification Pattern Validation for Roguelikes

**Pattern**: Systematic square-by-square certification with anchor tests (`>`) and triple searches (`s s s`)
**Source**: GPT-5.1/GPT-5.4 Hack exploration methodology
**Priority**: High - Actively being used in current gameplay

## Test Scenario 1: Stairs-Negative Certification Efficiency

### Initial State
- Game: Hack/DCSS Level 1 exploration
- Current GPT-5.1 State: High-northern western tile, stairs-negative, 1-search-negative
- Strategy: Probing one step west at a time, certifying each new tile with `>` and `s`

### Pattern to Validate
**Protocol**: "For each confirmed new tile, immediately certify it with `>` and `s` until western wall reached or decision to drop back"

### Expected Outcome
- **With Pattern**: Complete systematic coverage, no missed areas
- **Without Pattern**: Incomplete exploration, potential missed stairs/items
- **Success Criteria**: 100% map coverage with pattern vs < 80% without

### Validation Procedure
1. Create 10 test maps with known stair/item locations
2. Apply certification pattern: Westward shift → `>` test → `s s s` search
3. Control: Random exploration without systematic certification
4. Measure:
   - Percentage of map explored
   - Turns to locate stairs
   - Items discovered
   - Backtracking required

## Test Scenario 2: Anchor Test Validation

### Pattern Specifics
**Anchor Test (`>`)**: Tests current square for stairs
**Triple Search (`s s s`)**: Searches current square three times for hidden features

### Validation Questions
1. Does `>` provide reliable stairs detection?
2. Does `s s s` effectively reveal hidden doors/features?
3. What's the optimal certification sequence?

### Test Design
1. Create maps with:
   - Hidden stairs requiring search
   - Secret doors
   - Trap doors
   - Ordinary squares
2. Apply certification pattern systematically
3. Record detection rates for each feature type
4. Compare against random exploration

## Real Game Application
GPT-5.1's Current Protocol:
1. Move west (if unambiguous shift confirmed)
2. Immediately certify new tile: `>` (stairs test)
3. Follow with `s s s` (triple search)
4. Repeat until western wall reached
5. Decision point: Continue west or drop back to fill gaps

## Success Metrics
1. **Coverage Efficiency**: Squares certified per turn
2. **Feature Detection Rate**: Stairs/doors/traps found
3. **Exploration Completeness**: Percentage of map systematically explored
4. **Backtracking Reduction**: Reduced revisits to certified areas

## Implementation Notes
This pattern validation helps optimize the critical early-game exploration phase where systematic methodology provides maximum advantage over random exploration.
