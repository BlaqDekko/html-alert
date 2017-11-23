from lxml import html
from slacker import Slacker
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
import logging

log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)  # DEBUG

fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)

def routine():
    page = requests.get('http://steamcommunity.com/id/rrapetor')
    #page = requests.get('http://steamcommunity.com/id/BlaqDekko')
    tree = html.fromstring(page.content)
    status = str(tree.xpath('/html/body/div[1]/div[7]/div[2]/div/div[2]/\
    div/div[1]/div[1]/div/div[1]/text()'))
    if "Offline" in status:
        print('Not Online')
    else:
        slack = Slacker('xoxp-273626192374-272795003300-273453876133-e9eee4f6111fdcc1fc1ea1258fe99301')
        slack.chat.post_message('#luke_thomas_detector', 'Luke is Online!')
        print status
        scheduler.remove_job('routine')
        scheduler.add_job(routine2, 'interval', hours=2, id='routine2')
        #scheduler.add_job(routine2, 'interval', seconds=15, id='routine2')

def routine2():
	page = requests.get('http://steamcommunity.com/id/rrapetor')
	#page = requests.get('http://steamcommunity.com/id/BlaqDekko')
	tree = html.fromstring(page.content)
	status = str(tree.xpath('/html/body/div[1]/div[7]/div[2]/div/div[2]/\
	div/div[1]/div[1]/div/div[1]/text()'))
	if "Offline" in status:
		print status
		scheduler.remove_job('routine2')
		#scheduler.add_job(routine, 'interval', seconds=5, id='routine')
		scheduler.add_job(routine, 'interval', minutes=45, id='routine')
	else:
		print('Still Online')

scheduler = BlockingScheduler()
scheduler.add_job(routine, 'interval', minutes=45, id='routine')
#scheduler.add_job(routine, 'interval', seconds=5, id='routine')

print ('Starting Scheduler')

scheduler.start()



#Options are "[Currently Offline]," "[Currently Online]," and "[Currently In-Game]."
