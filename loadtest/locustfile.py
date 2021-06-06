from uuid import uuid4
from locust import HttpUser, task, between

class ApiClientUser(HttpUser):
    wait_time = between(0.5, 2.5)

    @task
    def get_user(self):
        uuid = uuid4()
        self.client.get(f"/v1/users/{uuid}", name="/v1/users/{uuid}")