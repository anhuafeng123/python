class User(object):
    '''这是一个类'''
    def __init__(self,first_name,last_name,sex,age,login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.login_attempts = login_attempts
    def describe_user(self):
        print("姓:%s"%self.last_name)
        print("名:%s"%self.first_name)
        print("性别:%s"%self.sex)
        print("年龄:%s"%self.age)
    def greet_user(self):
        print("嘿!我的小可爱!")
    def increment_login_attempts(self):
        self.login_attempts = int(self.login_attempts) + 1
        print(self.login_attempts)
    def reset_login_attempts(self):
        self.login_attempts*=0
        print(self.login_attempts)
user1 = User("树","崔","男","22","3")
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts() 
'''        
user2 = User("宥嘉","胡","女","18","6")
user2.describe_user()
user2.greet_user()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.reset_login_attempts()        
user3 = User("淼浩","贾","女","20","1")
user3.describe_user()
user3.greet_user()
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.reset_login_attempts()     
'''
