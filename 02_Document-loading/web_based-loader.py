from langchain_community.document_loaders import WebBaseLoader
import bs4 # - beautifully soup-4

# web_loader = WebBaseLoader(
#     web_path=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
#     header_template={"User-Agent": "MyLangChainAgent/3.0"}
#     )

# web_data = web_loader.load()

# print(web_data[0].page_content[:300])
# print()
# print(web_data[0].metadata)


## -- Instead of whole page you can take any div's data in page

web_loader_div = WebBaseLoader(
    web_path=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    header_template={"User-Agent": "MyLangChainAgent/3.0"},
    bs_kwargs=dict(parse_only=bs4.SoupStrainer(
        ## retrive based on these sections
        class_=('Post-title', "post-contect","post-header")
    ))
)

data = web_loader_div.load()

print("Page-Content: ")
print(data[0].page_content[:300]+"...")

print("Meta-Data:")
print(data[0].metadata)


# Page-Content: 


#       LLM Powered Autonomous Agents

# Date: June 23, 2023  |  Estimated Reading Time: 31 min  |  Author: Lilian Weng


# ...
# Meta-Data:
# {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}