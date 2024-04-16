# RaspberryPiCatCam

I’ve created a cat cam using a raspberry pi4. This cat cam allows a remote user to view cat's with a click of a button. There is a button that will allow user to activate the motor to feed the cats

# Hardware
- camera from Dorothea that has a resolution of 1080p.
- The motor sg90 servo motor with 180 degree capability.
- The model is 3-D printed.
- raspebrry pi4
- STL to design 3-D model 

# Languages
- The server runs off of a flask app written in python
- User interface: html and JavaScript.
- The display is formatted with css and bootstrap.
- There is an additional server used to display the camera used from open source: https://picamera.readthedocs.io/en/release-1.13/recipes2.html then rendered by davidplowman and chrisruk on picamera2/examples/mpjeg_server.py 
