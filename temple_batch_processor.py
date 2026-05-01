#!/usr/bin/env python3
"""
Quick Batch Processor - Process multiple sheets with one command
Requires: temple_lighting_automation.py in the same directory

Usage:
    python temple_batch_processor.py

This will process sheets defined in batch_config.json
"""

import json
import sys
import os
from pathlib import Path

# Try to import the main workflow
try:
    from temple_lighting_automation import TempleWorkflow
except ImportError:
    print("❌ Error: temple_lighting_automation.py not found in the same directory")
    sys.exit(1)


def load_batch_config(config_file="batch_config.json"):
    """Load batch processing configuration"""
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"⚠️  Config file not found: {config_file}")
        print("Creating default config template...")
        create_default_config(config_file)
        return None


def create_default_config(config_file):
    """Create a default configuration template"""
    default_config = {
        "excel_file": "/path/to/your/丙午年初一十五点灯.xlsx",
        "year_stem": "丙午",
        "jobs": [
            {
                "sheet": "正月初一",
                "lunar_date": "正月初一",
                "names_file": "./names/正月初一_names.txt",
                "enabled": True
            },
            {
                "sheet": "正月十五日",
                "lunar_date": "正月十五",
                "names_file": "./names/正月十五_names.txt",
                "enabled": True
            },
            {
                "sheet": "三月十五日",
                "lunar_date": "三月十五",
                "names_file": "./names/三月十五_names.txt",
                "enabled": False
            }
        ]
    }
    
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(default_config, f, ensure_ascii=False, indent=2)
    
    print(f"\n📝 Created template: {config_file}")
    print("   Edit this file and set:")
    print("   1. excel_file: path to your Excel file")
    print("   2. jobs[n].enabled: true/false to enable/disable each job")
    print("   3. jobs[n].names_file: path to each month's names file")


def load_names_from_file(file_path):
    """Load names from file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().strip().split('\n')
    except FileNotFoundError:
        print(f"❌ Names file not found: {file_path}")
        return []


def process_batch(config):
    """Process multiple sheets based on configuration"""
    excel_file = config.get("excel_file")
    year_stem = config.get("year_stem", "丙午")
    
    if not Path(excel_file).exists():
        print(f"❌ Excel file not found: {excel_file}")
        return
    
    workflow = TempleWorkflow(excel_file, year_stem)
    jobs = config.get("jobs", [])
    
    completed = 0
    skipped = 0
    failed = 0
    
    print("\n" + "="*60)
    print("🔄 BATCH PROCESSING")
    print("="*60)
    
    for idx, job in enumerate(jobs, 1):
        if not job.get("enabled", True):
            print(f"\n⏭️  [{idx}/{len(jobs)}] SKIPPED: {job['sheet']}")
            skipped += 1
            continue
        
        sheet_name = job.get("sheet")
        lunar_date = job.get("lunar_date")
        names_file = job.get("names_file")
        
        print(f"\n{'='*60}")
        print(f"📋 [{idx}/{len(jobs)}] Processing: {sheet_name}")
        print(f"{'='*60}")
        
        # Load names
        print(f"📂 Loading names from: {names_file}")
        names = load_names_from_file(names_file)
        
        if not names:
            print(f"❌ Failed to load names")
            failed += 1
            continue
        
        print(f"✅ Loaded {len(names)} names")
        
        try:
            workflow.run_workflow(sheet_name, names, lunar_date)
            completed += 1
        except Exception as e:
            print(f"❌ Error: {e}")
            failed += 1
    
    # Summary
    print("\n" + "="*60)
    print("📊 BATCH PROCESSING SUMMARY")
    print("="*60)
    print(f"✅ Completed: {completed}")
    print(f"⏭️  Skipped:   {skipped}")
    print(f"❌ Failed:    {failed}")
    print(f"📁 File:      {excel_file}")
    print("="*60)


def main():
    print("\n" + "="*60)
    print("🏯 BATCH PROCESSOR FOR TEMPLE LIGHTING DONATIONS")
    print("="*60)
    
    # Load config
    config = load_batch_config()
    
    if config is None:
        print("\n⚠️  Please edit batch_config.json and try again")
        return
    
    # Validate config
    excel_file = config.get("excel_file")
    if excel_file == "/path/to/your/丙午年初一十五点灯.xlsx":
        print("\n❌ Error: Please update the Excel file path in batch_config.json")
        return
    
    # Ask for confirmation
    print("\nConfiguration loaded. Ready to process:")
    jobs = config.get("jobs", [])
    enabled_count = sum(1 for j in jobs if j.get("enabled", True))
    print(f"  - Total jobs: {len(jobs)}")
    print(f"  - Enabled: {enabled_count}")
    print(f"  - Excel file: {excel_file}")
    
    confirmation = input("\nProceed? (yes/no): ").strip().lower()
    if confirmation not in ["yes", "y"]:
        print("Cancelled.")
        return
    
    # Process batch
    process_batch(config)


if __name__ == "__main__":
    main()
