#!/usr/bin/env python3
"""
Simple Menu Interface for Temple Lighting Automation
Run this for an easy-to-use menu-driven interface
"""

import os
import sys
from pathlib import Path
import subprocess

def print_menu():
    """Print the main menu"""
    print("\n" + "="*60)
    print("🏯 TEMPLE LIGHTING DONATION AUTOMATION - MAIN MENU")
    print("="*60)
    print("\n1. 🔄 Process Single Sheet")
    print("2. 📦 Batch Process Multiple Sheets")
    print("3. 📖 View Automation Guide")
    print("4. ⚙️  Create/Edit Batch Config")
    print("5. 📂 Open Output Folder")
    print("6. ❌ Exit")
    print("\n" + "-"*60)


def run_single_process():
    """Run the main automation script"""
    print("\n🔄 Starting Single Sheet Processor...")
    try:
        subprocess.run([sys.executable, "temple_lighting_automation.py"])
    except FileNotFoundError:
        print("❌ Error: temple_lighting_automation.py not found")


def run_batch_process():
    """Run the batch processor"""
    print("\n📦 Starting Batch Processor...")
    try:
        subprocess.run([sys.executable, "temple_batch_processor.py"])
    except FileNotFoundError:
        print("❌ Error: temple_batch_processor.py not found")


def view_guide():
    """Display the automation guide"""
    guide_file = "AUTOMATION_GUIDE.md"
    if Path(guide_file).exists():
        with open(guide_file, 'r', encoding='utf-8') as f:
            print("\n" + f.read())
    else:
        print(f"❌ Guide file not found: {guide_file}")


def edit_batch_config():
    """Edit or create batch config"""
    config_file = "batch_config.json"
    print(f"\n📝 Opening {config_file}...")
    
    if not Path(config_file).exists():
        print(f"⚠️  Creating default config...")
        try:
            from temple_batch_processor import create_default_config
            create_default_config(config_file)
        except ImportError:
            print("❌ Error: Could not create default config")
            return
    
    # Try to open with default editor
    if sys.platform == "darwin":  # macOS
        os.system(f"open {config_file}")
    elif sys.platform == "win32":  # Windows
        os.system(f"start {config_file}")
    else:  # Linux
        os.system(f"xdg-open {config_file}")


def open_output_folder():
    """Open the output folder"""
    print("\nWhere is your output folder located?")
    print("Examples:")
    print("  - /Users/username/Desktop/temple/点灯")
    print("  - C:\\Users\\username\\Desktop\\temple\\点灯")
    
    folder_path = input("\nEnter folder path: ").strip()
    
    if Path(folder_path).exists():
        if sys.platform == "darwin":  # macOS
            os.system(f"open '{folder_path}'")
        elif sys.platform == "win32":  # Windows
            os.startfile(folder_path)
        else:  # Linux
            os.system(f"xdg-open '{folder_path}'")
    else:
        print(f"❌ Folder not found: {folder_path}")


def main():
    """Main menu loop"""
    print("\n" + "="*60)
    print("Welcome to Temple Lighting Donation Automation!")
    print("="*60)
    
    while True:
        print_menu()
        choice = input("Select option (1-6): ").strip()
        
        if choice == "1":
            run_single_process()
        elif choice == "2":
            run_batch_process()
        elif choice == "3":
            view_guide()
        elif choice == "4":
            edit_batch_config()
        elif choice == "5":
            open_output_folder()
        elif choice == "6":
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Cancelled by user")
        sys.exit(0)
