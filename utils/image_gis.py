from google_images_search import GoogleImagesSearch
from config import GIS_API_KEY, CX_ID

gis = GoogleImagesSearch(GIS_API_KEY, CX_ID)

query = 'IPL'
fileType = 'jpg'

_search_params = {
    'q': query,
    'num': 1,
    'imgsize':'huge',
    'fileType': fileType,
}
try:
    gis.search(search_params=_search_params, path_to_dir = "..\\static\\others", custom_image_name=f"{query}.{fileType}")
except Exception as e:
    print(e)