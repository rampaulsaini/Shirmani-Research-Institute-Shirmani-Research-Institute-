def health():
    return False

def discover():
    return []

def prepare(item):
    return {"status":"PLANNED","reason":"null_adapter"}

def execute(item):
    return {"status":"NOT_EXECUTED","reason":"null_adapter"}
