#!/usr/bin/env python3
"""Write the gh CLI token into .env (GITHUB_TOKEN=...). Prints no secret."""
import pathlib
import re
import subprocess

out = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
m = re.search(r"\b((?:gho|ghp|github_pat)_[A-Za-z0-9_]+)", out.stdout or "")
if not m:
    raise SystemExit("токен gh не найден в выводе `gh auth token`")
tok = m.group(1)
p = pathlib.Path("/home/crnsfx/Work/pr-scout/.env")
text = p.read_text()
if re.search(r"(?m)^GITHUB_TOKEN=.*$", text):
    text = re.sub(r"(?m)^GITHUB_TOKEN=.*$", f"GITHUB_TOKEN={tok}", text)
else:
    text += f"\nGITHUB_TOKEN={tok}\n"
p.write_text(text)
print(f".env обновлён: GITHUB_TOKEN длиной {len(tok)}, префикс {tok[:4]}…")
