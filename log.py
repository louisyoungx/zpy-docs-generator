from config import DEBUG

def log(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
