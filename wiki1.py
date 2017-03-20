import requests
import codecs
api_base_url = 'https://en.wikipedia.org/w/api.php'
api_params = {'format':'xmlfm', 'action':'query', 'titles':'jack bauer',
'prop':'revisions', 'rvprop':'content'}
wiki_data = requests.get(api_base_url, params=api_params)
#fo = codecs.open('C:\\Users\\(유저이름)\\Desktop\\wiki.html', 'w', 'utf-8') #window의 경우
#fo = open('/Users/( 유저이름)/Desktop/wiki.html', 'w') #Mac의 경우
fo.write(wiki_data.text)
fo.close()  
