import re, os
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.dirname(HERE)
src=open(f"{ROOT}/index.html",encoding="utf-8").read()
def unesc(s): return s.replace("&quot;",'"').replace("&amp;","&")
ids=[("fr-concept","concept.html","__SRC_CONCEPT__"),("fr-problem","problem.html","__SRC_PROBLEM__"),("fr-drill","drill.html","__SRC_DRILL__")]
shell=src
for fid,fname,ph in ids:
    m=re.search('(<iframe id="'+fid+'" data-srcdoc=")([^"]*)(")', shell)
    if not m: print("MISS",fid); continue
    open(f"{HERE}/{fname}","w",encoding="utf-8").write(unesc(m.group(2)))
    shell=shell[:m.start(2)]+ph+shell[m.end(2):]
open(f"{HERE}/shell.html","w",encoding="utf-8").write(shell)
print("추출 완료:", [f for _,f,_ in ids]+["shell.html"])
