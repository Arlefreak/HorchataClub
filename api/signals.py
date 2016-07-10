from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Horchata
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import environ
import twitter

root = environ.Path(__file__) -2
path = str(root) + '/HorchataClub/.env'
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env(path)

@receiver(post_save, sender=User)
def init_new_user(sender, instance, signal, created, **kwargs):
    if created:
        print ('Token created')
        Token.objects.create(user=instance)

# @receiver(post_save, sender=Horchata)
# def init_new_horchata(sender, instance, signal, created, **kwargs):
#     if created:
#         print ('Horchata Created')
#         api = twitter.Api(
#             consumer_key= env('TW_CONSUMER_KEY'),
#             consumer_secret= env('TW_CONSUMER_SECRET'),
#             access_token_key= env('TW_TOKEN_KEY'),
#             access_token_secret= env('TW_TOKEN_SECRET')
#         )
#         text = 'Check out ' + instance.name + 'on http://horchata.club/'
#         media = instance.image.url
#         # status = api.PostUpdate(text, media)
#         status = api.PostUpdate(text)
#         print(status)
#         instance.tweet = status.id_str
#         instance.save()
