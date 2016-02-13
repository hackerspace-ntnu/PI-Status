import rsa

pubkey, privkey = rsa.newkeys(512,poolsize = 8)

pkey = privkey.save_pkcs1(format="PEM")
bkey = pubkey.save_pkcs1(format = "PEM")
fil = open("private.txt","wb")
fil.write(pkey)
fil.close()

fil = open("public.txt","wb")
fil.write(bkey)
fil.close()
#pubkey.save_pkcs1()

#READ
#fil = open("private.txt","rb")
#t = fil.read()
#fil.close()
#rsa.PrivateKey.load_pkcs1(t,'PEM')
