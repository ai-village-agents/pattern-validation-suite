#!/usr/bin/env python3
"""
Pattern Validation Submission Script

A simple tool for AI Village agents to submit pattern validation results
to the Pattern Validation Suite repository.

Usage:
    python3 submit-validation.py --agent AGENT_NAME --pattern PATTERN_NAME --game GAME --success BOOL

Example:
    python3 submit-validation.py --agent "Claude Opus 4.6" --pattern "teleport-timing" --game "BSD Robots" --success True
"""

import argparse
import json
import datetime
import os
from pathlib import Path

def submit_validation(agent_name, pattern_name, game, success, notes="", score_improvement=None):
    """Submit a pattern validation result."""
    
    # Create results directory if it doesn't exist
    results_dir = Path("results/submissions")
    results_dir.mkdir(parents=True, exist_ok=True)
    
    # Create submission filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{results_dir}/{agent_name.replace(' ', '_')}_{pattern_name}_{timestamp}.json"
    
    # Create submission data
    submission = {
        "agent": agent_name,
        "pattern": pattern_name,
        "game": game,
        "success": success,
        "timestamp": datetime.datetime.now().isoformat(),
        "notes": notes,
        "score_improvement": score_improvement,
        "submission_id": f"{agent_name.replace(' ', '_')}_{timestamp}"
    }
    
    # Write to file
    with open(filename, 'w') as f:
        json.dump(submission, f, indent=2)
    
    print(f"✅ Validation submitted: {filename}")
    print(f"   Agent: {agent_name}")
    print(f"   Pattern: {pattern_name}")
    print(f"   Game: {game}")
    print(f"   Success: {success}")
    
    return filename

def generate_dashboard():
    """Generate a simple dashboard from all submissions."""
    results_dir = Path("results/submissions")
    submissions = []
    
    if not results_dir.exists():
        print("No submissions yet.")
        return
    
    for file in results_dir.glob("*.json"):
        try:
            with open(file, 'r') as f:
                data = json.load(f)
                submissions.append(data)
        except:
            continue
    
    if not submissions:
        print("No valid submissions found.")
        return
    
    # Calculate statistics
    total = len(submissions)
    successful = sum(1 for s in submissions if s.get("success") is True)
    success_rate = (successful / total * 100) if total > 0 else 0
    
    patterns_tested = set(s["pattern"] for s in submissions)
    games_covered = set(s["game"] for s in submissions)
    agents_participating = set(s["agent"] for s in submissions)
    
    # Generate dashboard
    dashboard = f"""# Pattern Validation Dashboard
    
*Last updated: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*

## Overall Statistics
- **Total Validations**: {total}
- **Patterns Tested**: {len(patterns_tested)}
- **Games Covered**: {len(games_covered)}
- **Agents Participating**: {len(agents_participating)}
- **Average Success Rate**: {success_rate:.1f}%

## Pattern Effectiveness Summary

"""
    
    # Group by pattern
    pattern_results = {}
    for sub in submissions:
        pattern = sub["pattern"]
        if pattern not in pattern_results:
            pattern_results[pattern] = {"total": 0, "successful": 0, "games": set(), "agents": set()}
        
        pattern_results[pattern]["total"] += 1
        if sub.get("success") is True:
            pattern_results[pattern]["successful"] += 1
        pattern_results[pattern]["games"].add(sub["game"])
        pattern_results[pattern]["agents"].add(sub["agent"])
    
    # Add pattern details to dashboard
    dashboard += "### Pattern Performance\n\n"
    for pattern, data in sorted(pattern_results.items()):
        pattern_success_rate = (data["successful"] / data["total"] * 100) if data["total"] > 0 else 0
        games_list = ", ".join(sorted(data["games"]))
        agents_list = ", ".join(sorted(data["agents"]))
        
        dashboard += f"**{pattern}**\n"
        dashboard += f"- Success Rate: {pattern_success_rate:.1f}% ({data['successful']}/{data['total']})\n"
        dashboard += f"- Games Tested: {games_list}\n"
        dashboard += f"- Agents: {agents_list}\n\n"
    
    # Write dashboard
    dashboard_file = Path("results/dashboard.md")
    with open(dashboard_file, 'w') as f:
        f.write(dashboard)
    
    print(f"✅ Dashboard generated: {dashboard_file}")
    print(f"   Based on {total} submissions")
    print(f"   Overall success rate: {success_rate:.1f}%")

def main():
    parser = argparse.ArgumentParser(description="Submit pattern validation results")
    parser.add_argument("--agent", required=True, help="Agent name (e.g., 'Claude Opus 4.6')")
    parser.add_argument("--pattern", required=True, help="Pattern name (e.g., 'teleport-timing')")
    parser.add_argument("--game", required=True, help="Game name (e.g., 'BSD Robots')")
    parser.add_argument("--success", type=bool, required=True, help="Whether pattern was successful (True/False)")
    parser.add_argument("--notes", default="", help="Additional notes or observations")
    parser.add_argument("--score-improvement", type=float, help="Score improvement percentage if applicable")
    parser.add_argument("--dashboard", action="store_true", help="Generate dashboard from all submissions")
    
    args = parser.parse_args()
    
    if args.dashboard:
        generate_dashboard()
    else:
        submit_validation(
            agent_name=args.agent,
            pattern_name=args.pattern,
            game=args.game,
            success=args.success,
            notes=args.notes,
            score_improvement=args.score_improvement
        )

if __name__ == "__main__":
    main()
