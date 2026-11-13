import zipfile,re,sys
src,dst=sys.argv[1:3]
M={'9FC9CD':'999999','1F2A30':'1A1A1A','EAF4F6':'EDEDED','0E7C86':'333333','C98A12':'1A1A1A','FBF3E0':'FFFFFF','51606C':'555555','2E74B5':'333333','1F4D78':'333333','0563C1':'1A1A1A'}
z=zipfile.ZipFile(src); files={n:z.read(n) for n in z.namelist()}
for f in ['word/document.xml','word/styles.xml','word/numbering.xml','word/footer1.xml']:
    d=files[f].decode()
    for a,b in M.items(): d=re.sub(a,b,d,flags=re.I)
    files[f]=d.encode()
with zipfile.ZipFile(dst,'w',zipfile.ZIP_DEFLATED) as o:
    for k in z.namelist(): o.writestr(k,files[k])
