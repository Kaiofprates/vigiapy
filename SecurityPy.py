import pyautogui,time,os
#from twilio.rest import Client
from datetime import datetime
from pygame import mixer
from time import strftime
from cam import capcam
import subprocess as sp


#os.system('color 5f')
mixer.init()
mixer.music.load('alarm.mp3')

sirene = lambda: mixer.music.play()

data = str(datetime.now())

global a 

"""def msn():
	account_sid = "ACef0d9f6b1bd4bf9ef66cb9edc08e9204"
	auth_token  = "2aa3ac696c81fd99ed0b3af1ee46de29"
	client = Client(account_sid, auth_token)
	text = str('Evento inesperado em {}'.format(data))
	message = client.messages.create(to="+5538992506946",
		from_="+15104910320",
		body = text)"""
celip = "192.168.0.100"
def rot():
	#print(strftime('%H:%M:%S'))
	temp = str(strftime('%H:%M:%S'))
	print("\x1b[36m{:=^80}\x1b[0m".format(temp))
	time.sleep(1)
	os.system('clear')


def move():
	a ,b = pyautogui.position()
	x = a 
	while a == x:
		#time.sleep(1)
		rot()
		print('\x1b[36m{:=^80}\x1b[0m'.format('MONITORANDO SUA RESIDÊNCIA'))
		ipt,res = sp.getstatusoutput('ping -w 3 '+celip)
		print(' \x1b[35m\t\t\t\tresposta do ip\x1b[34m\n{:=^80}\x1b[0m'.format(ipt))
		if ipt == 0:
			secur()
		a,b = pyautogui.position()
	
	capcam()
	sirene()
	#msn()

def secur():
	while True:
		print("\x1b[31m{:=^80}\x1b[0m".format('AGUARDANDO ACIONAMENTO'))
		ipt,res = sp.getstatusoutput('ping -w 3 '+celip)
		print(' \x1b[35m\t\t\t\tresposta do ip\x1b[32m\n{:=^80}\x1b[0m'.format(ipt))
		if ipt == 1:
			move()
		else:
			time.sleep(1)
			os.system('clear')
secur()
move()

