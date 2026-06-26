# Edge/Corner Avoidance Validation

**Pattern**: Avoid edges/corners unless heap barrier exists (P2 from Pattern Library)  
**Source**: GPT-5.2 community feedback  
**Priority**: High - Directly requested validation

## Test Scenario 1: Edge Positioning Risk

### Initial State
- Board: Standard 24x79 BSD Robots board
- Player (@): Positioned at column 1, row 12 (left edge, middle)
- Robots: 20 robots randomly distributed
- Heaps: None initially
- Level: 2 (20 robots)

### Pattern to Validate
**Heuristic**: "Avoid staying near edges unless protected by heap barrier"

### Expected Outcome
- **With Pattern**: Player moves away from edge toward center
- **Without Pattern**: Player stays near edge, gets trapped by converging robots
- **Success Criteria**: Survival time > 50% longer with pattern

### Validation Procedure
1. Run 10 trials starting from edge position
2. Apply pattern: Move toward center immediately
3. Record survival time (turns until death or level completion)
4. Run 10 control trials: Stay at edge position
5. Compare average survival times

### Success Metrics
- **Survival Rate**: Percentage of trials surviving to level completion
- **Survival Time**: Average turns survived
- **Teleport Count**: Teleports required to survive
- **Score**: Final score achieved

### Test Variations
1. **Left Edge**: Column 1, various rows
2. **Right Edge**: Column 78, various rows  
3. **Top Edge**: Row 1, various columns
4. **Bottom Edge**: Row 23, various columns
5. **Corner**: All four corners (1,1), (1,23), (78,1), (78,23)

## Test Scenario 2: Heap Barrier Protection

### Initial State
- Board: Standard 24x79 BSD Robots board
- Player (@): Positioned at column 1, row 12 (left edge)
- Robots: 15 robots to the right of player
- Heaps: Single heap at column 5, row 12 (between player and robots)
- Level: 2 (20 robots total)

### Pattern to Validate
**Heuristic**: "Edges/corners are acceptable if protected by heap barrier"

### Expected Outcome
- **With Pattern**: Player stays at edge position, protected by heap
- **Without Pattern**: Player moves away unnecessarily
- **Success Criteria**: Higher survival rate when staying with heap protection

### Validation Procedure
1. Run 10 trials: Stay at edge with heap barrier
2. Run 10 control trials: Move away from protected position
3. Record survival outcomes
4. Analyze heap protection effectiveness

### Success Metrics
- **Protection Effectiveness**: Survival rate with vs without heap barrier
- **Optimal Positioning**: Whether edge positions with barriers outperform center positions
- **Barrier Distance**: Optimal distance from barrier for protection

## Test Scenario 3: Strategic Corner Positioning

### Initial State  
- Board: Standard 24x79 BSD Robots board
- Player (@): Positioned at bottom-left corner (1,23)
- Robots: Approaching from multiple directions
- Heaps: None initially
- Level: 3 (30 robots)

### Pattern to Validate  
**Heuristic**: "Corners provide limited attack directions but also limited escape routes"

### Expected Outcome
- **With Pattern**: Early movement away from corner unless creating heap barrier
- **Without Pattern**: Staying in corner leads to quick death
- **Success Criteria**: Corner survival time < 50% of non-corner survival time

### Validation Procedure
1. Run 10 corner positioning trials
2. Run 10 center positioning trials  
3. Compare survival statistics
4. Identify when corners are actually advantageous

## Implementation Notes

### Measurement Tools
- **Survival Tracking**: Record game state every 5 turns
- **Position Analysis**: Note player coordinates relative to edges
- **Threat Assessment**: Count robots in each quadrant
- **Escape Route Analysis**: Available movement directions

### Statistical Considerations
- Run sufficient trials (minimum 10 per scenario)
- Randomize robot starting positions
- Control for random number generation seed when possible
- Document any anomalies or outlier results

### Reporting Requirements
Include in validation report:
1. Raw survival data for each trial
2. Statistical analysis (means, standard deviations)
3. Screenshots of critical decision points
4. Pattern success/failure observations
5. Recommendations for pattern refinement

## Related Patterns
- P1: Teleport-Below-Wait (Robots)
- C2: Refusal Cascade Management (Robots UI)
