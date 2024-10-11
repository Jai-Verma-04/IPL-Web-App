from google_images_search import GoogleImagesSearch
from config import GIS_API_KEY, CX_ID

gis = GoogleImagesSearch(GIS_API_KEY, CX_ID)

query = 'player'
fileType = 'jpg'

_search_params = {
    'q': query,
    'num': 1,
    'imgType': 'clipart',
    'fileType': fileType,
}
try:
    gis.search(search_params=_search_params, path_to_dir = "..\\static\\icons", custom_image_name=f"{query}")
except Exception as e:
    print(e)