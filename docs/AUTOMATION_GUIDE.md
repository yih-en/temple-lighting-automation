# 🏯 Temple Lighting Donation Automation Tool
## 点灯自动化工具使用指南

### Overview (概述)
This tool automates the monthly lighting donation spreadsheet processing for the temple. Use it twice per month:
- **初一 (Initial day)** - Around the 1st of each lunar month
- **十五日 (15th day)** - Around the 15th of each lunar month

---

## Installation (安装)

### Requirements
- Python 3.7+
- openpyxl library

### Setup Steps

1. **Download the script** to your computer:
   - Save `temple_lighting_automation.py` to your project folder
   - Example: `~/Desktop/temple/scripts/`

2. **Install Python dependencies** (run once):
   ```bash
   pip install openpyxl
   ```

3. **Optional: Install for PDF export** (if needed):
   ```bash
   pip install reportlab
   ```

---

## Usage (使用方法)

### Quick Start

1. **Open Terminal/Command Prompt** in your folder
   ```bash
   # Mac/Linux
   python3 temple_lighting_automation.py
   
   # Windows
   python temple_lighting_automation.py
   ```

2. **Follow the prompts**:
   - Enter path to your Excel file
   - Select which month sheet to process (e.g., "三月十五日")
   - Choose how to input names (paste or from file)
   - Paste your name list and press Enter twice

3. **Done!** The file will be updated and saved automatically

---

## Step-by-Step Workflow

The script performs these steps automatically:

### ✅ Step 1: Clean Old Data
Clears existing names from columns B, E, H, K (rows 5-30)

### ✅ Step 2: Insert New Names
Distributes your 93 names across 4 columns:
- **Column B (姓名)**: Names 1-26
- **Column E (姓名)**: Names 27-52
- **Column H (姓名)**: Names 53-78
- **Column K (姓名)**: Names 79-93

### ✅ Step 3: Add Numbering
Numbers each row (1-26 per column)

### ✅ Step 4: Apply Formatting
- Font: **KaiTi TC**, Size **15**
- Alignment: Centered, both horizontally and vertically
- Borders: Thin borders around all name cells

### ✅ Step 5: Update Date Header
Sets Row 2 to: "**丙午年三月十五日**" (or appropriate month)

### ✅ Step 6: Add Footer
Adds blessing text at the bottom:
**"出入平安   生意興隆   身體健康"**
- Font: KaiTi TC, Size 38, Bold

### ✅ Step 7: Save & Export
- Saves the Excel file
- Exports to PDF (if available)

---

## Input Formats

### Option 1: Paste Format (推荐)
Paste your list exactly as you have it:
```
1.⁠ ⁠李大明✔️
 2.⁠ ⁠李小明✔️
 3.⁠ ⁠林芊芊✔️
...
```
The script automatically removes:
- Numbers (1., 2., 3., etc.)
- Checkmarks (✔️, ✓)
- Extra spaces and invisible characters

### Option 2: Text File Format
Create a `names.txt` file with one name per line:
```
李大明
李小明
林芊芊
...
```

Then select option "2" when prompted and provide the file path.

---

## Available Month Sheets

The script automatically lists all available sheets:
```
1. 正月初一
2. 正月十五
3. 二月初一
4. 二月十五日
5. 三月初一
6. 三月十五日
7. 四月初一
8. 四月十五日
... and more
```

---

## File Structure Recommendation

Organize your files like this:

```
Desktop/
├── temple/
│   ├── 点灯/
│   │   ├── 丙午年初一十五点灯.xlsx    (Main Excel file)
│   │   ├── 丙午年初一十五点灯.pdf     (Output PDF)
│   │   └── PDF exports/
│   │       ├── 丙午年正月初一点灯.pdf
│   │       ├── 丙午年正月十五点灯.pdf
│   │       └── ...
│   └── scripts/
│       ├── temple_lighting_automation.py  (This script)
│       ├── names_templates/
│       │   ├── 正月初一_names.txt
│       │   ├── 正月十五_names.txt
│       │   └── ...
```

---

## Common Workflow: Monthly Process

### Twice Per Month Process:

**Around the 1st of the month (初一):**
1. Collect names for that day's ceremony
2. Save them in a text file or have ready to paste
3. Run the script, select the "初一" sheet
4. Paste names when prompted
5. Script completes automatically

**Around the 15th of the month (十五):**
1. Repeat the same process for the "十五日" sheet

---

## Troubleshooting (故障排除)

### Problem: "File not found"
**Solution:** Make sure you're providing the complete file path:
```
/Users/username/Desktop/temple/点灯/丙午年初一十五点灯.xlsx
```

### Problem: "Sheet not found"
**Solution:** Check the exact sheet name in your Excel file. Use the number instead:
```
When asked for sheet: just type "6" instead of the full name
```

### Problem: "openpyxl not installed"
**Solution:** Install it:
```bash
pip install openpyxl
```

### Problem: Font doesn't show as "KaiTi TC"
**Solution:** If KaiTi TC isn't installed, use an alternative:
- Edit the script: change `'KaiTi TC'` to `'SimHei'` or `'Calibri'`
- Or install KaiTi TC fonts on your computer

### Problem: PDF export fails
**Solution:** 
- Option 1: Export manually from Excel (Ctrl+S / Cmd+S as PDF)
- Option 2: Install reportlab: `pip install reportlab`

---

## Advanced: Batch Process Multiple Sheets

If you want to process multiple sheets at once, create a configuration file:

**batch_config.json:**
```json
{
  "excel_file": "/Users/username/Desktop/temple/点灯/丙午年初一十五点灯.xlsx",
  "jobs": [
    {
      "sheet": "正月初一",
      "lunar_date": "正月初一",
      "names_file": "./names_templates/正月初一_names.txt"
    },
    {
      "sheet": "正月十五日",
      "lunar_date": "正月十五",
      "names_file": "./names_templates/正月十五_names.txt"
    }
  ]
}
```

Then run:
```bash
python temple_lighting_automation.py --batch batch_config.json
```

---

## Support & Customization

### Want to customize something?
- **Change font**: Edit line with `Font(name='KaiTi TC'...)`
- **Change font size**: Edit the `size=15` parameter
- **Change footer text**: Edit the footer text in the script
- **Change date format**: Edit the date formatting logic

### Questions?
Refer to the inline comments in the script or modify as needed!

---

## Version Info
- Version: 1.0
- Last Updated: 2024
- Compatibility: Python 3.7+, Windows/Mac/Linux

---

**Happy automating! 🙏**
