class Employee:

	def __init__(self,name,age,position,salary):
		self.name = name
		self.age = age
		self.position = position
		self.salary = salary
		print(f"""
		name: {self.name}\n
		age: {self.age}\n
		position: {self.position}\n
		salary: {self.salary}
		""")

employee1 = Employee('Ji-Soo',38,'developer',1200)



