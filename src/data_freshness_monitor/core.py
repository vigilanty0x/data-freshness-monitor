from datetime import datetime,timezone
def monitor(datasets,*,now,default_max_age_seconds=3600):
 current=datetime.fromisoformat(now.replace("Z","+00:00")); results=[]
 for d in datasets:
  stamp=d.get("observed_at")
  if not stamp: results.append({"id":d["id"],"status":"blocked","age_seconds":None}); continue
  try: age=(current-datetime.fromisoformat(stamp.replace("Z","+00:00"))).total_seconds()
  except ValueError: results.append({"id":d["id"],"status":"blocked","age_seconds":None}); continue
  limit=d.get("max_age_seconds",default_max_age_seconds)
  status="fresh" if 0<=age<=limit else "stale"
  results.append({"id":d["id"],"status":status,"age_seconds":age})
 return {"status":"healthy" if all(r["status"]=="fresh" for r in results) else "degraded","datasets":results}
def run(data): return monitor(**data)

