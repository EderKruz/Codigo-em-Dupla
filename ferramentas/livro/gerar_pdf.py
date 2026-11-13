import uno, sys, time, subprocess, os
from com.sun.star.beans import PropertyValue
def P(n,v):
    p=PropertyValue(); p.Name=n; p.Value=v; return p
src=os.path.abspath(sys.argv[1]); out=os.path.abspath(sys.argv[2])
proc=subprocess.Popen(['soffice','--headless','--invisible','--norestore','--accept=socket,host=localhost,port=2002;urp;'])
ctx=None
for i in range(40):
    try:
        local=uno.getComponentContext()
        res=local.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver',local)
        ctx=res.resolve('uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext'); break
    except Exception: time.sleep(0.5)
desk=ctx.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop',ctx)
doc=desk.loadComponentFromURL('file://'+src,'_blank',0,(P('Hidden',True),))
idx=doc.getDocumentIndexes()
for i in range(idx.getCount()): idx.getByIndex(i).update()
doc.refresh()
doc.storeToURL('file://'+out,(P('FilterName','writer_pdf_Export'),))
doc.close(True)
try: desk.terminate()
except Exception: pass
proc.wait(timeout=30)
print('ok')
