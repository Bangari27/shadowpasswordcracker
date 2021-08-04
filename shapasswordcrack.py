# Once you have the shadow password file then look into and the file has so many password but it is encrypted.
# Usually (salt) will be the start with $ and end with $( Note : inbetween $ can be contain ignore it)
# Rohith Bangari 
# 25-07-2021
import crypt
def shadowpass(cryptPass):
	s = cryptPass[0:30] # stripping out salt from the encrypted password
	#salt = cryptPass.split('$')[0:4].strip('')
	print("salt char :" +s)
	sha = cryptPass[30:] # Remaining will be password
	#sha = cryptPass.split('$')[4].split(' ')
	print("Shadow file password :" +sha)
	dict=open('dictionary.txt','r')  # Dictionary contain password
# we will look into each word of the dictinary and  encrypted with salt using crypt function library and comapre with the encrypted password 
	for word in dict.readlines():
		word=word.strip('\n')
		cryptWord = crypt.crypt(word,s)
		if(cryptWord == cryptPass):
			print("Found Password:"+word+"\n")
			return
	print("Password not found\n")
	return
def main():
	pasfile = open('shapass.txt')
	for line in pasfile.readlines():
		if ":" in line:
		  user = line.split(':')[0]  # Split  username ans password
		  encryptPass=line.split(':')[1].strip(' ')
		  print("Cracking Password for:", user)
		  print("Encrypted  password",encryptPass)
		  shadowpass(encryptPass)
main()
