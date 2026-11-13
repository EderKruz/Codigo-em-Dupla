import zipfile,re,sys
src,dst=sys.argv[1:3]
z=zipfile.ZipFile(src); files={n:z.read(n) for n in z.namelist()}
d=files['word/document.xml'].decode()
ps=list(re.finditer(r'<w:p[ >].*?</w:p>',d,re.S))
tx=lambda p:''.join(re.findall(r'<w:t[^>]*>([^<]*)',p))
toc=[m for m in ps if '<w:tab/>' in m.group(0) and re.search(r'<w:t>\d+</w:t></w:r></w:p>$',m.group(0)) and m.start()<d.find('Heading1')]
print(len(toc),tx(toc[0].group(0)),'...',tx(toc[-1].group(0)))
B='<w:r><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:instrText xml:space="preserve"> TOC \\o "1-1" \\h \\z \\u </w:instrText></w:r><w:r><w:fldChar w:fldCharType="separate"/></w:r>'
E='<w:r><w:fldChar w:fldCharType="end"/></w:r>'
a,b=toc[0],toc[-1]
pa=a.group(0); i=pa.find('</w:pPr>')+8; pa=pa[:i]+B+pa[i:]
pb=b.group(0).replace('</w:p>',E+'</w:p>')
d=d[:b.start()]+pb+d[b.end():]
d=d[:a.start()]+pa+d[a.end():]
s=files['word/settings.xml'].decode()
if 'updateFields' not in s: s=s.replace('</w:settings>','<w:updateFields w:val="true"/></w:settings>')
files['word/settings.xml']=s.encode(); files['word/document.xml']=d.encode()
with zipfile.ZipFile(dst,'w',zipfile.ZIP_DEFLATED) as o:
    for n in z.namelist(): o.writestr(n,files[n])
