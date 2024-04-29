from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # assuming rating from 1 to 5
    comment = models.TextField(max_length=200)
    review_date = models.DateField(auto_now_add=True)
    
    # GenericForeignKey fields
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # Self-referencing ForeignKey to support replies within the same model
    parent = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"Review {self.id} by {self.user.username}"

    @staticmethod
    def get_reviews_for_service(service_model, service_id):
        content_type = ContentType.objects.get_for_model(service_model)
        reviews = Review.objects.filter(content_type=content_type, object_id=service_id)
        return reviews
