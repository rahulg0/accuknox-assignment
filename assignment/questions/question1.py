from models import Author
from django.dispatch import receiver
from django.db.models.signals import post_save
import time

@receiver(post_save, sender=Author)
def create_author(sender, instance, **kwargs):
    print("Creating author with name: ", instance.name)
    time.sleep(20) # since default nature of signal receiver is synchronous it will wait for 20 seconds
    print("Author created successfully")

# for this to work we have to make instance of the model

author1 = Author.objects.create(name="J.K Rowling", email="rownling@gmail.com")
author1.save()

#Output we would receive from signals would be like this

#Creating author with name:  J.K Rowling
#Then we will get 20 seconds of delay which describes that the task is time consuming
#Author created successfully

'''
This example tells us about the synchronous nature of signal receiver.
Though we can make it synchronous by using async or celery to send the signal.
Then our program wont have to wait for 20 seconds and celery workers will take care of it, but i use async as it is easy to implement.
'''