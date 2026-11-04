"""Benchmark HTTP REAL contra la PoC local. Ejecutar con el servidor activo."""
import urllib.request, time, csv, statistics, json, platform
from datetime import datetime
from pathlib import Path

URL="http://127.0.0.1:8000/api/action"
OUT=Path("resultados")
OUT.mkdir(exist_ok=True)
N=30
rows=[]
for mode in ("legacy","centralized"):
    for i in range(1,N+1):
        start=time.perf_counter()
        status="ok"
        try:
            with urllib.request.urlopen(URL, timeout=5) as response:
                response.read()
                code=response.status
        except Exception as exc:
            status="error"
            code=str(exc)
        ms=(time.perf_counter()-start)*1000
        rows.append({"timestamp":datetime.now().isoformat(timespec="seconds"),"mode":mode,"iteration":i,"latency_ms":round(ms,2),"status":status,"http_code":code,"source":"medicion_real_local"})
        time.sleep(.05)
    print(f"{mode}: {N} solicitudes completadas")
path=OUT/"benchmark_real.csv"
with path.open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
summary={}
for mode in ("legacy","centralized"):
    vals=[r["latency_ms"] for r in rows if r["mode"]==mode and r["status"]=="ok"]
    errs=sum(1 for r in rows if r["mode"]==mode and r["status"]!="ok")
    sv=sorted(vals)
    p95=sv[min(len(sv)-1, int((len(sv)-1)*.95))] if sv else None
    summary[mode]={"n":len(vals),"mean_ms":round(statistics.mean(vals),2) if vals else None,"p95_ms":p95,"errors":errs,"error_rate_percent":round(errs/N*100,2),"source":"medicion_real_local"}
(OUT/"resumen_real.json").write_text(json.dumps({"environment":{"python":platform.python_version(),"platform":platform.platform(),"url":URL},"results":summary},indent=2),encoding="utf-8")
print("Guardado:",path,"y resultados/resumen_real.json")
print("Nota: esta prueba mide latencia HTTP del endpoint local; no mide LCP ni crash rate.")
