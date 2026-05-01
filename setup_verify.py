#!/usr/bin/env python3
"""
Setup Verification Script
Run this to verify your automation environment is set up correctly
"""

import sys
import subprocess
from pathlib import Path


def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    print(f"Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 7:
        print("✅ Python version compatible")
        return True
    else:
        print("❌ Python 3.7+ required")
        return False


def check_openpyxl():
    """Check if openpyxl is installed"""
    try:
        import openpyxl
        print(f"✅ openpyxl installed (version: {openpyxl.__version__})")
        return True
    except ImportError:
        print("❌ openpyxl not installed")
        print("   Fix: pip install openpyxl")
        return False


def check_files():
    """Check if required files exist"""
    required_files = [
        "temple_lighting_automation.py",
        "menu.py",
        "README.md"
    ]
    
    all_exist = True
    print("\nRequired Files:")
    for file in required_files:
        if Path(file).exists():
            size = Path(file).stat().st_size / 1024
            print(f"✅ {file} ({size:.1f} KB)")
        else:
            print(f"❌ {file} - NOT FOUND")
            all_exist = False
    
    return all_exist


def check_excel_file():
    """Prompt user for Excel file path and verify"""
    print("\n" + "="*60)
    print("Excel File Verification")
    print("="*60)
    excel_path = input("Enter path to your Excel file (or press Enter to skip): ").strip()
    
    if not excel_path:
        print("⏭️  Skipping Excel file check")
        return None
    
    excel_path = Path(excel_path)
    
    if not excel_path.exists():
        print(f"❌ File not found: {excel_path}")
        return False
    
    if not excel_path.suffix.lower() == '.xlsx':
        print(f"⚠️  Warning: File is not .xlsx format")
        return False
    
    # Try to load it
    try:
        import openpyxl
        wb = openpyxl.load_workbook(excel_path)
        sheets = wb.sheetnames
        print(f"✅ Excel file valid")
        print(f"   Sheets found: {len(sheets)}")
        print(f"   First 5 sheets: {', '.join(sheets[:5])}")
        return True
    except Exception as e:
        print(f"❌ Error reading Excel file: {e}")
        return False


def run_verification():
    """Run all verification checks"""
    print("\n" + "="*60)
    print("🏯 TEMPLE AUTOMATION - SETUP VERIFICATION")
    print("="*60 + "\n")
    
    results = []
    
    # Check Python
    print("1️⃣  Checking Python Installation...")
    results.append(check_python_version())
    
    # Check openpyxl
    print("\n2️⃣  Checking openpyxl Library...")
    results.append(check_openpyxl())
    
    # Check files
    print("\n3️⃣  Checking Required Files...")
    results.append(check_files())
    
    # Check Excel file
    print("\n4️⃣  Checking Excel File...")
    excel_result = check_excel_file()
    if excel_result is not None:
        results.append(excel_result)
    
    # Summary
    print("\n" + "="*60)
    print("VERIFICATION SUMMARY")
    print("="*60)
    
    if all(results):
        print("✅ All checks passed! You're ready to go!")
        print("\nNext steps:")
        print("1. Run: python menu.py")
        print("2. Select: 1. Process Single Sheet")
        print("3. Follow the prompts")
        return 0
    else:
        print("⚠️  Some checks failed. See details above.")
        print("\nCommon fixes:")
        print("• openpyxl: pip install openpyxl")
        print("• File path: Use full absolute path")
        print("• Python: Upgrade to Python 3.7+")
        return 1


if __name__ == "__main__":
    try:
        exit_code = run_verification()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n⚠️  Verification cancelled")
        sys.exit(1)
