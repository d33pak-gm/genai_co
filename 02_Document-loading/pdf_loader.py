## For more ref - https://docs.langchain.com/oss/python/integrations/document_loaders

from langchain_community.document_loaders import PyPDFLoader

try:
    pdf_loader = PyPDFLoader(
        file_path="./docs/PAPER1.pdf",
        mode="page",
        extract_images=False
    )
    pdf_doc = pdf_loader.load()
    # txt_doc

    print(f"page contents: {pdf_doc[0].page_content[:300]}")
    print() # new-line
    print(f"meta-data-of-page: {pdf_doc[0].metadata}")

except Exception as e:
    print(f"Failed to fetch!\n{e}")



# page contents: Provided proper attribution is provided, Google hereby grants permission to
# reproduce the tables and figures in this paper solely for use in journalistic or
# scholarly works.
# Attention Is All You Need
# Ashish Vaswani∗
# Google Brain
# avaswani@google.com
# Noam Shazeer∗
# Google Brain
# noam@google.com
# Niki Par

# meta-data-of-page: {'producer': 'pdfTeX-1.40.25', 'creator': 'LaTeX with hyperref', 'creationdate': 
# '2024-04-10T21:11:43+00:00', 'author': '', 'keywords': '', 'moddate': '2024-04-10T21:11:43+00:00', 
# 'ptex.fullbanner': 'This is pdfTeX, Version 3.141592653-2.6-1.40.25 (TeX Live 2023) kpathsea version 6.3.5', 
# 'subject': '', 'title': '', 'trapped': '/False', 'source': './docs/PAPER1.pdf', 'total_pages': 15, 'page': 0, 
# 'page_label': '1'}