from re import findall
from rubika import Bot
from requests import get
import requests
import time


bot = Bot("auth")
target = "g0BVzsB01fd8383fc2e2aff3e3353d6d"

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

# static variable
answered, sleeped, retries = [], False, {}

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

		open("id.txt","w").write(str(messages[-1].get("message_id")))

		for msg in messages:
			if msg["type"]=="Text" and not msg.get("message_id") in answered:
				if not sleeped:
					if hasInsult(msg.get("text"))[0] and not msg.get("author_object_guid") in admins :
						#ID = loads(c.decrypt(getUserInfo(msg.get("author_object_guid")).json().get("data_enc"))).get("data").get("user").get("username")
						#sendMessage(guid, f"#اخطار @{ID}", msg["message_id"])
						bot.deleteMessages(target, [str(msg.get("message_id"))])

					elif hasAds(msg.get("text")) and not msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [str(msg.get("message_id"))])

					elif "forwarded_from" in msg.keys() and bot.getMessagesInfo(target, [msg.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "!sleep" and msg.get("author_object_guid") in admins :
						sleeped = True
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "!del" and msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("reply_to_message_id")])
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("!ban") and msg.get("author_object_guid") in admins :
						try:
							guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
							if not guid in admins :
								bot.banGroupMember(target, guid)
								bot.sendMessage(target, "✅", message_id=msg.get("message_id"))
							else :
								bot.sendMessage(target, "❎", message_id=msg.get("message_id"))
								
						except IndexError:
							bot.banGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])
							bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("!send") :
						bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"], "شما یک پیام ناشناس دارید:\n"+" ".join(msg.get("text").split(" ")[2:]))
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "سلام" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "سلام عشقم چطوری ؟ ❤😍", message_id=msg.get("message_id"))

					elif msg.get("text") == "بیا بخورش" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "کونتو؟", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "اره" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "نگاییدم", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "نه" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "نکمه ، درد بگیری ایشالا", message_id=msg.get("message_id"))

					elif msg.get("text") == "خوبی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "فدات ط خوبی چخبرا ؟ 😊", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "سلامتی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "همیشه سلامت باشی گلم♥️", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ایول" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بنازم به ایول گفتنت😍", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "😡" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "ببخشید دیگه تکرار نمیشه جونم😖", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "چقدر منو دوست داری" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "خیلی دوست دارم انقد که گفتنی نیست😊❤️", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "استقلال" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "قسم به تیم استقلال ، قسم به سیمای خوبان ، قسم به ناصر حجازی ، ندای ما استقلال 💙", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "💙" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "قسم به تیم استقلال ، قسم به سیمای خوبان ، قسم به ناصر حجازی ، ندای ما استقلال 💙", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "پرسپولیس" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "پرسپولیس عشق آسیایی پرسپولیس خالق یک جامی گل بزن امشبو به یاد پروین و علی دایی ❤", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "❤" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "پرسپولیس عشق آسیایی پرسپولیس خالق یک جامی گل بزن امشبو به یاد پروین و علی دایی ❤", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "😎" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "هر کی با ما در افتاد ور افتاد 😎", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "😂" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "نخند عین جوکر میشی", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "😐" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "چیه بیا منو بخور", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "😂😂" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "نخند عین جوکر میشی", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "هعپ" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "آبی روشن عین من سیتی برف میاد سریع ترکیم هووو", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "رفیعی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "یک شاسگول به تمام معنا", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "آرش" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "رئیس جذابمه", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "چی بلدی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بطچ؟", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "چراغی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "دشمن سیب زمینی دست میکنه تو بینی در میاره شیرینی #شوخی 😂", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ارمیا" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "رئیسمه فداش بشم من", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "لینک" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "https://rubika.ir/joing/BIIDIJDG0YFBDNYODQGWDRSQPXYTGIMM", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "گوه نخور" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "شب میرینم صبح بخور", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ربات" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "عمت رباته بیشعور", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "خودتو معرفی کن" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "من ربات هستم که با هوش مصنوعی میتونم اینجا رو مدیریت کنم و باهاتون مثل یک انسان واقعی چت کنم", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ممنون" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "خواهش میکنم گلم💋😌", message_id=msg.get("message_id"))

					elif msg.get("text") == "لیست" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "لیست تبادلات فعال اکانت هوشمند : @ROld_Leader - https://rubika.ir/joinc/BCFFGFBF0QVAXVWXTWFMGMQVIXINYUGR - @ASYJXUK_GILOUNLkmgu - @tp__code ", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "تبادل" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "لیست تبادلات فعال اکانت هوشمند : @ROld_Leader - https://rubika.ir/joinc/BCFFGFBF0QVAXVWXTWFMGMQVIXINYUGR - @ASYJXUK_GILOUNLkmgu - @tp__code ", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "بای" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "کجا میری بودی حالا 😕", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "چه خبر" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "سلامتی خوبم میگذرونم دیگه", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "عشق" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "😊❤️", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "منم خوبم" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "خدا رو شکر 😘", message_id=msg.get("message_id"))

					elif msg.get("text") == "فدات" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "خدا نکنه قربونت 😁❤️", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "بی تر ادب" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "اره دا تو همینم نیستی 😏", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "هعی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "زر نزن باو", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "مرسی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "🥰", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "بمولا" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "اینا منو میخوان بمولا 🥲", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("!add") :
						bot.invite(target, [bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]])
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "!lock" :
						print(bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","AddMember"]).text)
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "!unlock" :
						bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","SendMessages","AddMember"])
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg["text"].startswith("!font"):
						response = get(f"https://api.codebazan.ir/font/?text={msg['text'].split()[1]}").json()
						#print("\n".join(list(response["result"].values())))
						try:
							bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:10])).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "متأسفانه نتیجه‌ای در بر نداشت ☹️", message_id=msg["message_id"])

					elif msg.get("text").startswith("!jok"):
						
						try:
							response = get("https://api.codebazan.ir/jok/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("!time"):
						
						try:
							response = get("https://api.codebazan.ir/time-date/?td=all").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])

				else:
					if msg.get("text") == "!wakeup" and msg.get("author_object_guid") in admins :
						sleeped = False
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

			elif msg["type"]=="Event" and not msg.get("message_id") in answered and not sleeped:
				name = bot.getGroupInfo(target)["data"]["group"]["group_title"]
				data = msg['event_data']
				if data["type"]=="RemoveGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"بای بای {user} 🗑️", message_id=msg["message_id"])
				
				elif data["type"]=="AddedGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"سلام {user} عزیز به گروه {name} خوش اومدی 😃\nلطفا قوانین رو رعایت کن 🥰", message_id=msg["message_id"])
				
				elif data["type"]=="LeaveGroup":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"بای بای {user} 🗑️", message_id=msg["message_id"])
					
				elif data["type"]=="JoinedGroupByLink":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"سلام {user} عزیز به گروه {name} خوش اومدی 😃\nلطفا قوانین رو رعایت کن 🥰", message_id=msg["message_id"])

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
