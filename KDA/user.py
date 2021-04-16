from flask import session

def getuser():
    try:
        user = session["USER_ID"]
    except:
        user = "Guest"
    return user