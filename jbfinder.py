import re 
import requests
from colorama import Fore, Style
import socket
urlpattern=re.compile(r'^(https?://)')

while True:
	breaker = False
	print("if you want to directory enumeration type(dir) or if you wnat to dns enumeration type (dns)")
	while not breaker == True:
			type = str(input("=>"))
			if type == "dir":
				break
			elif type == "dns":
				break
			else:
				print("!!!error on input!!!")
				print("pealse onlyh input 'dir' for directory enumeration and dns for dsn enumeration")
	if type == "dir":
		print("enter the url here")
		while True:
			url = str(input("=>"))
			if urlpattern.match(url):
				if url.endswith("/"):
					url = url[:-1]
				else:
					pass
				break
			else:
				print("does'nt match with url pattern")
		print("do you want client side esrror message like 404 if you want type 'yes' or if you don't want type 'no'")
		while True:
			wantclienterror = str(input("=>"))
			if wantclienterror.lower() == "yes":
				clienterror= True
				break
			elif wantclienterror.lower() == "no":
				 clienterror=False
				 break
			else :
				print("!!!error input!!!")
				print("type only 'yes' or 'no'")
				continue
		breaker = False
		while not breaker == True:
			print("enter the path of wordlist here")
			while True:
				path=input("=>")
				if path.endswith(".txt"):
					pass
				else:
					print("!!! input error !!!")
					print("verify the path you have  given is a txt wordlist")
				try:
					with open(path,'r') as p:
						for i in p:
							i = i.strip()
							respond = requests.get(url+str("/")+str(i))
							if int(respond.status_code) == 200:
								print(f"{Fore.GREEN}{respond.status_code}!! on => {url+str("/")+str(i)}{Style.RESET_ALL}")
							elif int(respond.status_code)>= 300 and int(respond.status_code) < 399:
								print(f"{Fore.BLUE}{respond.status_code} redirection on => {url+str("/")+str(i)}{Style.RESET_ALL}")
							elif int(respond.status_code) >= 400 and int(respond.status_code) < 499:
								if respond.status_code == 403:
									print(f"{Fore.MAGENTA}{respond.status_code} Forbidden on => {url+str("/")+str(i)}{Style.RESET_ALL}")
								elif clienterror == True:
									print(f"{Fore.YELLOW}{respond.status_code} client side error on => {url+str("/")+str(i)}{Style.RESET_ALL}")
								else:
									pass
							elif int(respond.status_code) >=500 and int(respond.status_code) < 599:
								print(f"{Fore.RED}{respond.status_code} server side error on => {url+str("/")+str(i)}{Style.RESET_ALL}")
							else:
								continue
					breaker = True
					break
				except:
					print("!!!STOPPING!!!")
					print("you can eneter new wordlist now or control c for exit")
				
	elif type == "dns":
		dbreaker = False
		while not dbreaker == True:

			dns = input("enter the dns here\n=>")
			print("enter the txt wordlist file path here")
			dnsbreaker = False
			while not dnsbreaker == True:
				wordlist=input("=>")
				try:
					with open(wordlist,'r') as words:
						for word in words:
							word = word.strip()
							if not word:
								continue
							else:
								try:
									print(f"{Fore.GREEN}host fount => {word}.{dns} dns lookup => {socket.gethostbyname(word + '.' + dns)}{Style.RESET_ALL}")
								except:
									print(f"{Fore.RED}not found => {word}.{dns}{Style.RESET_ALL}")
						dnsbreaker =True
						dbreaker
						break
				except:
					print("enter new wordlist or press control c for exit")
	else:
		pass
