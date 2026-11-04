"""Genera datos SINTÉTICOS para probar el análisis; no son mediciones empíricas."""
import csv, random
from pathlib import Path
random.seed(42)
out=Path("resultados");out.mkdir(exist_ok=True)
rows=[]
for mode,base in [("legacy",38.0),("centralized",37.0)]:
    for i in range(1,101):
        rows.append({"mode":mode,"iteration":i,"latency_ms":round(max(1,random.gauss(base,5)),2),"status":"ok" if random.random()>.01 else "error","source":"SINTETICO_DEMO_NO_EMPIRICO"})
with (out/"datos_sinteticos_demo.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
print("Archivo sintético de demostración creado en resultados/datos_sinteticos_demo.csv")
