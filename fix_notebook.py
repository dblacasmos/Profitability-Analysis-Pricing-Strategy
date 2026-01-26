import json

in_file = "Profitability_Analysis_&_Pricing_Strategy.ipynb"
out_file = "Profitability_Analysis_Pricing_Strategy_FIXED.ipynb"

with open(in_file, "r", encoding="utf-8") as f:
    nb = json.load(f)

# 1) Eliminar metadata de widgets rota (lo que causa el KeyError 'state')
md = nb.get("metadata", {})
if "widgets" in md:
    md.pop("widgets", None)

# 2) También puede venir en metadata de kernelspec/language, eso no molesta, lo dejamos

# 3) Guardar notebook arreglado
nb["metadata"] = md

with open(out_file, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("OK:", out_file)
