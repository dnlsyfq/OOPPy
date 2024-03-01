class MenuItem:
	def info(self,price):
		print(f"The price of the {self.name} is ${price}")

menu_item1 = MenuItem()
menu_item2 = MenuItem()
menu_item3 = MenuItem()
menu_item4 = MenuItem()

menu_item1.name = 'Sandwich'
menu_item1.info(5)

menu_item2.name = 'Chocolate Cake'
menu_item2.info(4)

menu_item3.name = 'Coffee'
menu_item3.info(3)

menu_item4.name = 'Orange Juice'
menu_item4.info(2)