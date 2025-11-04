from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph
from dotenv import load_dotenv
from news import Fetch_news,response
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
load_dotenv()

def News(response):


    news_data = Fetch_news(response)
    formatted_news = "\n".join([
        f"{item['Index']}. {item['Title']} (Source: {item['Source']})"
        for item in news_data
    ])
    messages=[
        SystemMessage(content=
                    (
                        "You are a professional LinkedIn content writer "
                            "who creates engaging posts summarizing daily tech news "
                            "in a friendly and informative tone. "
                            "like #AI #Tech #Innovation #Startups"
                            "also if you find any news not releated to tech remove it"
                            "there should be only two headline which len should be less then 150 characters"
                            

                    )
                    
                    ),
        HumanMessage(content=f"Here are today's top tech news:\n\n{formatted_news}")

    ]

    # print(Fetch_news)
    llm=ChatOpenAI(temperature=0)

    hi=llm.invoke(messages)
    res=hi.content

    return res

