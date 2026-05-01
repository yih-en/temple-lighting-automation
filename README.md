# Temple Lighting Donation Automation (点灯自动化工具)

Automates monthly temple lighting donation spreadsheet processing. Run twice per month (初一 and 十五) to clear old data, distribute names across four columns, apply formatting, update the date header, and save.

---

## Setup

```bash
pip install openpyxl
```

Verify your environment:
```bash
python setup_verify.py
```

---

## Usage

### Menu interface (recommended)
```bash
python -m temple_lighting
```

### Direct interactive mode
```bash
python -m temple_lighting.automation
```

### Batch mode (multiple sheets at once)
1. Edit `batch_config.json` with your settings
2. Run:
```bash
python -m temple_lighting.batch
```

---

## Normal Monthly Workflow

You'll do this **twice per month**:

1. Run `python -m temple_lighting`
2. Select `1. Process Single Sheet`
3. Enter your Excel file path (full path, e.g. `/Users/username/Desktop/temple/点灯/丙午年初一十五点灯.xlsx`)
4. Select the sheet for that month (e.g. `三月初一` or just `5`)
5. Paste your names list and press Enter twice
6. Done — file is updated and saved (~2 seconds)

---

## Input Format

Paste names as-is (numbers and checkmarks included):
```
1.⁠ ⁠李小明
 2.⁠ ⁠李大春✔️
 3.⁠ ⁠林芊芊✔️
```
The script automatically strips numbers, checkmarks (✔️, ✓), invisible characters, and extra spaces.

---

## Customization

Open `temple_lighting/automation.py` to change:

| Setting | Location |
|---|---|
| Font / size | `format_names_font()` — `Font(name='KaiTi TC', size=15)` |
| Footer text | `add_footer()` — `footer_text="出入平安   生意興隆   身體健康"` |
| Year stem | `TempleWorkflow.__init__()` — `year_stem="丙午"` |
| Column layout | `insert_names()` — `name_cols = [2, 5, 8, 11]` |

---

## Batch Config

`batch_config.json` is auto-created on first run of batch mode:

```json
{
  "excel_file": "/path/to/your/丙午年初一十五点灯.xlsx",
  "year_stem": "丙午",
  "jobs": [
    {
      "sheet": "正月初一",
      "lunar_date": "正月初一",
      "names_file": "./names/正月初一_names.txt",
      "enabled": true
    }
  ]
}
```

---

## Troubleshooting

**`ModuleNotFoundError: No module named 'openpyxl'`**
```bash
pip install openpyxl
```

**"File not found" error** — always use the full absolute path to the Excel file.

**"Sheet not found"** — use the sheet number shown in the list instead of the full name.

**Font renders incorrectly** — KaiTi TC is not installed on your system. Change the font name in `automation.py` to one available on your machine (e.g. `SimHei`), or install KaiTi TC.

---

## Project Structure

```
temple-lighting-automation/
├── temple_lighting/        # Main package
│   ├── automation.py       # TempleWorkflow class and interactive entry point
│   ├── batch.py            # Batch processor
│   └── cli.py              # Menu interface
├── docs/                   # Documentation
├── tests/
├── requirements.txt
├── pyproject.toml
└── setup_verify.py
```
