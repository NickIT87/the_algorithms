from locust import User, TaskSet


def login(l):
    print("I am logged in")

def logout(m):
    print("I am logged out")

class UserBehaviour(TaskSet):
    tasks = [login, logout]

class User(User):
    task_set = UserBehaviour
