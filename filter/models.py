from django.db import models


class Filter(models.Model):
    ifa = models.CharField(max_length=54)
    is_dhaka = models.BooleanField(default=False)
    is_khulna = models.BooleanField(default=False)
    is_male = models.BooleanField(default=False)
    is_female = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ifa

    class Meta:
        indexes = [
            models.Index(fields=['is_dhaka', ]),
            models.Index(fields=['is_khulna', ]),
            models.Index(fields=['is_male', ]),
            models.Index(fields=['is_female', ]),
        ]