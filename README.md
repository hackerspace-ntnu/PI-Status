# PI-Status
Keeps track of raspberry-Pies and their IP-adresses.
Used to display the current Ip-adress on a website using a .json file.
Currently the client does only work on linux machines due to the way the IP is retrieved.

#How to use
1. pip install rsa
2. run the keygenerator once, to create a new set of private and public keys
3. configure the adress.py so it contains your prefered port and the adress of your server.
4. move the client.py, adress.py and the public.txt to your raspberry-pi
5. configure your pi to run the client.py on startup, or run it in intervals of 10 minutes.
6. run your server.py
7. run client.py on your pi.
8. server should show that it recieved an update.
9. client should show that the update was recieved.
10. the client ip is now saved in a .json file

Works with multiple clients at once.
