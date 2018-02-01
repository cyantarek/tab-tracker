from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

	@task
	def get_songs(self):
		return self.client.get("/")


class WebsiteBehavior(HttpLocust):
	task_set = UserBehavior