import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter , ImageGrab 
from sys import argv

for i in os.listdir(os.path.abspath(".")) :
	if (i[i.rfind(".")+1:] == "pimg") :
		os.system("expimg.exe "+i)
		for j in os.listdir(os.path.abspath(".")) :
			if (j[j.rfind(".")+1:] == "tlg") :
				os.system("tlg2png.exe "+j+" "+j[:j.rfind(".")] + ".png")
				os.remove(j)
		nm = i[:i.rfind(".")] + "+pimg+"
		rulen = nm + "layers.txt"
		with open(os.path.join(rulen)) as ru:
			rule = ru.read()
		p1=rule.find("width:        "+rule[14:18])-5
		base=rule[p1:p1+4].lstrip().rstrip("\n").rstrip("\r")
		b0=Image.open(nm+base+".png")
		ind=rule.find("layer_id:")
		while (ind>0) :
			cnm=rule[ind+14:rule.find("\n")].rstrip("\n").rstrip("\r")
			b2=Image.open(nm+cnm+".png")
			left=rule.find("left:",ind)+14
			top=rule.find("top:",ind)+14
			pos=(int(rule[left:rule.find("\n",left)]),int(rule[top:rule.find("\n",top)]))
			b1=Image.open(nm+base+".png")
			b1.paste(b2,pos,b2)
			b1.save(cnm+"done.png","png")
			ind=rule.find("layer_id:",ind+1)
