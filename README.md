# 🧃 Filejuicer

**Filejuicer** is a Python-based CLI tool that extracts sensitive and interesting information
from files by aggressively applying regex like it owes you money.

Give it a file.  
It gives you the juice.

---

## 🧠 What Is Filejuicer?

Most files look boring.
Logs, dumps, configs, backups — all “nothing to see here”.

Filejuicer disagrees.

It scans files and extracts things like:
- Emails
- URLs
- IP addresses
- Phone numbers
- Credit card–like patterns
- API keys and secrets
- Tokens (JWTs included)
- MAC addresses
- PAN numbers

If it looks valuable, Filejuicer tries to pull it out.

---

## 🚀 Features

- Supports input formats:
  - `.txt`
  - `.json`
  - `.xml`
- Extracts multiple data types using regex
- Prints results directly to terminal
- Optional output saving
- Supports output formats:
  - `.txt`
  - `.json`
  - `.xml`
- Simple CLI usage with flags

---

## 🧪 Usage

### ▶️ Basic Usage
```bash
python filejuicer.py input.txt

#▶️ With Output File
python filejuicer.py input.json -o output.json

#▶️ Help
python filejuicer.py -h
