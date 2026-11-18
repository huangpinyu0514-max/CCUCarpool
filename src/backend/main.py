from fastapi import FastAPI
from model import EmailVertification, CodeVertification, User
from crud import *
import smtp

app = FastAPI()
EMAILVERTIFICATION_CODE = None

@app.get("/apitest")
def apitest():
    return {"all":"good"}

@app.post("/vertify/email")
def vertify_email(req: EmailVertification):
    if email_exist(req.email):
        return {"exist": True}
    EMAILVERTIFICATION_CODE = smtp.send_vertification_code(req.email)
    return {"exist": False}

@app.post("/vertify/code")
def vertify_code(req: CodeVertification):
    if (req.code == EMAILVERTIFICATION_CODE):
        create_user(req.user)
        return {"status": True}
    else:
        return {"status": False}