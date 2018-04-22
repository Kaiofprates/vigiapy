#coding: utf-8
import smtplib, cv2
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText
#from email.mime.image import MIMEImage

def capcam():
	camera_port = 0  
	nFrames = 30
	camera = cv2.VideoCapture(camera_port)
	file = "imagen.png"
	retval, img = camera.read()
	cv2.imshow('Foto',img)
	cv2.imwrite(file,img)
	cv2.destroyAllWindows()
	camera.release()

"""server = smtplib.SMTP('smtp.gmail.com:587')
				server.starttls()
				server.login("email","senha")
			
				to_addr = "email"
				subject = 'SECURIT CAM EVENT'
				body = 'Essa pessoa invadiu sua residência'
			
				msg = MIMEMultipart()
				msg["From"] = "email"
				msg["To"] = to_addr
				msg["Subject"] = subject
			
				imgFilename = 'capture.png' 
				with open('imagen.png', 'rb') as f:
				    msgImg = MIMEImage(f.read(), name=imgFilename)
				msg.attach(msgImg)
			
				msgText = MIMEText('<b>{}</b><br><img src="cid:{}"><br>'.format(body, imgFilename), 'html')
				msg.attach(msgText)
				server.sendmail("deltreesociety@gmail.com", to_addr, msg.as_string())
				server.quit()"""
