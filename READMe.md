
* create class

```
class MenuItem:
	pass
```

* create instance

```
menu_item1 = MenuItem()

```


* set instance variables

```
menu_item1.name = 'Sandwich'
```

* create class functions @ methods
```
class MenuItem:
	def hello(self):
		print('Hello!')


```

* call instance methods
```
menu_item1 = MenuItem()
menu_item1.hello() 
```

* self
```
class MenuItem:
	def info(self):
		print(self.name)

menu_item1 = MenuItem()
menu_item1.name = 'Sandwich'
menu_item1.info()
```

A class is like a blueprint and an instance is an object that we create using that blueprint. The properties of an instance are called instance variables and functions are called instance methods.

__init__ method (also known as a class constructor in Python), which is executed right after an instance is created. When ClassName() is called and an instance is created, the __init__ method will be called immediately after

```

class MenuItem:
	def __init__(self):
		print(' ')  // call automatically

menu_item1 = MenuItem()		
```

Instance Variables in __init__
```
class MenuItem:
	def __init__(self):
		self.name = 'Sandwich'

menu_item1 = MenuItem()
print(menu_item1.name)
```

```
class MenuItem:
	def __init__(self,name):
		self.name = name

menu_item1 = MenuItem('Chocolate Cake')		
print(menu_item1.name)

```