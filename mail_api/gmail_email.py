import imaplib
from email.parser import HeaderParser
import email
from time import sleep
import RPi.GPIO as GPIO
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib

eml='your_email@gmail.com'
pssw='your_password'

target='from@email.com'

l_s=''

def login():
	global l_s
	try:
		l_s= imaplib.IMAP4_SSL("imap.gmail.com",993)
		l_s.login(eml,pssw)
		print "Login"
	except Exception as s:
		print "Login_error"
		print s
		
def check_mail():
	global l_s
	a,b=l_s.select('INBOX')
	dataa=[]
	try:
		typ, dataa = l_s.uid('search','(FROM '+target+')','UNSEEN')
	except Exception as s:
		print s
	data=dataa[0].split(' ')
	if data != [''] and len(data)>0:
		for x in range(0,len(data)):
			typ,mail= l_s.uid('fetch', data[x], '(RFC822)')
			parser = HeaderParser()
			h = parser.parsestr(mail[0][1])
			r_string=mail[0][1].decode('utf-8')
			e_msg=email.message_from_string(r_string)
			for part in e_msg.walk():
				if part.get_content_type()=='text/plain':
					body=part.get_payload(decode=True)
					body=body.split('--')[0].replace('\r','').replace(' ','').replace('\t','')
					print "Message: ",body
					for scm in body.lower().replace('\r','').split('\n'):
						dev,mode,val=wwe(scm.replace(' ','').replace('\t',''))
						if str(val)=='0' or str(val)=='1':
							dev_rply(h['Subject'],h['Message-ID'],str(dev),str(val))
						sleep(0.5)
				#print str(j)+" : "+str(h[j]) 
				

def wwe(ss):
	try:
		if "read:" in ss:
			mode='in'
			dev=ss.split('read:')[1]
			val='q'
		else:
			mode='out'
			if 'on' in ss:
				val='on'
				dev=ss.split('gpio:')[1].split(':on')[0]
			else:
				val='off'
				dev=ss.split('gpio:')[1].split(':off')[0]
	
		if dev in('17','18','27','22','23','24','25','5','6','13','19','26','21','20','16','12'):
			if mode=='out':
				GPIO.setup(int(dev),GPIO.OUT)
				if val=='on':
					GPIO.output(int(dev),GPIO.HIGH)
					return(str(dev),'OUTPUT','OK')
				else:
					GPIO.output(int(dev),GPIO.LOW)
					return(str(dev),'OUTPUT','OK')
			elif mode=='in':
				GPIO.setup(int(dev),GPIO.IN)
				if val=='q':
					return(str(dev),'INPUT',str(GPIO.input(int(dev))))
				else:
					return(str(dev),'ERROR','Error')
	except:
		return('Error',"Error",'Error')				


def dev_rply(subject,msg_id,device,sts):
	msg = MIMEMultipart('alternative')
	msg['To'] =str(target)
	msg['From']=str(eml)
	msg['Subject']='Re: '+str(subject)
	msg['In-Reply-To']=str(msg_id)
	msg['References']=str(msg_id)
	if sts=='0':
		text="GPIO "+device+" is LOW"
	else:
		text="GPIO "+device+" is High"
	part1=MIMEText(str(text), 'plain')
	msg.attach(part1)
	try:
		server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
		#server_ssl.ehlo() # optional, called by login()
		server_ssl.login(eml,pssw)  
		server_ssl.sendmail(eml,target, msg.as_string())
		server_ssl.quit()
	except:
		print "Msg Not Sent"
		
def loop():
	global l_s
	GPIO.setmode(GPIO.BCM)
	login()
	try:
		while True:
			check_mail()
			sleep(10)
	except:
		print "Process Fail"
		
try:
	loop()
except:
	GPIO.cleanup()
