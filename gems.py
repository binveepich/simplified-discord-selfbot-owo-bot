from data import data
from time import sleep, time
from color import color
from menu import UI
from re import findall, sub
client = data()
ui= UI()
class gems:
	def __init__(self, bot, start_time):
		self.last_inv = 0
		self.last_use = 0
		self.inv_cooldown = 15   
		self.use_cooldown = 10   
		self.last_used_gems = []
		self.bot = bot
		self.start_time = start_time
		self.available = [1, 3, 4, 5]
		self.gemtypes = [1, 3, 4, 5]
		self.regex = r"gem(\d):\d+>`\[(\d+)"
	def at(self):
		elapsed = int(time() - self.start_time)
		h = elapsed // 3600
		m = (elapsed % 3600) // 60
		s = elapsed % 60
		return f'\033[0;43m{h:02}:{m:02}:{s:02}\033[0;21m'
	def useGems(self, gemslist=[1,3,4,5]):
		if time() - self.last_inv < self.inv_cooldown:
			return
		self.last_inv = time()
		def switchCode(code):
			for i in code:
				if i == 1:
					code[code.index(i)] = 0
				elif i == 3:
					code[code.index(i)] = 1
				elif i == 4:
					code[code.index(i)] = 2
				elif i == 5:
					code[code.index(i)] = 3
		switchCode(gemslist)
		self.bot.typingAction(str(client.channel))
		sleep(3)
		self.bot.sendMessage(str(client.channel), "owo inv")
		ui.slowPrinting(f"{self.at()}{color.okgreen} [SENT] {color.reset} owo inv")
		client.totalcmd += 1
		sleep(2)
		msgs=self.bot.getMessages(str(client.channel), num=10)
		msgs=msgs.json()
		inv = None
		for i in range(len(msgs)):
			if msgs[i]['author']['id'] == client.OwOID and 'Inventory' in msgs[i]['content']:
				inv=findall(r'`(.*?)`', msgs[i]['content'])
		if not inv:
			sleep(3)
			client.totalcmd -= 1
			return
		else:
			self.available = []
			if '050' in inv:
				self.bot.sendMessage(str(client.channel), "owo lb all")
				ui.slowPrinting(f"{self.at()}{color.okgreen} [SENT] {color.reset} owo lb all")
				sleep(5)
				self.available = list(self.gemtypes)
				return
			if '049' in inv:
				self.bot.sendMessage(str(client.channel), "owo lb f all")
				ui.slowPrinting(f"{self.at()}{color.okgreen} [SENT] {color.reset} owo lb f all")
				sleep(5)
				self.available = list(self.gemtypes)
				return
			if '100' in inv:
				self.bot.sendMessage(str(client.channel), "owo crate all")
				ui.slowPrinting(f"{self.at()}{color.okgreen} [SENT] {color.reset} owo crate all")
				sleep(5)
			if '028' in inv:
				sleep(3)
				self.bot.sendMessage(str(client.channel), "owo use 28")
				ui.slowPrinting(f"{self.at()}{color.okgreen} [SENT] {color.reset} owo use 28")
				self.available = list(self.gemtypes)
				return
			inv = [item for item in inv if item.isdigit() and int(item) < 100 and int(item) > 50]
			tier = [[],[],[],[]]
			ui.slowPrinting(f"{self.at()}{color.okblue} [INFO] {color.reset} Found {len(inv)} Gems Inventory")
			for gem in inv:
				gem = int(gem)
				if 50 < gem < 58:
					tier[0].append(gem)
				elif 64 < gem < 72:
					tier[1].append(gem)
				elif 71 < gem < 79:
					tier[2].append(gem)
				elif 78 < gem < 86:
					tier[3].append(gem)
			if tier[0]:
				self.available.append(1)
			if tier[1]:
				self.available.append(3)
			if tier[2]:
				self.available.append(4)
			if tier[3]:
				self.available.append(5)
			use = []
			for level in gemslist:
					if not len(tier[level]) == 0:
						use.append(str(max(tier[level])))
			if use:
				if time() - self.last_use < self.use_cooldown:
					return

				# tránh dùng lại gem cũ
				if use == self.last_used_gems:
					return

				self.last_used_gems = use.copy()
				self.last_use = time()

				sleep(5)
				self.bot.sendMessage(str(client.channel), "owo use " + ' '.join(use))
			else:
				ui.slowPrinting(f"{self.at()}{color.okcyan} [INFO] {color.reset} You Don't Have Any Available Gems")
	def detect(self):
		m = self.bot.getMessages(client.channel, num = 10)
		m = m.json()
		if type(m) is list:
			for i in range(len(m)):
				if m[i]['author']['id'] == client.OwOID and "**🌱" in m[i]['content']:
					m = m[i]
					break
				if i == len(m) - 1:
					return
			gems = findall(self.regex, m['content'])
			usegems = list(self.gemtypes)
			usegems2 = []
			if len(gems) < 4:
				for i in gems:
					if int(i[0]) in usegems:
						usegems.pop(usegems.index(int(i[0])))
				for i in usegems:
					if int(i) in self.available:
						usegems2.append(i)
				if usegems2:
					self.useGems(usegems2)