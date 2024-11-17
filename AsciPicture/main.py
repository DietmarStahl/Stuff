import matplotlib.pyplot as plt
import urllib.request
import io
import numpy as np

url = "https://github.com/DietmarStahl/Stuff/blob/main/AsciPicture/image.png?raw=true"
response = urllib.request.urlopen(url)
image = plt.imread(io.BytesIO(response.read()))

weights = np.array([0.2989, 0.5870, 0.1140])
image_values = np.dot(image[...,:3], weights)

ascii_bins = [0.1, 0.2, 0.3, 0.4, 0.6, 0.8, 1.0]
ascii_chars = np.array(['.', ':', '+', '*', '#', '%', '@'])

bin_indices = np.digitize(image_values, ascii_bins)

image_ascii = ascii_chars[bin_indices - 1]

with open('ascii_art.txt', 'w') as f: 
    for row in image_ascii:
        f.write(''.join(row) + '\n')
