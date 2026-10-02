"""Rewrites the block between <!--RECENT:START--> and <!--RECENT:END--> in README.md
with your most recently pushed public repos (forks and the profile repo excluded)."""
import json, os, re, urllib.request

user = os.environ["GH_USER"]
req = urllib.request.Request(
    f"https://api.github.com/users/{user}/repos?sort=pushed&per_page=100&type=owner",
    headers={"Authorization": f"Bearer {os.environ.get('GH_TOKEN','')}",
             "Accept": "application/vnd.github+json"})
repos = json.load(urllib.request.urlopen(req))
repos = [r for r in repos if not r["fork"] and not r["archived"] and r["name"].lower() != user.lower()][:8]

rows = ["| Project | What it is | Stack | Updated |", "|---|---|---|---|"]
for r in repos:
    desc = (r["description"] or "—").replace("|", "/")[:80]
    lang = r["language"] or "—"
    rows.append(f"| [**{r['name']}**]({r['html_url']}) | {desc} | `{lang}` | {r['pushed_at'][:10]} |")
block = "<!--RECENT:START-->\n" + "\n".join(rows) + "\n<!--RECENT:END-->"

text = open("README.md", encoding="utf-8").read()
text = re.sub(r"<!--RECENT:START-->.*?<!--RECENT:END-->", block, text, flags=re.S)
open("README.md", "w", encoding="utf-8").write(text)
