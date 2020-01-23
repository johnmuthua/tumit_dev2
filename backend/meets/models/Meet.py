from django.db import models
from django.contrib.auth.models import User
from .import Profile


class Meet(models.Model):

    PARTNER = 'PART'
    VOLUNTEER = 'VOL'
    SPONSOR = 'SPR'
    CORPORATE = 'CORP'
    CROWDSOURCE = 'CRWD'
    INTERN = 'INTR'
    OPENSOURCE = 'OPNS'

    TYPE = (
        (PARTNER, "partner"),
        (VOLUNTEER, "volunteer"),
        (SPONSOR, "sponsor"),
        (CORPORATE, "corporate"),
        (CROWDSOURCE, "crowdsource"),
        (INTERN, "intern"),
        (OPENSOURCE, "opensource"),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meets')
    type = models.CharField(max_length=4, choices=TYPE, default=VOLUNTEER)
    title = models.CharField(max_length=150)
    body = models.TextField()
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    u_name = models.CharField(max_length=50, blank=True, null=True)

    # TODO create custom method to fill fullname
    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     self.u_name = str(Profile.qu)
    #     super(Meet, self).save(*args, **kwargs)
