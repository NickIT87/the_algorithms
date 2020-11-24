from locust import User, task, between

class MyUser(User):
    @task
    def my_task(self):
        print("executing my_task")

    wait_time = between(0.5, 10)