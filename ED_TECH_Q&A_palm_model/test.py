from langchain.llms import GooglePalm 


llm = GooglePalm.configure(google_api_key = GOOGLE_API_KEY)
poem = llm("write a 4 line poem for my love")
print(poem)