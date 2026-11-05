import json
from pathlib import Path

data = json.loads((Path(__file__).resolve().parents[1] / "data" / "official.json").read_text(encoding="utf-8"))
assert data["currency"] == "CAD"
assert len(data["departments"]) == 21
assert sum(x["amount"] for x in data["departments"]) == 14_336_888_000
assert len(data["cases"]) == 4
assert len({x["id"] for x in data["cases"]}) == 4
for x in data["financials"]:
    assert x["amount"] >= 0 and x["source"] in data["sources"]
for x in data["departments"]:
    assert x["amount"] >= 0 and x["source"] in data["sources"]
for x in data["cases"]:
    assert x["source"] in data["sources"]
    assert x["status"] == "Official audit finding"
for x in data["sources"].values():
    assert x["url"].startswith("https://")
print("Official dataset validation passed.")
