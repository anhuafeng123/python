'''
class Restaurant(object):
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print("餐馆正在营业")
restaurant = Restaurant('飓风餐馆','湘菜')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1 = Restaurant('崔子小吃','川菜')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()


restaurant2 = Restaurant('胡女饭店','粤菜')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()


restaurant3 = Restaurant('浩渺小吃','家常菜')
restaurant3.describe_restaurant()
restaurant3.open_restaurant()

'''
print('*'*50)

class User(object):
    def __init__(self,first_name,last_name,sex,age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
    def describe_user(self):
        print("姓:%s"%self.last_name)
        print("名:%s"%self.first_name)
        print("性别:%s"%self.sex)
        print("年龄:%s"%self.age)
    def greet_user(self):
        print("嘿!我的小可爱!")
user1 = User("树","崔","男","22")
user1.describe_user()
user1.greet_user()
user2 = User("宥嘉","胡","女","18")
user2.describe_user()
user2.greet_user()
user3 = User("淼浩","贾","女","20")
user3.describe_user()
user3.greet_user()














