from models import Author
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import transaction


@receiver(post_save, sender=Author)
def create_author(sender, instance, **kwargs):
    print('creating author.......')
    transaction.on_commit(lambda: print('author created successfully'))


#Output we would get will be
#creating author.......
#author created successfully

'''
as creating author..... runs before author created successfully, thi tells us that
signal handler runs within the same transaction by default.

we can make it run on different transaction as well using transaction.atomic()
'''