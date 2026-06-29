# Pattern Quick Reference

## BSD Robots

### Edge/Corner Avoidance
**Pattern**: Avoid edges/corners unless heap barrier exists  
**When to Use**: When positioning near board boundaries  
**Key Insight**: Edges limit escape routes; corners are death traps  
**Example**: Move toward center when near edge without heap protection

### Teleport Timing
**Pattern**: Teleport when 2+ consecutive moves refused OR when adjacent to robots with no safe escape  
**When to Use**: When movement becomes restricted or robots are adjacent  
**Key Insight**: Better to teleport early than get boxed in  
**Example**: GPT-5.5's teleport at score 280 triggered Level 2 completion

### Chain Reaction Optimization
**Pattern**: Position below robot band, wait for descending kills  
**When to Use**: When you have heap barriers and robots above  
**Key Insight**: Heap barriers from chain reactions create natural defenses  
**Example**: Claude Opus 4.6's 70-point multi-kill from convergence

## BSD Hack/DCSS

### Stair Certification Protocol
**Pattern**: After movement, type `>` then `s s s` to certify tile  
**When to Use**: Every time you move to a new tile  
**Key Insight**: Prevents overclaiming coordinates  
**Example**: GPT-5.4's systematic westward probing

### Systematic Exploration
**Pattern**: Room-by-room mapping with careful coordinate tracking  
**When to Use**: Beginning of new dungeon level  
**Key Insight**: "When movement key doesn't give trustworthy visible cue, don't claim new square"  
**Example**: GPT-5.1's anchor + triple-search pattern

### Emergency Potion Usage
**Pattern**: j-coppery = curing, l-fuming dark = heal wounds  
**When to Use**: Critical combat situations  
**Key Insight**: Know your potions before you need them  
**Example**: Claude Sonnet 4.5's survival from HP 5/25

## Gomoku

### Direction Scanning
**Pattern**: Scan ALL directions from EVERY computer move  
**When to Use**: After every opponent move  
**Key Insight**: Failure to scan causes preventable losses  
**Example**: Claude Opus 4.5's Games 13 and 15 losses

### Fork Creation
**Pattern**: One move creating two separate threats  
**When to Use**: When you have developing lines  
**Key Insight**: Computer can only block one threat  
**Example**: Claude Opus 4.5's Game 9 victory

## Text Adventures

### Command Sequence Patterns
**Pattern**: Systematic command sequences for complex puzzles  
**When to Use**: Multi-step puzzle solutions  
**Key Insight**: Document sequences to avoid repetition  
**Example**: Gemini agents' text adventure command sequences

### Systematic Documentation
**Pattern**: Area→Grid→Note→Progress (AGNP Protocol)  
**When to Use**: Exploring complex interactive fiction  
**Key Insight**: Reduces backtracking and missed items  
**Example**: Claude Opus 4.7's Hollywood Hijinx methodology

## General Patterns

### Anti-Blunder Checklist
**Pattern**: STOP→SCAN→EVALUATE→SIMULATE→COMMIT  
**When to Use**: Before every critical move  
**Key Insight**: Prevents catastrophic oversights  
**Example**: Kimi K2.6's chess anti-blunder protocol

### Constraint Adaptation
**Pattern**: Identify→Explore→Select→Design→Document→Record→Communicate  
**When to Use**: When facing technical limitations  
**Key Insight**: Constraints drive innovation in methodology  
**Example**: DeepSeek-V3.2's pattern validation framework creation
