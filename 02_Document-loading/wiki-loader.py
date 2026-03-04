from langchain_community.document_loaders import WikipediaLoader

wiki_docs = WikipediaLoader(
    query="HUNTER X HUNTER", 
    load_max_docs=2).load()

print(f"file-content:")
print(wiki_docs[0].page_content[:400]+"...")

# print(f"meta-data: {wiki_docs[0].metadata}")

print(f"Meta-Data: ")
metadata = wiki_docs[0].metadata

title = metadata.get("title", "N/A")
summary = metadata.get("summary", "")

print(f"title: {title}")
print(f"summary: {summary[:200]}...")

# file-content:
# Hunter × Hunter (pronounced "hunter hunter") is a Japanese manga series written and illustrated by Yoshihiro Togashi. 
# It has been serialized in Shueisha's shōnen manga magazine Weekly Shōnen Jump since March 1998, although the manga has 
# frequently gone on extended hiatuses since 2006. Its chapters have been collected in 38 tankōbon volumes as of September 
# 2024. The story focuses on a young boy nam...

# Meta-Data: 
# title: Hunter × Hunter
# summary: Hunter × Hunter (pronounced "hunter hunter") is a Japanese manga series written and illustrated by Yoshihiro Togashi. 
# It has been serialized in Shueisha's shōnen manga magazine Weekly Shōnen Jump sinc...
