# PI-Status
Keeps track of raspberry-Pies and their IP-adresses. Used to display the current Ip-adress on a website using a .json file.

#How to use
1. pip install rsa
2. run the keygenerator once, to create a new set of private and public keys
3. move the client.py and the public.txt to your raspberry-pi
4. configure the client.py file so it connects to your servers ip.
5. configure your pi to run the client.py on startup, or run it in intervals of 10 minutes.
6. run your server.py
7. run client.py on your pi.
8. server should show that it recieved an update.
9. client should show that the update was recieved.
10. the client ip is now saved in a .json file

Works with multiple clients at once.
