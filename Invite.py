import aminofix 
import concurrent.futures
import os
import pyfiglet
from colorama import init, Fore, Back, Style
print("\t\033[1;32m CHATINVITE/ \033[1;36mBOT  \n\n")
init()
print(Fore. BLUE + Style.BRIGHT)
print(pyfiglet.figlet_format("Victorayush", font="cyberlarge"))
print(pyfiglet.figlet_format("Doctor", font="cyberlarge"))
print("""
.,  
                                                 ^
                                                ,.
              
__________(█)Dr
_______██████Victor
_____ ████████ayush
___███████████tripathi
___ (░░░░░░░)░░░)Ravi
___(░(░█░░█░)░░░)Alexa
__ (░░(░░●░░░)░░░)Techvision
__ (░░░░◡░░)░░░░)Follow
_██(░░░░░░░░░░)██Youtube
_███(░░░░░░░░░)███Techvision
████ ██(░░░)██ ████enjoy
████ █████████ ███script
████ ████░████ ███amino
(░░)_ ▓▓▓▓▌▓▐▓▓▓_(░░)
(██) ███████████ (██)
_____█████░█████_▓▓▓)
_____█████-,█████▓▓▓▓▓)
_____█████-,█████▓▓▓▓▓)
___(░░░░░░)(░░░░░) ▓▓▓▓)
______(███)_(███)▓▓▓▓▓▓)
____ (████)_(████)▓▓▓▓▓)  
                
                  (,(,(,_)   Community Name Techvison Alexa 4.0   (,(,(,_)
    \n\t\t{}    Instagram  _victor_ayush_
      """)
      
print("""

      
The cat is sad coz it’s not getting likes
　　　　　／＞　　フ
　　　　　| 　_　 _ l
　 　　　／` ミ＿xノ
　　 　 /　　　 　 |
　　　 /　 ヽ　　 ﾉ
　 　 │　　| | | 
╭━━━━━╮
┃ 𝙈𝙀𝙊𝙒 ┃
╰━┳━━━╯Owner Ravi Levi, Victor Ayush Tripathi (FutureDoctor)
  ┃Telegram Techvision_victor_ravi
  ◣  ◢                       ◢◤
  ▉▉▉                  ◢◤
  ▉▉▉▃▃▃▃▃▃▉
   ◥▉▉▉▉▉▉▉▉
     ▉▉▉▉▉▉▉▉
     ▋  ▋    ▋  ▋
     ▋  ▋    ▋  ▋
     ▋  ▋    ▋  ▋ 
            
                  
                        
                              """)     
client = aminofix.Client("42CA80011C37D4A8D7DC42AD6335BFB310F705C8F15F8F7E9C7C6905741F2512B10BE7AECCF3279DE7")
email = input("Email: ")
password = input("Password: ")
client.login(email=email, password=password)
clients = client.sub_clients(size=100)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
communityid = clients.comId[int(input("Select the community: "))-1]
SUB =aminofix.SubClient(comId=communityid, profile=client.profile)
chats = SUB.get_chat_threads(size=150)
for z, title in enumerate(chats.title, 1):
	print(f"{z}.{title}")
chatx = chats.chatId[int(input("Select the chat: "))-1]


def inviteonlineusers():
	with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
		for i in range(0, 20000, 250):
			onlineusers = SUB.get_online_users(start=i, size=5000).profile.userId
			if onlineusers:
				for userId in onlineusers:
					print(f"{userId} Invited/.....")
					_ = [executor.submit(SUB.invite_to_chat, userId,chatx)]
			else:
				break
		for i in range(0, 20000, 250):
			publichats = SUB.get_public_chat_threads(type="recommended", start=i, size=5000).chatId
			chatsuin = SUB.get_chat_threads(start=i, size=100).chatId
			chats = [*publichats, *chatsuin]
			if chats:
				for chatid in chats:
					for u in range(0, 1000, 50):
						users = SUB.get_chat_users(chatId=chatid, start=u, size=100).userId
						if users:
							for userId in users:
								try:
									print(f"{userId} Invited/....")
									_ = [executor.submit(SUB.invite_to_chat, userId,chatx)]
								except:
									pass
						else:
							break
							print("Invited All Online Users")
def inviteuserfollowers():
	userlink=input("Type user link: ")
	user=client.get_from_code(userlink)
	userx=user.objectId
	with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
		for i in range(0, 20000, 250):
			followers = SUB.get_user_followers(userId=userx, start=i, size=100).profile.userId
			if followers:
				for userId in followers:
					try:
						print(f"{userId} Invited/....")
						_ = [executor.submit(SUB.invite_to_chat, userId, chatx)]
					except:
						pass
			else:
				break
				print("Invited User Followers/....")

def inviterecentusers():
	with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
		for i in range(0, 20000, 250):
			recentusers = SUB.get_all_users(type="recent", start=i, size=100).profile.userId
			users = [*recentusers]
			if users:
				for userId in users:
					print(f"{userId} Invited/.....")
					_ = [executor.submit(SUB.invite_to_chat, userId, chatx)]
			else:
				break
				print("Invited Recent & Banned Users")

def inviteallusers():
	with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
		for i in range(0, 20000, 250):
			onlineusers = SUB.get_online_users(start=i, size=100).profile.userId
			recentusers = SUB.get_all_users(type="recent", start=i, size=100).profile.userId
			curators = SUB.get_all_users(type="curators", start=i, size=100).profile.userId
			leaders = SUB.get_all_users(type="leaders", start=i, size=100).profile.userId
			users = [*onlineusers, *recentusers, *curators, *leaders]
			if users:
				for userId in users:
					print(f"{userId} Invited/....")
					_ = [executor.submit(SUB.invite_to_chat, userId, chatx)]
			else:
				break
		for i in range(0, 20000, 250):
			publichats = SUB.get_public_chat_threads(type="recommended", start=i, size=100).chatId
			chatsuin = SUB.get_chat_threads(start=i, size=100).chatId
			chats = [*publichats, *chatsuin]
			if chats:
				for chatid in chats:
					for u in range(0, 1000, 50):
						users = SUB.get_chat_users(chatId=chatid, start=u, size=100).userId
						if users:
							for userId in users:
								try:
									print(f"{userId} Invited/....")
									_ = [executor.submit(SUB.invite_to_chat, userId, chatx)]
								except:
									pass
						else:
							break
							print("Invited All Online Users:")

print("    1.Invite Online Users:")
print("    2.Invite User Followers:")
print("    3.Invite Recent Users:")
print("    4.Invite All Users:")
inviteselect = input("Type Number: ")
if inviteselect == "1":
	inviteonlineusers()

elif inviteselect == "2":
	inviteuserfollowers()

elif inviteselect == "3":
	inviterecentusers()

elif inviteselect == "4":
	inviteallusers()