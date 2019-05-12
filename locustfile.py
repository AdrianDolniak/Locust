from locust import HttpLocust, TaskSet, task


class MyTaskSet(TaskSet):
    @task(1)
    def small_file(self):
        self.client.get("/small.txt")

    @task(1)
    def medium_file(self):
        self.client.get("/medium.txt")

    @task(1)
    def large_file(self):
        self.client.get("/large.txt")

    @task(1)
    def fake_file(self):
        self.client.get("/fake.txt")


class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 9000
