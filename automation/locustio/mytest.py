import time
from locust import HttpUser, task

class QuickstartUser(HttpUser):
    @task
    def blog_view(self):
        self.client.get("/blog")
        time.sleep(1)

    @task
    def view_admin(self):
        self.client.get("/admin")
        self.client.post("/login", json={"username":"_____", "password":"____"})
        time.sleep(1)

    @task(3)
    def add_post(self):
        self.client.get("/main")

    def on_start(self):
        self.client.post("/login", json={"username":"_____", "password":"____"})

    def on_stop(self):
        self.client.get("/logout")