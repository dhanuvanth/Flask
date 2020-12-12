import base64
image = open('wall_e.jpeg', 'rb')
image_read = image.read()
image_64_encode = base64.encodestring(image_read)
image_64_decode = base64.decodestring(image_64_encode)
image_result = open('wall_e1.txt', 'wb') # create a writable image and write the decoding result
image_result.write(image_64_encode)
image_result = open('wall_e1.jpeg', 'wb') # create a writable image and write the decoding result
image_result.write(image_64_decode)