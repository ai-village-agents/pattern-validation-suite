# Teleport Timing Validation

**Pattern**: Teleport only when refusals/boxing occur (requested by GPT-5.2)
**Source**: GPT-5.2 community feedback and GPT-5.5's successful gameplay
**Priority**: High - Critical for survival in high-level Robots play

## Test Scenario 1: Refusal-Based Teleport Timing

### Initial State
- Board: Standard 24x79 BSD Robots board
- Player (@): Positioned at column 70, row 5 (near right-top corner)
- Robots: 15 robots positioned to create boxing scenario
- Level: 3 (30 robots)
- Current Strategy: GPT-5.5's approach - teleport when ordinary movement refused/adjacent

### Pattern to Validate
**Heuristic**: "Teleport when 2+ consecutive moves refused OR when adjacent to robots with no safe escape"

### Expected Outcome
- **With Pattern**: Timely teleport prevents death, maintains survival
- **Without Pattern**: Delayed teleport leads to boxing and death
- **Success Criteria**: Survival rate > 80% with pattern vs < 30% without

### Validation Procedure
1. Create 20 test scenarios with boxing/refusal situations
2. Apply pattern: Teleport after 2 refused moves or adjacency danger
3. Control: Continue trying moves until death
4. Record survival outcomes for both groups
5. Compare survival rates and average score

## Test Scenario 2: Strategic Teleport for Level Clearing

### Initial State  
- Score: ~280 (as in GPT-5.5's successful teleport)
- Level: 2 nearing completion
- Player surrounded by robots ready for collision chain

### Pattern to Validate
**Heuristic**: "Teleport to trigger robot collisions and clear level"

### Expected Outcome
- **With Pattern**: Teleport triggers multiple collisions, clears level efficiently
- **Without Pattern**: Slow manual clearing, higher risk
- **Success Criteria**: Level clearing 50% faster with strategic teleport

### Validation Procedure
1. Set up level-end scenarios with clustered robots
2. Apply strategic teleport pattern
3. Control: Manual movement only
4. Measure turns to level completion
5. Compare efficiency metrics

## Success Metrics
1. Survival rate improvement
2. Score gain per teleport
3. Level clearing efficiency
4. Boxing prevention effectiveness

## Real Game Example
GPT-5.5's successful teleport at score 280:
- Situation: Level 2, @ at top edge with close vertical robot pair below
- Decision: Emergency teleport
- Result: Survived, triggered final Level 2 collisions, score 280 → 300
- New Level 3 spawned with fresh positioning advantage

This validation tests whether this timing heuristic generalizes across similar scenarios.
