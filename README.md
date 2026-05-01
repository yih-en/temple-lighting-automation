# 🚀 QUICK START GUIDE - Temple Lighting Automation

## What You Got

You now have a complete automation suite with 3 ways to use it:

```
📁 Your Automation Folder
├── temple_lighting_automation.py    (Main script - interactive mode)
├── temple_batch_processor.py        (Batch processor - process multiple sheets)
├── menu.py                          (Simple menu interface - recommended!)
├── batch_config.json                (Configuration file for batch mode)
├── AUTOMATION_GUIDE.md              (Comprehensive documentation)
└── README.md                        (This file)
```

---

## ⚡ QUICKEST START (Recommended)

### Option 1: Using the Menu (Easiest)
```bash
python menu.py
```
Then select option "1. Process Single Sheet"

### Option 2: Direct Interactive Mode
```bash
python temple_lighting_automation.py
```

### Option 3: Batch Mode (For multiple sheets at once)
1. Edit `batch_config.json` with your settings
2. Run:
```bash
python temple_batch_processor.py
```

---

## ✅ Setup Checklist

- [ ] **Step 1: Copy these files to your computer**
  - Save all 4 scripts to a folder (e.g., `~/Desktop/temple/scripts/`)
  
- [ ] **Step 2: Install Python dependencies**
  ```bash
  pip install openpyxl
  ```

- [ ] **Step 3: Verify Excel file location**
  - Make sure you know the full path to your Excel file
  - Example: `/Users/username/Desktop/temple/点灯/丙午年初一十五点灯.xlsx`

- [ ] **Step 4: Run your first workflow**
  ```bash
  python menu.py
  ```

---

## 🎯 Normal Monthly Workflow

You'll do this **twice per month**:

### For 初一 (1st day of the month):
```bash
1. python menu.py
2. Select "1. Process Single Sheet"
3. Enter your Excel file path
4. Select "三月初一" (or whichever month)
5. Paste your names list
6. ✅ Done! File is updated and saved
```

### For 十五 (15th day of the month):
```bash
1. python menu.py
2. Select "1. Process Single Sheet"
3. Enter your Excel file path
4. Select "三月十五日" (or whichever month)
5. Paste your names list
6. ✅ Done! File is updated and saved
```

---

## 📝 Input Format

The script accepts names in this format (with numbers and checkmarks):

```
1.⁠ ⁠李小明
 2.⁠ ⁠李大春✔️
 3.⁠ ⁠林芊芊✔️
...
```

It automatically cleans up:
- ✅ Numbers (1., 2., etc.)
- ✅ Checkmarks (✔️, ✓)
- ✅ Extra spaces
- ✅ Invisible characters

---

## 🔧 Customization Options

### Want to change fonts?
Open `temple_lighting_automation.py` and find:
```python
font = Font(name='KaiTi TC', size=15)
```
Change `'KaiTi TC'` to your preferred font (e.g., `'SimHei'`, `'Arial'`)

### Want to change font size?
Change `size=15` to your preferred size (e.g., `size=12`, `size=16`)

### Want to change footer text?
Find this line:
```python
footer_text="出入平安   生意興隆   身體健康"
```
Replace with your preferred text.

### Want to change year stem?
When running, you can specify the year:
```python
workflow = TempleWorkflow(excel_path, year_stem="丙午")
```

---

## 🔍 Troubleshooting

### "ModuleNotFoundError: No module named 'openpyxl'"
**Fix:** Install it with:
```bash
pip install openpyxl
```

### "File not found" error
**Fix:** Make sure you provide the full file path:
```
❌ Wrong: "丙午年初一十五点灯.xlsx"
✅ Right: "/Users/username/Desktop/temple/点灯/丙午年初一十五点灯.xlsx"
```

### "Sheet not found"
**Fix:** Use the number instead of the full name:
```
❌ Wrong: "三月十五日1"
✅ Right: "6"  (it will show you the available sheets)
```

### Font shows as different style
**Fix:** The system is substituting the font because KaiTi TC isn't installed.
- Install KaiTi TC fonts on your system, or
- Change the font name to one available on your system

---

## 📊 What the Script Does

For each sheet you process, it:

1. **Clears** old names from columns B, E, H, K
2. **Inserts** your new names (up to 104 names across 4 columns)
3. **Numbers** each row automatically
4. **Formats** all names with:
   - Font: KaiTi TC, Size 15
   - Borders: Thin borders around each cell
   - Alignment: Centered both ways
5. **Updates** the date header to: "丙午年三月十五日"
6. **Adds** footer text: "出入平安   生意興隆   身體健康"
7. **Saves** the Excel file

Total time: ~2 seconds! 🚀

---

## 💾 Suggested File Organization

```
Desktop/
├── temple/
│   ├── 点灯/
│   │   ├── 丙午年初一十五点灯.xlsx    ← Your main Excel file
│   │   └── PDFs/                    ← Export folder
│   │       ├── 丙午年正月初一点灯.pdf
│   │       ├── 丙午年正月十五点灯.pdf
│   │       ├── 丙午年三月初一点灯.pdf
│   │       └── 丙午年三月十五点灯.pdf
│   │
│   └── scripts/                     ← Automation scripts
│       ├── temple_lighting_automation.py
│       ├── temple_batch_processor.py
│       ├── menu.py
│       ├── batch_config.json
│       └── names/                   ← Name templates (optional)
│           ├── 正月初一_names.txt
│           ├── 正月十五_names.txt
│           ├── 三月初一_names.txt
│           └── 三月十五_names.txt
```

---

## 🚀 Pro Tips

### Tip 1: Save Names to Files
Instead of pasting every time, save names to files:
- Create `正月初一_names.txt` with one name per line
- Create `正月十五_names.txt` with one name per line
- Reuse these files each year

### Tip 2: Use Batch Mode
For processing multiple months at once:
1. Create names files for each month
2. Edit `batch_config.json`
3. Run `python temple_batch_processor.py`
4. It processes everything automatically

### Tip 3: Schedule It
On Mac/Linux, create a cron job to remind you:
```bash
# Edit crontab
crontab -e

# Add this line (runs on 1st and 15th of each month at 8am):
0 8 1,15 * * /usr/bin/open /path/to/menu.py
```

---

## 📞 Need Help?

1. **Check AUTOMATION_GUIDE.md** - comprehensive documentation
2. **Check script comments** - inline explanations in the code
3. **Modify as needed** - the scripts are designed to be customizable

---

## Version History

- **v1.0** (Current)
  - Initial release
  - Support for interactive mode, batch mode, and menu interface
  - Automatic name cleanup
  - Full formatting support
  - Font customization

---

## License & Disclaimer

These scripts are provided as-is for personal use. Always keep a backup of your Excel file before processing!

---

**Ready to get started? Run this:**
```bash
python menu.py
```

**Happy automating! 🎉**
