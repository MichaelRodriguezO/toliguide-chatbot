def get_session_id(data):
    session_id = data.get("session_id")
    if not session_id:
        session_id = "anonymous"
    return session_id
