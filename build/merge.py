import os
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
def esc(s): return s.replace("&","&amp;").replace('"',"&quot;")
shell=open(f"{HERE}/shell.html",encoding="utf-8").read()
for ph,fn in [("__SRC_CONCEPT__","concept.html"),("__SRC_PROBLEM__","problem.html"),("__SRC_DRILL__","drill.html")]:
    shell=shell.replace(ph, esc(open(f"{HERE}/{fn}",encoding="utf-8").read()))
open(f"{ROOT}/index.html","w",encoding="utf-8").write(shell)
print("병합 완료 -> index.html", len(shell),"chars")
