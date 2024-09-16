from models import Author
from django.dispatch import receiver
from django.db.models.signals import post_save
import threading

@receiver(post_save, sender=Author)
def create_author(sender, instance, **kwargs):
    print('creating author in thread: ', threading.current_thread().name)

#Now for us to know that the thread in which signal is running and caller is running is same we should print it aswell 
#we can do that by using threading.current_thread().name
print('current thread: ', threading.current_thread().name)

#OUtput we would get will be

#creating author in thread:  MainThread
#current thread:  MainThread

'''
Now we can see that the thread in which signal is running and caller is running is same.
Also we can run the signal in seperate thread as well by using threading.thread(target, args)

'''
