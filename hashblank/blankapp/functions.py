from threading import Thread


def new_thread(function):
    def wrapper(*args, **kwargs):
        thread = Thread(target = function, args=args, kwargs=kwargs)
        thread.daemon = True
        thread.start()
    return wrapper

###################################
