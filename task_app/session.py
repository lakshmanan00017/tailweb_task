import os
import time


SESSION_STORE = {}
SESSION_DURATION = 30 * 60 

def generate_token():
    return os.urandom(24).hex()

def create_session(teacher_id):
    token = generate_token()
    expiry = time.time() + SESSION_DURATION
    SESSION_STORE[token] = {"teacher_id": teacher_id, "expiry": expiry}
    return token

def validate_session(token):
    session = SESSION_STORE.get(token)
    if not session:
        return None  

    if time.time() > session["expiry"]:
        del SESSION_STORE[token]  
        return None

    return session["teacher_id"]

def destroy_session(token):
    if token in SESSION_STORE:
        del SESSION_STORE[token]