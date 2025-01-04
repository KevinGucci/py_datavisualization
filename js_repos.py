import requests
import plotly.express as px
import pandas as pd

url='https://api.github.com/search/repositories?q=language:javascript&sort=stars'

response= requests.get(url)
print(f"Status Code:{response.status_code}")

respository= response.json()
print(respository.keys())

repo1= pd.json_normalize(respository['items'])
print(repo1)
name= repo1['name']
stars= repo1['stargazers_count']
url=repo1['owner.login']

fig= px.bar(x=name,y=stars,title="repos",hover_name=url,color=stars)
fig.show()