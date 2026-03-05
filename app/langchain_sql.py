from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from app.config import OPENAI_API_KEY

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)

prompt_template = """You are a PostgreSQL expert.

Table: sales_daily

Columns:
- date (date)
- region (text)
- category (text)
- revenue (numeric)
- orders (integer)
- created_at (timestamp)

Return ONLY a single SQL SELECT query.
Do not include markdown or backticks.

Question:
{question}

SQL:
"""

prompt = PromptTemplate(
    input_variables=["question"],
    template=prompt_template
)

def generate_sql(question):
    chain = prompt | llm
    response = chain.invoke({"question": question})
    return response.content.strip()
