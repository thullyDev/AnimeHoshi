from .imageKit import imagekit
from PIL import Image

class Storage:
	def upload(self, name, file):
		upload = imagekit.upload_file(file=file, file_name=name)
		response = upload.response_metadata.raw
		return response.get("url")

	def upload_base64_image(self, name, base64):
		base64_bytes = base64.encode('utf-8')
		binary_data = base64.b64decode(base64_bytes)
		temp_file = tempfile.NamedTemporaryFile(delete=False)
		temp_file.write(binary_data)  
		temp_file.close() 
		img = Image.open(temp_file.name)
		import os
		os.remove(temp_file.name)

	# def delete(self, file_id, options=None):
	# 	response = imagekit.delete_file(file_id=file_id)
	# 	return response.response_metadata.raw
