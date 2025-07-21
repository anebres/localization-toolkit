# 🌍 Localization QA Toolkit

A lightweight Python command-line toolkit for verifying translation quality in multilingual apps.

This tool helps **Localization Engineers** and **QA testers**:
- Detect untranslated or identical strings
- Validate placeholder consistency between source and target
- Flatten nested translation files
- Run quick, scriptable checks from the command line

---

## 🚀 Features

- ✅ Detect untranslated strings
- ⚠️ Compare placeholders between source and target
- 📄 Supports nested JSON translation files
- 🛠 CLI-based — easy to use with automation or CI pipelines

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/localization-toolkit.git
cd localization-toolkit
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
