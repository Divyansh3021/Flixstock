from PIL import Image

input_image = Image.open('input.jpg')
mask_image = Image.open('mask.png').convert('L')  # Converting mask to grayscale

mask_image = mask_image.resize(input_image.size)

background_color = (255, 255, 255) 

background_image = Image.new('RGB', input_image.size, background_color) # Creating a new image with the background color

result_image = Image.composite(input_image, background_image, mask_image) # Applying the mask to composite the input image onto the background image

result_image.save('result.jpg')
