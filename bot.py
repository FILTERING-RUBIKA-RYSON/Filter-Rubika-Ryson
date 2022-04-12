from requests import get
from re import findall
from rubika.client import Bot
from rubika.tools import Tools
from rubika.encryption import encryption
import time
import datetime


bot = Bot(input("please enter your auth account rubika >_ "))
time.sleep(1)
print ("okay")
print ()
print ()
time.sleep(0.5)
target=input("please enter guid group rubika >_ ")

time.sleep(0.5)
print ()
print ()
print ("okay")


def hasInsult(msg):
	swData = [False,None]
	for i in open("dontReadMe.txt").read().split("\n"):
		if i in msg:
			swData = [True, i]
			break
		else: continue
	return swData

def hasAds(msg):
	links = list(map(lambda ID: ID.strip()[1:],findall("@[\w|_|\d]+", msg))) + list(map(lambda link:link.split("/")[-1],findall("rubika\.ir/\w+",msg)))
	joincORjoing = "joing" in msg or "joinc" in msg

	if joincORjoing: return joincORjoing
	else:
		for link in links:
			try:
				Type = bot.getInfoByUsername(link)["data"]["chat"]["abs_object"]["type"]
				if Type == "Channel":
					return True
			except KeyError: return False
			
answered = [bot.getGroupAdmins]
retries = {}
sleeped = False
# Creator = maxtor
plus= True

