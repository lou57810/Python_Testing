from locust import HttpUser, task


class ProjectPerfTest(HttpUser):

    club = [
        {
            "name": "Héraclès_Temple",
            "email": "heracles@heavylift.gr",
            "points": "12"
        }]

    competition = [
        {
            "name": "Summer LiftTest",
            "date": "2023-04-20 15:00:00",
            "numberOfPlaces": "35"
        }]

    @task
    def perf_login(self):
        email = "john@simplylift.co"
        self.client.post("/showSummary", data={"email": email})

    @task
    def perf_index(self):
        self.client.get("/")

    @task
    def perf_book(self):
        self.client.get('/book/Winter Meeting/Simply Lift')

    @task
    def perf_purchase_places_page(self):

        self.client.post("/purchasePlaces", data={
            "club": "Simply Lift",
            "competition": "Winter Meeting",
            "places": 28})

    @task
    def perf_logout(self):
        self.client.get("/logout")
