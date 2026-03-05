from fastapi import APIRouter, Form
from app.langchain_sql import generate_sql
from app.database import run_query
import pandas as pd

router = APIRouter()

@router.post("/ask-data")
async def ask_data(text: str = Form(...)):
    try:
        sql = generate_sql(text)
        columns, rows = run_query(sql)
        
        df = pd.DataFrame(rows, columns=columns)
        preview = df.head(10).to_markdown(index=False)
        
        return {
            "response_type": "in_channel",
            "text": f"*SQL Generated*\n```{sql}```\n\n*Result Preview*\n```{preview}```"
        }
    
    except Exception as e:
        return {
            "response_type": "ephemeral",
            "text": f"Error: ```{str(e)}```"
        }