while True:
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]
		while True:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue
		
		open("id.db","w").write(str(messages[-1].get("message_id")))

		for msg in messages:
			if msg["type"]=="Text" and not msg.get("message_id") in answered:
				if not sleeped:
					if msg.get("text") == "آنلاینی" and msg.get("author_object_guid") in admins :
						bot.sendMessage(target, "im online", message_id=msg.get("message_id"))
						
					elif hasAds(msg.get("text")) and not msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif "forwarded_from" in msg.keys() and bot.getMessagesInfo(target, [msg.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [str(msg.get("message_id"))])

					elif msg.get("text").startswith("add") :
						bot.invite(target, [bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]])
						bot.sendMessage(target, "کاربر مورد نظر افزوده شد!", message_id=msg.get("message_id"))

					elif msg.get("text") == "دستورات":
						bot.sendMessage(target, "تست کن رفیق یاد میگیری !")
					elif msg.get("text").startswith("cal"):
						msd = msg.get("text")
						if plus == True:
							try:
								call = [msd.split(" ")[1], msd.split(" ")[2], msd.split(" ")[3]]
								if call[1] == "+":
									am = float(call[0]) + float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
									plus = False
							
								elif call[1] == "-":
									am = float(call[0]) - float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "*":
									am = float(call[0]) * float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "/":
									am = float(call[0]) / float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							except IndexError:
								bot.sendMessage(target, "دستور رو اشتباه وارد کردید رفیق" ,message_id=msg.get("message_id"))
						plus= True
					elif msg.get("text").startswith("send") :
						bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"], "شما یک پیام ناشناس دارید:\n"+" ".join(msg.get("text").split(" ")[2:]))
						bot.sendMessage(target, "okay buddy", message_id=msg.get("message_id"))

					elif msg.get("text") == "سلام":
						bot.sendMessage(target, "hi", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "خوبی":
						bot.sendMessage(target, "im good", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "چه خبر":
						bot.sendMessage(target, "salamati", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "چخبر":
						bot.sendMessage(target, "salamati", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "ربات":
						bot.sendMessage(target, "type for >", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "استغفرالله":
						bot.sendMessage(target, "yeah", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ممد":
						bot.sendMessage(target, "mmd ryson bozorg is offline", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "😂":
						bot.sendMessage(target, "خخ", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "😐":
						bot.sendMessage(target, "سطحت اینقدر پایینه که هنوز پوکر میدی بچه", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("گاییدم"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("نگاییدم"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("kir"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("کیر"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("کص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("کون"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("مادرت"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("مادرتو"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("کیرم"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("کوص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("کوس"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("کبص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("کوبص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("کسکش"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("بی ناموس"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("بیناموس"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("بی ناموص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("بیناموص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text") == "سنجاق" and msg.get("author_object_guid") in admins :
						    bot.pin(target, msg["reply_to_message_id"])
						    bot.sendMessage(target, "پیام مورد نظر با موفقیت سنجاق شد!", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "برداشتن سنجاق" and msg.get("author_object_guid") in admins :
						    bot.unpin(target, msg["reply_to_message_id"])
						    bot.sendMessage(target, "پیام مورد نظر از سنجاق برداشته شد!", message_id=msg.get("message_id"))

					elif msg.get("text") == "پایان" and msg.get("author_object_guid") in admins :
						sleeped = True
						bot.sendMessage(target, "ربات با موفقیت خاموش شد!", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("پینگ"):
						
						try:
							responser = get(f"https://api.codebazan.ir/ping/?url={msg.get('text').split()[1]}").text
							bot.sendMessage(target, responser,message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "please Enter correctly", message_id=msg["message_id"])

					elif msg.get("text").startswith("trans"):
						
						try:
							responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
							al = [responser["result"]]
							bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
							bot.sendMessage(target, "okay bro", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "not found", message_id=msg["message_id"])

					elif msg.get("text").startswith("فونت"):
						#print("\n".join(list(response["result"].values())))
						try:
							response = get(f"https://api.codebazan.ir/font/?text={msg.get('text').split()[1]}").json()
							bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:110])).text
							bot.sendMessage(target, "okay bro", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "not found my friend", message_id=msg["message_id"])



					elif msg.get("text").startswith("جوک"):
						
						try:
							response = get("https://api.codebazan.ir/jok/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "not found my friend", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("زمان"):
						
						try:
							response = get("https://api.codebazan.ir/time-date/?td=all").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "not found my friend", message_id=msg["message_id"])

					elif msg.get("text") == "ساعت":
						bot.sendMessage(target, f"Time : {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}", message_id=msg.get("message_id"))

					elif msg.get("text") == "تاریخ میلادی":
						bot.sendMessage(target, f"Date: {time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday}", message_id=msg.get("message_id"))

					elif msg.get("text") == "پاک" and msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("reply_to_message_id")])
						bot.sendMessage(target, "پیام مورد نظر پاک شد...", message_id=msg.get("message_id"))


					elif msg.get("text") == "بستن گروه" and msg.get("author_object_guid") in admins :
						print(bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","AddMember"]).text)
						bot.sendMessage(target, "گروه بسته شد!", message_id=msg.get("message_id"))

					elif msg.get("text") == "باز کردن گروه" and msg.get("author_object_guid") in admins :
						bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","SendMessages","AddMember"])
						bot.sendMessage(target, "گروه باز شد!", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("بن") and msg.get("author_object_guid") in admins :
						try:
							guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
							user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
							if not guid in admins :
								bot.banGroupMember(target, guid)
								bot.sendMessage(target, f"کاربر مورد نظر بن شد !", message_id=msg.get("message_id"))
							else :
								bot.sendMessage(target, f"خطا", message_id=msg.get("message_id"))
								
						except IndexError:
							a = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
							if a in admins:
								bot.sendMessage(target, f"خطا", message_id=msg.get("message_id"))
							else:
								bot.banGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])
								bot.sendMessage(target, f"کاربر مورد نظر بن شد !", message_id=msg.get("message_id"))

				else:
					if msg.get("text") == "شروع" and msg.get("author_object_guid") in admins :
						sleeped = False
						bot.sendMessage(target, "ربات شروع به فعالیت کرد!", message_id=msg.get("message_id"))

			elif msg["type"]=="Event" and not msg.get("message_id") in answered and not sleeped:
				name = bot.getGroupInfo(target)["data"]["group"]["group_title"]
				data = msg['event_data']
				if data["type"]=="RemoveGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"اگه قوانین رو رعایت میکردی حذف نمیشدی !", message_id=msg["message_id"])
				
				elif data["type"]=="AddedGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"hi {user} to group {name} welcome\nل This is where freedom comes first, buddy\n\nmy channel: @caetorr", message_id=msg["message_id"])
				
				elif data["type"]=="LeaveGroup":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"ok", message_id=msg["message_id"])
					
				elif data["type"]=="JoinedGroupByLink":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"hi {user} to group {name} welcome \n This is where freedom comes first, buddy\n\n my channel : @caetorr", message_id=msg["message_id"])

			answered.append(msg.get("message_id"))

	except KeyboardInterrupt:
		exit()

	except Exception as e:
		if type(e) in list(retries.keys()):
			if retries[type(e)] < 3:
				retries[type(e)] += 1
				continue
			else:
				retries.pop(type(e))
		else:
			retries[type(e)] = 1
			continue
