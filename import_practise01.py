import  requests
text = requests.get('http://news.baidu.com')
print(text.content)







