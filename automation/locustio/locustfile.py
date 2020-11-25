import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("https://martinschrader.pythonanywhere.com")
        print("executing my_task")
        
    wait_time = between(0.5, 10)
    


##from locust import User, task, between

##class MyUser(User):
##    @task
##    def my_task(self):
##        print("executing my_task")

##    wait_time = between(0.5, 10)