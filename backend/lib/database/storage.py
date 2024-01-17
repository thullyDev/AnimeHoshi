from django.conf import settings
from imagekitio import ImageKit
import tempfile
import os
import base64
from ..resources import IMAGEKIT_PUBLIC_KEY, IMAGEKIT_PRIVATE_KEY, IMAGEKIT_URL_ENDPOINT

imagekit = ImageKit(
	private_key=IMAGEKIT_PRIVATE_KEY, 
	public_key=IMAGEKIT_PUBLIC_KEY, 
	url_endpoint=IMAGEKIT_URL_ENDPOINT,
)
class Storage:
	def upload(self, name, file):
		file = "C://Users//Thully//Documents//projects//AnimeHoshi//site_logo.jpg"
		upload = imagekit.upload_file(file=file, file_name=name)
		response = upload.response_metadata.raw
		return response.get("url")

	def upload_base64_image(self, name, base64_img):
		imgdata = base64.b64decode(base64_img)
		filename = f"{name}.jpg"  
		with open(filename, 'wb') as file:
		    file.write(imgdata)
		    print(file.name)
		    image_path = os.path.join(settings.BASE_DIR, filename)
		    print(image_path)
		    upload = self.upload(name=filename, file=image_path)
		    print(upload)

		# with tempfile.NamedTemporaryFile(mode="wb", suffix='.jpg') as jpg:
		# 	jpg.write(imgdata)
		# 	upload = self.upload(name=name, file=jpg.name)
		# 	print(upload)


	# def delete(self, file_id, options=None):
	# 	response = imagekit.delete_file(file_id=file_id)
	# 	return response.response_metadata.raw
