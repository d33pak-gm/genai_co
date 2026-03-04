from langchain_community.document_loaders import TextLoader

txt_loader = TextLoader(
    file_path="./docs/short-story.txt", 
    autodetect_encoding=True
    )

texts = txt_loader.load()
print(texts[0].page_content[:300])


## -- lazy_load() returns a generator/iterator, not a list. You can't index it with texts[i] directly.

# texts = list(txt_loader.lazy_load())  # Convert to list

# retrived_data = [texts[i] for i in range(min(300, len(texts)))]
# print("\n", retrived_data[0].page_content[:300])
# print()
# print(f"meta-data: {retrived_data[0].metadata}")



## -- o/p:

#         Snow White and the Seven Dwarfs

# Once upon a time in the middle of winter, when the flakes of
# snow were falling like feathers from the sky, a queen sat at
# a window sewing, and the frame of the window was made of black
# ebony.  And whilst she was sewing and looking out of the window
# at the snow, she

# (prj_venv) C:\Users\deeo_\Desktop\Ai_Pract\02_Document-loading>python txt_loader.py

#         Snow White and the Seven Dwarfs

# Once upon a time in the middle of winter, when the flakes of
# snow were falling like feathers from the sky, a queen sat at
# a window sewing, and the frame of the window was made of black
# ebony.  And whilst she was sewing and looking out of the window
# at the snow, she

# meta-data: {'source': './docs/short-story.txt'}