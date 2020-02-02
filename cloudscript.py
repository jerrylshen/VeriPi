from cloudinary import Search
import urllib.request

cloudName = 'dth0ow8ry'
api_key = 293352914274159
api_secret = 'wLi2XaqNePSx2f9jAFDX39vqTzg'
target_directory = '/Users/Richard/Documents/UCI/HackUCI2020/unknown/'

search = Search()
search.expression('face')
faces = search.execute(cloud_name=cloudName, api_key=api_key, api_secret=api_secret)
for i, item in enumerate(faces['resources']):
    urllib.request.urlretrieve(item['url'], f"{target_directory}{item['filename']}{i}.{item['format']}")
print('Faces downloaded')