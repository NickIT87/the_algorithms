from locust import HttpUser, TaskSet, task

#https://martinschrader.pythonanywhere.com/

class UserBehaviour(TaskSet):
    @task
    def launch_Url(self):
        self.client.get("/")


class User(HttpUser):
    task_set = UserBehaviour()
    min_wait = 5000
    max_wait = 15000
