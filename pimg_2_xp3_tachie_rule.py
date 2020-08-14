import os

for i in os.listdir(os.path.abspath(".")) :
	if (i[i.rfind(".")+1:] == "txt") :
		with open(os.path.join(i)) as ru:
			rule = ru.read()
		out = open(i[:i.rfind("+")]+".txt","w")
		out.write("#layer_type	name	left	top	width	height	type	opacity	visible	layer_id	group_layer_id			\n\n")
		pos=rule.find("name:")
		while(pos>0):
			name=rule[pos+12:rule.find("\n",pos+1)].lstrip()
			pos=rule.find("layer_id:",pos)
			layerid=rule[pos+12:rule.find("\n",pos+1)].lstrip()
			pos=rule.find("width:",pos)
			width=rule[pos+12:rule.find("\n",pos+1)].lstrip()
			pos=rule.find("height:",pos)
			height=rule[pos+12:rule.find("\n",pos+1)].lstrip()
			pos=rule.find("left:",pos)
			left=rule[pos+12:rule.find("\n",pos+1)].lstrip()
			pos=rule.find("top:",pos)
			top=rule[pos+12:rule.find("\n",pos+1)].lstrip()
			pos=rule.find("opacity:",pos)
			opacity=rule[pos+12:rule.find("\n",pos+1)].lstrip()
			pos=rule.find("layer_type:",pos)
			layertype=rule[pos+12:rule.find("\n",pos+1)].lstrip()
			pos=rule.find("type:",pos+12)
			type=rule[pos+12:rule.find("\n",pos+1)].lstrip()
			pos=rule.find("visible:",pos)
			visible=rule[pos+12:rule.find("\n",pos+1)].lstrip()
			out.write(layertype+"	"+name+"	"+left+"	"+top+"	"+width+"	"+height+"	"+type+"	"+opacity+"	"+visible+"	"+layerid+"	0			\n")
			pos=rule.find("name:",pos)
		out.close()
