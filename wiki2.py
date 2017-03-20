import requests, sys
import codecs #윈도우의 경우 
search_word = sys.argv[1]
api_url = 'https://en.wikipedia.org/w/api.php'
api_params = {'format':'xmlfm', 'action':'query', 'prop':'revisions', 'rvprop':'content'}
api_params['titles'] = search_word
wiki_data = requests.get(api_url, params=api_params)
fo = codecs.open('C:\\Users\\(유저이름)\\Desktop\\'+ search_word + '.html', 'w', 'utf-8') #윈도우의 경우
#fo = open('/Users/(유저이름)/Desktop/'+ search_word + '.html', 'w') #Mac의 경우
fo.write(wiki_data.text)
fo.close()  
