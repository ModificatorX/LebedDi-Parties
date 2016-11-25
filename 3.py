from datetime import datetime, date, time
import requests
r = requests.get('https://api.meetup.com/2/open_events?&sign=true&photo-host=public&lat=34&topic=softwaredev&lon=-118&radius=20&page=20&key=2f5e1d6512231504721f4a535f955')
res = r.json()
file = open("parties.html", "w+", encoding='utf-8')
j=0
file.write("<!DOCTYPE HTML><html><head><style>body{background:grey;}a:visited{color: blue;}div{font-family:Arial;border:solid;border-radius:10px;background:white;margin-bottom:10px;box-shadow: 0 0 20px rgba(0,0,0,0.5);}header{margin:-20px;vertical-align:middle;text-align:center;font-size:150%;color:red;}</style></head><body><header><h1>There is a list of occasions for a week</h1></header>")
while j<7:
	if 	j==0:
		file.write("<h1 align='center'>Monday</h1>")
	elif j==1:
		file.write("<h1 align='center'>Tuesday</h1>")
	elif j==2:
		file.write("<h1 align='center'>Wednsday</h1>")
	elif j==3:
		file.write("<h1 align='center'>Thursday</h1>")
	elif j==4:
		file.write("<h1 align='center'>Friday</h1>")
	elif j==5:
		file.write("<h1 align='center'>Saturday</h1>")
	elif j==6:
		file.write("<h1 align='center'>Sunday</h1>")
	for item in res['results']:
		dt=datetime.fromtimestamp(int(item['time'])/1000).weekday()
		if dt == j:
			file.write("<div>")
			file.write("<p>")
			
			file.write("<b>Time: </b>" + str(datetime.fromtimestamp(int(item['time'])/1000))+"\n")
			
			file.write("</p>")
			file.write("<p>")
			
			file.write("<b>Name of Occasion: </b>" + str((item['group'])['name'])+"\n")
			
			file.write("</p>")
			file.write("<p>")
			
			file.write("<b>Organizator: </b>" + str((item['group'])['who'])+"\n")
			
			file.write("</p>")
			file.write("<p>")
			
			file.write("<b>Description: </b>")
			
			file.write("</p>")
			file.write("<p>")
			
			file.write(str(item['description']))
			
			file.write("</p>")
			
			file.write("<b>Location</b> : " + str(item['name']))
			
			file.write("</p>")
			file.write("</div>")
	j+=1
file.write("</body></html>")
file.close
