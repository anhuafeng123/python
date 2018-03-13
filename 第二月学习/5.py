class Restaurant(object):
    def __init__(self,restaurant_name,cuisine_type):
        self.number_served = 0
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print("餐馆正在营业")
    def set_number_served(self,num):
        self.num = num
        print("当前就餐人数:%s"%self.num)
    def increment_number_served(self):
        self.num+=1
        print("我认为这家餐馆每天可能接待:%s"%self.num)

restaurant = Restaurant('飓风餐馆','湘菜',)
restaurant.describe_restaurant()

restaurant.number_served = 5
print("在这家店就餐过的人数在:%s"%restaurant.number_served)

restaurant.open_restaurant()
restaurant.set_number_served(22)
restaurant.increment_number_served()
