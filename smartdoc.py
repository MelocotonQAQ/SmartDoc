import sys,re

name_func =''
line_num = 0

dict_rq,dict_ra,dict_tc,dict_link,srs = {},{},{},{},{}	
def code_find_link(line,name,dict_name,srs_name):
		id_name = re.findall((name+r"\d"),line)
		if not id_name[0] in dict_name:
				dict_name[id_name[0]] = 1
		else:
				dict_name[id_name[0]] += 1
	
		num = dict_name[id_name[0]]
		while num>=1:
				name = id_name[0]+"_"+str(num)
				num-=1
				if not name in dict_link:
						dict_link[name]= ''
	
		if name_func!='':
				dict_link[name] = name_func+"_"+str(line_num)	
	
		id_whole = id_name[0]+"_"+str(dict_name[id_name[0]])
		link = gen_srs_html+"#"+id_name[0]
	
		line=re.sub("#{see "+id_name[0]+"}","<a href='"+link+"' id='"+id_whole+"'>"+"#{see "+id_name[0]+"}"+"</a>",line)
		return line
	
	
def write_code_content(line):
		global name_func,line_num
		if name_func!='':
				line_num+=1
	
		if line.find("def")!=-1:
			name_func = re.findall(".*def(.*):.*",line)[0]
			
			for key in dict_link:
					if dict_link[key]=='':
							dict_link[key]=name_func+"_"+str(line_num)	
		if line.find("return")!=-1:
				name_func=''
				line_num = 0
	
		if line.find("#{see rq")!=-1:
				line = code_find_link(line,'rq',dict_rq,srs)
	

		if line.find("#{see ra")!=-1:
				line = code_find_link(line,'ra',dict_ra,srs)
	

		if line.find("#{see tc")!=-1:
				line = code_find_link(line,'tc',dict_tc,srs)
	
		return line	
	

def srs_part(line,name,dict_name,srs_name):
		id_name = re.findall((name+r"\d"),line)
		srs[id_name[0]]=''
		link = gen_code_html+"#"+id_name[0]
		
		select = """<form action="" method="get" style="margin:0px;"><select name="jump" id="jumo" onchange="MM_jump('window',this)"><option value="srs.html">choose</option>"""
		i = 1
		if not id_name[0] in dict_name:
				dict_name[id_name[0]]=0
		while (i <= dict_name[id_name[0]] ):
				link = gen_code_html+"#"+id_name[0]+"_"+(str(i))
				name = id_name[0]+"_"+(str(i))
				select += '<option value="'+link+'">'+dict_link[name]+'</option>'
				i+=1
		select += '</select></form>'
		line +=select
		return line

def write_srs_content(line):
		if line.find("[id=rq")!=-1:
				line = srs_part(line,'rq',dict_rq,srs)
	
		elif line.find("[id=ra")!=-1:
				line = srs_part(line,'ra',dict_ra,srs)
	
		elif line.find("[id=tc")!=-1:
				line = srs_part(line,'tc',dict_tc,srs)
	
		elif line.find("Priority")!=-1:
				line = line.replace("Priority","Priority")
		return line
	

def write_code_html(txt,html,gen_code_html):
		write_head(html,'code')
		write_css(html)
		content = '<pre style="word-wrap: break-word; white-space: pre-wrap;">'
		html.write(content)
		for line in txt.readlines():
				link = write_code_content(line)
				html.write(link)
				link =''
		html.write("</pre>")
		write_foot(html)
		txt.close()
		html.close()	

	
def write_srs_html(txt,html,gen_srs_html):
		write_head(html,'srs')
		write_function(html)
		write_css(html)
		content = '<pre style="word-wrap: break-word; white-space: pre-wrap;">'
		html.write(content)
		for line in txt.readlines():
				link = write_srs_content(line)
				html.write(link)
				link =''
		html.write("</pre>")
		write_foot(html)
		txt.close()
		html.close()

def write_head(html,title):
		head = """
		<html>
		<head><title>"""+title+"""</title>
		"""
		html.write(head)
	
def write_function(html):
		function_jump = """
		<script type="text/javascript">
		function MM_jump(targ,selObj) {
		eval(targ+".location='"+selObj.options[selObj.selectedIndex].value+"'");
		}
		</script>
		"""
		html.write(function_jump)
	
def write_css(html):
		css = """
		<style>
		a:link {background-color:#FFFF00;} 
		a:visited {background-color:#FF0000;}
		a:hover {background-color:#FF704D;}
		a:active {background-color:#FF704D;}
		</style>
		</head>
		<body>
		"""
		html.write(css)

def write_foot(html):
		foot = """
		</body>
		</html>
		"""
		html.write(foot)

file_srs_addr = sys.argv[1]
file_code_addr= sys.argv[2]
gen_srs_html = "srs.html"
gen_code_html = "code.html"

f_code_txt = open(file_code_addr,'r')
f_srs_txt = open(file_srs_addr,'r')
f_code_html = open(gen_code_html,'w')
f_srs_html = open(gen_srs_html,'w')

if __name__ == '__main__':
		write_code_html(f_code_txt,f_code_html,gen_code_html)
		write_srs_html(f_srs_txt,f_srs_html,gen_srs_html)

