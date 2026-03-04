from langchain_community.document_loaders import ArxivLoader

arxiv_loader = ArxivLoader(
    query="1706.03762",
    doc_content_chars_max=1000,  # Extract max 1000 characters per paper
    load_max_docs=2
)

arxiv_data = arxiv_loader.load()

print(f"file-content:\n {arxiv_data[0].page_content[:400]}")

print() # - new line

print(f"meta-data: {arxiv_data[0].metadata}")

## o/p: will load data from - https://arxiv.org/abs/1706.03762 (attention is all you need.)

