from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class User(AbstractUser):
    pass


class Deal(models.Model):
    """Deal contains all the info about a Deal that was posted
        - User who posted
        - Content of the post itself
        - date and time of the post
        - Likes (0 for first)
    """

    id = models.AutoField(primary_key = True)
    heading = models.CharField(max_length=64)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created")
    url = models.URLField()
    description = models.TextField(max_length=500)
    price = models.IntegerField(default=0, blank=True)
    d_code = models.CharField(max_length=15, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    category = models.CharField(max_length=15, default="not_defined")

    def __str__(self):
        return f"User: {self.creator} created this Deal {self.heading} on {self.end_date}"

    # make the serialize function to acess the items values in python 
    def serialize(self):
        return {
            "id": self.id,
            "creator": self.creator,
            "link": self.link,
            "description": self.description,
            "price": self.price,
            "d_code": self.d_code,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "category": self.category,

        }