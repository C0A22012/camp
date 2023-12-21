from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#クエリパラメータ
@app.get("/camp")
async def camp(word:str):
    s_words = {"海":["狩野川キャンプ場", "宇和海キャンプ村", "美ら海水族館キャンプ場"],
             "山":["木曽福島キャンプ場", "富士五湖周辺のキャンプ場", "穂高温泉周辺"],
             "川":["川野辺キャンプ場"]}
    info = {"狩野川キャンプ場":["静岡県", "テント・肉"],
             "宇和海キャンプ村":["高知県", "テント・魚"],
             "美ら海水族館キャンプ場":["沖縄県", "ガス・酒"]}
        
    for i in word:
        if i in s_words:
            camps = s_words[i]
            for j in camps:
                return {"result":f"キャンプ場:{camps}　　キャンプ場情報：{info[j]}"}
    
    return {"result":"検索結果が見つかりませんでした。"}
    
# 
@app.get("/")
async def root():
    return {"message": "Hello World"}
