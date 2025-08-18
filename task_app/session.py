import os
import time


session_store = {}
session_duration = 30 * 60 

def generate_token():
    return os.urandom(24).hex()

def create_session(teacher_id):
    token = generate_token()
    expiry = time.time() + session_duration
    session_store[token] = {"teacher_id": teacher_id, "expiry": expiry}
    return token

def validate_session(token):
    session = session_store.get(token)
    if not session:
        return None  

    if time.time() > session["expiry"]:
        del session_store[token]  
        return None

    return session["teacher_id"]

def destroy_session(token):
    if token in session_store:
        del session_store[token]
