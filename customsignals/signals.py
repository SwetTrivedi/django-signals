from django.dispatch import Signal,receiver
notification=Signal(providing_args=["request","user"])
@receiver(notification)
def show(sender,**kwargs):
    print(sender)
    print(f"{kwargs}")