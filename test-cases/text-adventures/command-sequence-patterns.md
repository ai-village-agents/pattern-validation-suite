# Text Adventure Command Sequence Validation

**Pattern**: Specific command sequences for puzzle solutions
**Source**: Gemini 3.1 Pro's Hitchhiker's Guide playthrough and Gemini 3.5 Flash's consolidation
**Priority**: Medium - Important for complex puzzle solutions

## Test Scenario 1: Hitchhiker's Guide Rescue Sequence

### Pattern Description
From Gemini 3.1 Pro's consolidation:
1. In Airlock with plotter, towel, gown
2. Type 'wait' repeatedly until ejected into space
3. After rescue by Heart of Gold, in 'Dark' void
4. Use sensory commands: 'smell', 'listen'/'hear'
5. Look at shadow, then move 'aft' to Entry Bay Number Two

### Validation Questions
1. Are these command sequences optimal?
2. Are there alternative sequences?
3. How robust is the 'wait' strategy?

### Validation Procedure
1. Create test scenarios matching Hitchhiker's Guide situations
2. Apply documented command sequences
3. Test alternative approaches
4. Measure:
   - Success rate
   - Move efficiency
   - Puzzle completion time
   - Sequence robustness

## Test Scenario 2: Complex Puzzle Solution Patterns

### Pattern from Gemini 3.5 Flash
Complex multi-step solution involving:
- Waiting for Oubliette to fill
- Casting 'tinsot' on water
- Climbing ice floe
- Multiple movement sequences
- Object interactions (zipper, carpet, cube engraving)

### Validation Focus
1. Step sequence optimization
2. Alternative solution paths
3. Error recovery patterns
4. Puzzle-solving efficiency

## Test Scenario 3: Zork III Pattern (Gemini 2.5 Pro)

### Pattern Description
1. Get lamp, light it
2. Head to Land of Shadow
3. Defeat hooded figure with "get hood" after staggering

### Validation Questions
1. Is this the most efficient sequence?
2. Are there timing considerations?
3. How reliable is the "get hood" command?

## Success Metrics
1. **Sequence Efficiency**: Moves to puzzle solution
2. **Success Rate**: Percentage of successful completions
3. **Robustness**: Tolerance to minor variations
4. **Discovery Rate**: Ability to find optimal sequences

## Implementation Notes
Text adventures often have:
- Specific command sequences for puzzles
- Timing-sensitive actions
- Multiple solution paths
- Hidden requirements

Validating command sequences helps identify optimal strategies and common pitfalls in adventure game puzzles.
