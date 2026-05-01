# Temple Lighting Donation Automation (点灯自动化工具)

Automates monthly temple lighting donation spreadsheet processing. Run twice per month (初一 and 十五) to clear old data, distribute names across four columns, apply formatting, update the date header, save, and export to PDF.

---

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate          # run this every new terminal session
pip install -r requirements.txt    # installs openpyxl + xlwings
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

## Local Configuration

Create `config.local.json` in the project root (it is gitignored):

```json
{
  "excel_file": "/path/to/丙午年初一十五点灯.xlsx",
  "year_stem": "丙午",
  "open_with": "Microsoft Excel",
  "save_pdf_path": "/path/to/pdf/output/folder"
}
```

`save_pdf_path` enables automatic PDF export after each run. The PDF is named `{first 2 chars of excel filename}年{sheet name}.pdf` — e.g. `丙午年三月十五日.pdf`.

---

## Normal Monthly Workflow

You'll do this **twice per month**:

1. Run `python -m temple_lighting`
2. Select `1. Process Single Sheet`
3. Enter your Excel file path (or press Enter to use the saved path)
4. Select the sheet for that month (e.g. `三月初一` or just `5`)
5. Paste your names list and press Enter twice
6. Done — file is saved, PDF exported, and Excel opens (~2 seconds)

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
| Chinese font / size | `format_names_font()` — `Font(name='KaiTi TC', size=15)` |
| English font / size | `format_names_font()` — `Font(name='Aptos', size=13)` |
| Year stem | `TempleWorkflow.__init__()` — loaded from `config.local.json` |
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

**`ModuleNotFoundError: No module named 'openpyxl'`** or **`No module named 'xlwings'`**
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

**"File not found" error** — always use the full absolute path to the Excel file.

**"Sheet not found"** — use the sheet number shown in the list instead of the full name.

**Font renders incorrectly** — KaiTi TC is not installed. Change the font name in `automation.py` to one available on your machine (e.g. `SimHei`), or install KaiTi TC.

**PDF export skipped** — ensure `save_pdf_path` is set in `config.local.json` and xlwings is installed.
