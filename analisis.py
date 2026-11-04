"""Resume los datos reales del benchmark. No mezcla archivos sintéticos."""
import csv, statistics, json
from pathlib import Path
p=Path("resultados/benchmark_real.csv")
if not p.exists():
    raise SystemExit("No existe resultados/benchmark_real.csv. Ejecuta primero python benchmark.py")
data=list(csv.DictReader(p.open(encoding="utf-8")))
summary={}
for mode in ("legacy","centralized"):
    subset=[r for r in data if r["mode"]==mode]
    vals=sorted(float(r["latency_ms"]) for r in subset if r["status"]=="ok")
    errors=sum(r["status"]!="ok" for r in subset)
    p95=vals[min(len(vals)-1, int((len(vals)-1)*.95))] if vals else None
    summary[mode]={"n":len(subset),"mean_ms":round(statistics.mean(vals),2) if vals else None,"p95_ms":p95,"errors":errors,"error_rate_percent":round(errors/len(subset)*100,2) if subset else None}
Path("resultados/analisis_real.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
print("Este análisis resume exclusivamente benchmark_real.csv.")
