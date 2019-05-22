import sys,re
sys.setrecursionlimit(1000000)

def lines(file):
#     """
#     生成器,在文本最后加一空行
#     """
#
     for line in file: yield line
     yield '\n'
    
     # for line in lines(file):
     #     if line.strip():
     #         line.append(line)
     #     elif line:
     #         yield ''.join(line).strip()

print('<html><body>')
        
title = True
for line in lines(sys.stdin):
    line = re.sub(r'\*(.+?)\*',r'<em>\1</em>',line)
    if title:
         print('<p>')
         print (line)
         print ('</p>')
         title =False
    else:
         print('<p>')
         print (line)
         print('</p>')
           
def update_code(file):
    file_data = ''
    #new_str = 'href="www.baidu.com"'
    with open(file, "r") as f:
        for line in f:
            if line.find("#{see rq")!=-1:
                id_name = re.findall(("rq"+r"\d"),line)
                if id_name[0] in line:
                    old_str = "href='srs.html#"+id_name[0]+"'"
                    # if not id_name[0] in srs:
                    #     line = line.replace(old_str,new_str)
            if line.find("#{see ra")!=-1:
                id_name = re.findall(("ra"+r"\d"),line)
                if id_name[0] in line:
                    old_str = "href='srs.html#"+id_name[0]+"'"
                    # if not id_name[0] in srs:
                    #     line = line.replace(old_str,new_str)
            if line.find("#{see tc")!=-1:
                id_name = re.findall(("tc"+r"\d"),line)
                if id_name[0] in line:
                    old_str = "href='srs.html#"+id_name[0]+"'"
                    # if not id_name[0] in srs:
                    #     line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w") as f:
        f.write(file_data)

print('</html></body>')
   