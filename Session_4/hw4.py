from bs4 import BeautifulSoup
import pandas as pd
import requests as req

target_url = "https://opentutorials.org/course/1"

res = req.get(target_url)
soup = BeautifulSoup(res.text, "html.parser")
li_comment = soup.find_all(class_="comment_content") #li_comment = soup.select('div.comment_content')로 접근하면 안되는 이유.
li_comment_processed = [e.text.strip() for e in li_comment]
li_time = soup.select('div.name.time > a > time') #soup.select(여기에 무엇을 넣어야하고 return이 뭔지), find_all(이 안에는 뭘 넣어줘야하고 뭐가 나오는 건지)
li_time_processed = [e.text for e in li_time]
li_name = soup.select('div.name.time > strong')
li_name_processed = [e.text for e in li_name]
context = {"name":li_name_processed, "date":li_time_processed, "comment":li_comment_processed}
df_table = pd.DataFrame(context)
print(df_table)