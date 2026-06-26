# DCSS Combat and Resource Management Pattern Validation

**Pattern**: Potion identification and usage in critical combat situations
**Source**: Claude Sonnet 4.5's DCSS gameplay with potion management
**Priority**: High - Survival-critical patterns in roguelikes

## Test Scenario 1: Emergency Potion Usage

### Pattern Description
From Claude Sonnet 4.5's gameplay:
1. Critical HP situation: HP dropped to 5/25
2. Used j-coppery potion = potion of curing (healed 5→10 HP)
3. Continued combat with ranged tactics
4. After combat, used l-fuming dark potion = potion of heal wounds (HP 8/25→25/25)
5. Result: Survived 6-enemy combat from critical situation

### Validation Questions
1. Optimal potion usage timing
2. Potion identification strategies
3. Combat decision-making under low HP
4. Resource conservation vs survival

### Validation Procedure
1. Create DCSS combat scenarios with varying HP levels
2. Test different potion usage strategies
3. Measure:
   - Survival rate
   - HP preservation
   - Potion efficiency
   - Combat outcome quality

## Test Scenario 2: Ranged Combat Tactics

### Pattern Specifics
Claude Sonnet 4.5's ranged combat approach:
1. Threw darts at range against multiple enemies
2. Used poisoned and curare darts strategically
3. Switched dart types based on enemy and situation
4. Used stones as backup ranged weapon

### Validation Focus
1. Ranged weapon selection efficiency
2. Ammunition conservation strategies
3. Positioning for ranged combat
4. Switching between weapon types

## Test Scenario 3: Exploration and Armour Seeking

### Pattern Description
Current mission: Find leather armour on D:2
Strategy: Auto-explore ('o') while managing threats
Obstacle: 2 dart slugs nearby (dangerous ranged enemies)

### Validation Questions
1. Auto-explore efficiency vs manual exploration
2. Threat assessment during exploration
3. Item prioritization strategies
4. Safe exploration patterns

## Success Metrics
1. **Survival Rate**: Percentage of dangerous encounters survived
2. **Resource Efficiency**: HP preserved per consumable used
3. **Combat Effectiveness**: Enemies defeated per combat
4. **Exploration Efficiency**: Items found per exploration time

## Implementation Notes
DCSS requires:
- Careful resource management
- Strategic combat decisions
- Potion and scroll identification
- Exploration risk assessment
- Equipment prioritization

These patterns are critical for early-game survival and progression in challenging roguelikes.
