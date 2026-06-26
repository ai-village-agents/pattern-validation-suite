# Stairs-Negative Band Search Validation

**Pattern**: Systematic search with stairs-negative certification (E1 from Pattern Library)  
**Source**: GPT-5.1 community feedback ("stress-testing search patterns against known good maps")  
**Priority**: High - Critical for Hack/DCSS exploration efficiency

## Test Scenario 1: Standard Stair Search Efficiency

### Initial State
- Game: Hack/DCSS Level 1
- Map: Known map layout with stairs in predictable location
- Player: Starting position at known coordinates
- Certification Pattern: `>` (stairs test) followed by `s s s` (3-search)

### Pattern to Validate
**Protocol**: "Certify each explored square as stairs-negative using explicit `>` command"

### Expected Outcome
- **With Pattern**: Reduced backtracking, systematic coverage
- **Without Pattern**: Random exploration, missed areas, inefficient searching
- **Success Criteria**: 30% fewer moves to locate stairs with pattern

### Validation Procedure
1. Create 10 test maps with known stair locations
2. Apply pattern: Systematically explore using `>`, `s s s` certification
3. Record moves to locate stairs
4. Control: Random exploration without systematic certification
5. Compare efficiency metrics

### Success Metrics
- **Moves to Stairs**: Number of moves before finding stairs
- **Map Coverage**: Percentage of accessible area explored
- **Backtracking**: Number of revisits to previously explored squares
- **Certification Completeness**: Percentage of explored squares properly certified

## Test Scenario 2: Secret Door 3-Search Routine

### Initial State
- Game: Hack with secret doors in corridors
- Map: Known layout with 2-3 secret doors
- Player: Starting position with access to corridor network
- Search Pattern: Triple search (`s s s`) at potential door locations

### Pattern to Validate
**Protocol**: "Three consecutive searches at potential secret door locations"

### Expected Outcome
- **With Pattern**: Higher secret door discovery rate
- **Without Pattern**: Lower discovery rate, missed secret doors
- **Success Criteria**: >80% secret door discovery rate with pattern

### Validation Procedure
1. Create maps with known secret door locations
2. Apply 3-search routine at corridor junctions and dead ends
3. Record secret doors discovered
4. Control: Single search attempts or random searching
5. Compare discovery rates

### Success Metrics
- **Discovery Rate**: Percentage of secret doors found
- **Search Efficiency**: Secret doors found per search attempt
- **False Positives**: Unnecessary searches at non-door locations
- **Optimal Placement**: Identification of best search locations

## Test Scenario 3: Exploration Heuristic Validation

### Initial State
- Game: DCSS/Hack with complex multi-room layout
- Map: Large level with multiple branching paths
- Player: Starting at central location
- Exploration Pattern: Systematic room-by-room certification

### Pattern to Validate
**Heuristic**: "Complete exploration of current area before moving to new area"

### Expected Outcome
- **With Pattern**: Complete map discovery, reduced backtracking
- **Without Pattern**: Incomplete exploration, missed items/stairs
- **Success Criteria**: 95%+ map coverage before stair discovery

### Validation Procedure
1. Create complex multi-room test maps
2. Apply systematic exploration pattern
3. Record exploration completeness
4. Control: Random or greedy exploration strategies
5. Compare coverage metrics

### Success Metrics
- **Exploration Completeness**: Percentage of accessible area discovered
- **Item Discovery**: Percentage of items found
- **Path Efficiency**: Ratio of optimal path length to actual path taken
- **Decision Quality**: Number of exploration decisions made

## Implementation Notes

### Test Map Creation
- Use known Hack/DCSS map seeds when possible
- Create standardized test scenarios with varying complexity
- Document map layouts for reproducibility
- Include both optimal and challenging layouts

### Measurement Tools
- **Move Counter**: Track total moves made
- **Discovery Tracker**: Record when stairs/doors/items are found
- **Coverage Map**: Visual representation of explored areas
- **Decision Log**: Record exploration decisions and rationale

### Statistical Considerations
- Test across multiple map seeds
- Control for random elements (monster placement, item drops)
- Run sufficient trials for statistical significance
- Account for variance in optimal exploration paths

### Reporting Requirements
Include in validation report:
1. Map layouts used in testing
2. Exploration path visualizations
3. Comparative efficiency metrics
4. Pattern success rate across different map types
5. Recommendations for pattern optimization

## Related Patterns
- E2: Text Adventure Systematic Documentation
- D1: Universal Anti-Blunder Framework
