from GoogleNews import GoogleNews
import pandas as pd

def newsgoogle(search):
    googlenews= GoogleNews()
    googlenews.set_lang('en')
    search_key = googlenews.search(search)

    googlenews.set_period('4d')
    googlenews.get_page(6)

    titles = googlenews.get_texts()
    Data = []
    for head in titles:
        title = {"Headlines": head}
        Data.append(title)

    df = pd.DataFrame(Data)
    df.to_csv("news.csv",index=False)
    df
newsgoogle("Tata")