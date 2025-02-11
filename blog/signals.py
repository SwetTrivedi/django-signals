from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed

from django.contrib.auth.models import User

from django.dispatch import receiver

from django.db.models.signals import pre_init,post_init,pre_save,post_save,pre_delete,post_delete,pre_migrate,post_migrate #this is model signals

from django.core.signals import request_started,request_finished,got_request_exception

from django.db.backends.signals import connection_created

@receiver(user_logged_in , sender=User)
def loginsuccess(sender,request,user,**kwargs):
    print("-----")
    print("login in signal")
    print("sender:", sender)
    print("request:", request)
    print("user:", user)
    print(f"kwargs:{kwargs}")

# user_logged_in.connect(loginsuccess,sender=User)



# @receiver(user_logged_out , sender=User)
# def log_out(sender,request,user,**kwargs):
#     print("-----")
#     print("logout in signal")
#     print("sender:", sender)
#     print("request:", request)
#     print("user:", user)
#     print(f"kwargs:{kwargs}")

# user_logged_out.connect(log_out,sender=User)



# @receiver(user_login_failed)
# def login_failed(sender,credentials,request,**kwargs):
#     print("-----")
#     print("login failed  signal")
#     print("sender:", sender)
#     print('credintials: ',credentials)
#     print("request:", request)
#     print(f"kwargs:{kwargs}")



# @receiver(pre_save,sender=User)
# def at_begging_save(sender,instance,**kwargs):
#     print("_______________________")
#     print("Pre Save")
#     print("sender : ",sender)
#     print("instance: ",instance)
#     print(f"kwargs :,{kwargs}")
# pre_save.connect(at_begging_save,sender=User)


# @receiver(post_save,sender=User)
# def at_ending_save(sender,instance,created,**kwargs):
#     if created:
#         print("_______________________")
#         print("Post Save Signal ")
#         print("New Record ")
#         print("sender : ",sender)
#         print("instance: ",instance)
#         print("instance: ",created)
#         print(f"kwargs :,{kwargs}")
#     else:
        # print("_______________________")
        # print("Post Save Signal ")
        # print("Update")
        # print("sender : ",sender)
        # print("instance: ",instance)
        # print("instance: ",created)
        # print(f"kwargs :,{kwargs}")
# post_save.connect(at_ending_save,sender=User)

# @receiver(pre_delete,sender=User)
# def at_beginig_delete(sender,instance,**kwargs):
#     print("__________________________________")
#     print("Pre _Delete")
#     print("sender : ",sender)
#     print("instance: ",instance)
#     print(f"kwargs :,{kwargs}")




# @receiver(post_delete,sender=User)
# def at_ending_delete(sender,instance,**kwargs):
#     print("__________________________________")
#     print("Post_Delete")
#     print("sender : ",sender)
#     print("instance: ",instance)
#     print(f"kwargs :,{kwargs}")


# @receiver(pre_init,sender=User)
# def at_begining_init(sender,args,**kwargs):
#     print("__________________________________")
#     print("Pre _init")
#     print("sender : ",sender)
#     print(f"args:,{args}")
#     print(f"kwargs :,{kwargs}")


# @receiver(post_init,sender=User)
# def at_ending_init(sender,*args,**kwargs):
#     print("__________________________________")
#     print("Post_init")
#     print("sender : ",sender)
#     print(f"args: ,{args}")
#     print(f"kwargs :,{kwargs}")


# @receiver(request_started)
# def at_begining_request(sender, environ,**kwargs):
#     print("__________________________________")
#     print("Request started")
#     print("sender : ",sender)
#     print("environ:",environ)
#     print(f"kwargs :{kwargs}")



# @receiver(request_finished)
# def at_begining_request(sender,**kwargs):
#     print("__________________________________")
#     print("Request finished")
#     print("sender : ",sender)
#     print(f"kwargs :{kwargs}")


# @receiver(got_request_exception)
# def at_begining_request(sender, request,**kwargs):
#     print("__________________________________")
#     print("Request got exception")
#     print("sender : ",sender)
#     print("environ:",request)
#     print(f"kwargs :{kwargs}")


# @receiver(pre_migrate)
# def before_install_app(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
#     print("_______________________________")
#     print("Before install app ")
#     print("sender : ",sender)
#     print("App_config :",app_config)
#     print("verbosity :",verbosity)
#     print("interactive :",interactive)
#     print("Using : ",using)
#     print("plan : ",plan)
#     print('apps :',apps)
#     print(f'kwargs : {kwargs}')



# @receiver(post_migrate)   
# def at_end_migrte_flush(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
#     print("_______________________________")
#     print("at end migrate flush ")
#     print("sender : ",sender)
#     print("App_config :",app_config)
#     print("verbosity :",verbosity)
#     print("interactive :",interactive)
#     print("Using : ",using)
#     print("plan : ",plan)
#     print('apps :',apps)
#     print(f'kwargs : {kwargs}')




# @receiver(connection_created)
# def connect_database(sender,connection,**kwargs):
#     print("_______________________________")
#     print("connection Database ")
#     print("sender : ",sender)
#     print("App_config :",connection)
#     print(f"App_config :{kwargs}")
    






































# Today i learned about :-

# 1. Authentication Signals ( Logged_in, Logged_out , and Login_failed signal ).

# 2. Models Signals ( Pre_save , Post_save , Pre_delete ,  Post_delete and Pre_init , Post_init signals ).

# 3. Request/Response signals ( Request_started , Request_finished , got_request_exceptions signals )

# 4. Management Signals ( Pre_migrate , Post_migrate signals )

# 5. Database_wraper ( Connection_created signals )