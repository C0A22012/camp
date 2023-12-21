from fastapi import FastAPI

app = FastAPI()

# word = "りんご"
camps = {"りんご":"ringo"}

#クエリパラメータ
@app.get("/camp")
async def camp(word:str):
    if word:
        return (f"param:{camps[word]}")
    else:
        return {"none"}
    
# 
@app.get("/")
async def root():
    return {"message": "Hello World"}
