import pandas as pd
import numpy as np
import fetch_api
import measures



df = pd.read_csv('arxiv_papers.csv', delimiter=',', encoding = "utf8")


def get_abstract_main(paper_df_index):
    paper_id = df.iloc[paper_df_index]['url'][df.iloc[paper_df_index]['url'].rindex('/')+1:]
    main_text, abstract = fetch_api.get_clean_text(paper_id)
    return main_text,abstract,paper_id

#a couple of indexes
indicis = [2]


papers = {}
for i in indicis:
    main_text, abstract,paper_id = get_abstract_main(i)
    papers[paper_id] = measures.models_agreement(abstract, main_text)
#    print(test(abstract, main_text))
#    print('-------------')
#    print(post_process(abstract, main_text))