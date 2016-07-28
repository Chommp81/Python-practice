import urllib #for opening URL
import smtplib #for sending email
from bs4 import BeautifulSoup #for parsing HTML
import sys #needed to pass arguments in the command line
from datetime import datetime #for logging rate and date/time
import secrets #contains FROM email credentials

#this program asks for two currencies, then scrapes the appropriate Bloomberg page
#for the up to date exchange rate, and then returns it.
#If the rate is above the 'cutoff' rate, then the program will send an email to 
#wilson.palooza@gmail.com to alert them to the good rate.


def buildUrl(cur1,cur2):
	return "http://www.bloomberg.com/quote/" + cur1 + cur2 + ":CUR"

def getRate(url):
	uh = urllib.urlopen(url).read()
	soup = BeautifulSoup(uh, 'html.parser')

	rate = soup.find('div', class_='price').get_text()
	print "1", cur1, "buys", rate, cur2
	
	cutoff = 0.75 #this sets the rate above which we want to receive an alert

	#if the rate is AUDUSD and is more than the cutoff, then send an email.
	if float(rate) > cutoff and cur1=="AUD" and cur2=="USD":
		sendEmail(cur1,cur2,rate)
		print "Rate is higher than %s. Alert email sent!" % (cutoff)
	else:
		print "No email sent."

	logRate(cur1, cur2,rate) 

def logRate(cur1, cur2, rate):
	fhand = open('rate_log.txt','a')
	msg = '\n' + str(datetime.now()) + '\t' + "1 %s buys %s %s" % (cur1, rate, cur2)
	fhand.write(msg)
	fhand.close()
	print "Rate has been logged to rate_log.txt"
	
def sendEmail(cur1,cur2,rate):
	#create SMTP object with hostname and port number
	server = smtplib.SMTP('smtp.gmail.com', 587)

	#set up the proper connection for sending mail
	server.starttls()

	#log in to server
	server.login(secrets.username, secrets.password)

	#create the message
	msg = '''\n
	Luke! 
	The rate is above the cutoff! 
	The current rate is %s 
	1 %s buys %s %s 
	''' % (rate, cur1, rate, cur2)
	
	#send the message
	server.sendmail(secrets.fromAddress,secrets.toAddress,msg)
	server.quit()

def chooseCurrencies():
	global cur1
	while True:
		cur1 = raw_input("Choose currency one: ")
		cur1 = cur1.upper()
		if len(cur1) == 3: break
		print "Sorry. You need to choose the three letter code e.g. AUD. Try again."
			
	global cur2
	while True:
		cur2 = raw_input("Choose currency two: ")
		cur2 = cur2.upper()
		if len(cur2) == 3: break
		print "Sorry. You need to choose the three letter code e.g. AUD. Try again."

	url = buildUrl(cur1,cur2)

	print '\nChecking', url, '\n'
	getRate(url)


#this section checks if any arguments were passed at the command line.
###
#If there were 2 arguments, then get the rate.
#If there weren't 2 arguments, then just ask for the two currencies
if len(sys.argv) == 3:
	cur1 = sys.argv[1].upper()
	cur2 = sys.argv[2].upper()
	url = buildUrl(cur1, cur2)
	try:
		getRate(url)
	except AttributeError:
		chooseCurrencies()
else:
	chooseCurrencies()










