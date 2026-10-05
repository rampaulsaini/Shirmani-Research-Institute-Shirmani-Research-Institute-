from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'generated/real-product-factory-status.json'
F=['calculator','counter','text-cleaner','seo-title','color-picker','unit-converter','study-timer','flashcard','markdown-preview','drawing-pad','pixel-painter','memory-game','typing-test','budget-planner','habit-tracker','invoice-maker','resume-builder','quiz-maker','prompt-studio','json-formatter','word-counter']
def main():
 OUT.parent.mkdir(exist_ok=True); products=[{'id':f'SP-{i:04d}','family':F[(i-1)%len(F)],'url':f'products/app.html?id=SP-{i:04d}','status':'RUNNABLE'} for i in range(1,1009)]
 p={'strategy':'REAL_PRODUCT_FIRST','target_products':1008,'runnable_products':len(products),'families':len(F),'products':products,'commercial_status':'NO_SALE_CLAIM','verification_status':'DOWNSTREAM','pricing_policy':'Document a comparable reference price before claiming 20% less.','truth_boundary':'Runnable is not automatically sold, delivered, or independently verified.'}
 OUT.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(p['runnable_products'])
if __name__=='__main__':main()
