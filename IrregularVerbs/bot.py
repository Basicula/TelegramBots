import json
import random as rand

class IrregularVerb:
	def __init__(self,first,second,third):
		self.first = first
		self.second = second
		self.third = third
	
	@property
	def __dict__(self):
		first = self.first
		
		second = self.second[0]
		for i in range(1,len(self.second)):
			second += ' or ' + self.second[i]
			
		third = self.third[0]
		for i in range(1,len(self.third)):
			third += ' or ' + self.third[i]
		
		return first + ', ' + second + ', ' + third
	
	@property
	def __data__(self):
		return [self.first,self.second,self.third]

def GetData():
	with open('data.txt', 'r') as file:
		data = file.read()
		data = data.split('\n')
		words = {}
		curr_first_letter = ''
		for line in data:
			if line == '':
				continue
			if len(line) == 1:
				curr_first_letter = line.lower()
				words.setdefault(curr_first_letter, [])
			else:
				word = line.split('\t')
				verb = IrregularVerb(word[0], word[1].split('/'), word[2].split('/'))
				if curr_first_letter in words:
					words[curr_first_letter].append(verb)
		return  words

def DumpData(data):
	print(json.dumps(data, default=lambda x: x.__dict__,indent=4))
	
def ShowMessage(message):
	pass
	
def PushQuestion(data):
	type = rand.randint(0,6)
	letter = rand.choice("qwertyuiopasdfghjklzxcvbnm")
	while len(data[letter])==0:
		letter = rand.choice("qwertyuiopasdfghjklzxcvbnm")
	word = rand.choice(data[letter])
	print(word.__data__)
	#if 0: 
	#	GiveSecondByFirst
	#if 1:
	#	GiveThirdByFirst 
	#if 2:
	#	GiveFirstBySecond
	#if 3:
	#	GiveThirdBySecond
	#if 4:
	#	GiveFirstByThird
	#if 5:
	#	GiveSecondByThird
	#if 6:
	#	GiveAllByFirst

if __name__ == "__main__":
	data = GetData()
	PushQuestion(data)
	#DumpData(data)
	
