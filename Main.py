import random
import time
import sys
#from PySide.QtCore import *
#from PySide.QtGui import *

class MultiTable:
	"""Multiplication table"""
	def __init__(self,start=2,end=9,action=['*',':'],count=40):
		self.start=start
		self.end=end
		self.action=action
		self.count=count
	def get_action(self):
		first=random.randint(self.start,self.end)
		second=random.randint(self.start,self.end)
		action=random.choice(self.action)
		if action=='*':
			return (first,second,action,first*second)
		else:
			return (first*second,second,action,first)
		
	def step(self):
		first,second,action,correct_answer=self.get_action()
		print (first,action,second,' = ')
		time_at_start=time.time()
		try:
			
			raw_input=input()
			answer=int(raw_input)
		except:
			return 
		step_time=time.time()-time_at_start
		if answer == correct_answer:
			print ("Correct! Great")
			return (True,first,second,action,step_time)
		else:
			print ("Wrong :( Right answer is ", correct_answer)
			return (False,first,second,action,step_time)
		
		
	def game(self):
		result=[]
		print('start')
		input()
		for i in range(self.count):
			step_result=self.step()
			if step_result==None:
				f=open("Results.txt","a")
				
				timesum=sum(x[4] for x in result)
				print (time.strftime('%X %d %B %Y'),file=f)
				print ("Total time is",int(timesum), ",average time is ", int(timesum/(i)), ' for ', i,'iterations')
				print ("Total time is",int(timesum), ",average time is ", int(timesum/(i)), ' for ', i,'iterations', file=f)
				correct=int(sum(1 for x in result if x[0]==True) / i*100)
				print ( '% of correct answers is ', correct)
				print ( '% of correct answers is ', correct,file=f)
				print ('errors in', set((x[1],x[3],x[2]) for x in result if x[0]==False))
				print ('errors in', set((x[1],x[3],x[2]) for x in result if x[0]==False),file=f)
				print ('\n',file=f)
				
				f.close()
				input()
				return
				
			else:
				result.append(step_result)
			
	def save_to_file(self):
		f=open("Results.txt","a")
		f.writeline()



def main():
	table=MultiTable()
	#app = QApplication(sys.argv)
	# Create a button, connect it and show it
	#button = QPushButton("Click me")
	#button.clicked.connect(table.game)
	#button.show()
	# Run the main Qt loop
	#app.exec_()    
	table.game()			
			



if __name__ == "__main__":
	main()
		