from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_issue_list():
    with open("./data/issue_list.csv") as f:
        issue_list = f.read()
        return issue_list