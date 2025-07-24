# from PIL import Image
# from PIL import ImageFilter

# try:
#     img = Image.open('image/example.jpg')
#     #img.show()
#     print("Image opened success")
#     print(f"Image size: {img.size}")

#     img_gray = img.convert('L')
#     img_gray.save('image_sl/example_gray.png')
#     print("Gray_image coverted success")

#     img_blur = img_gray.filter(ImageFilter.BLUR)
#     img_blur.save('image_sl/example_blur.png')
#     print("Blur_image coverted success")

# except FileNotFoundError:
#     print("File not found !!!")
# except Exception as e:
#     print(f"Don't open file {e}")

import glob

txt_files = glob.glob('image_sl/*.png')
print(f"Các file .txt trong thư mục hiện tại: {txt_files}")