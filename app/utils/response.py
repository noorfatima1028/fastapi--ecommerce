def success(data=None, message="Success"):
    return {"status": "success", "message": message, "data": data}

def error(message="Something went wrong", code=400):
    return {"status": "error", "message": message, "code": code}