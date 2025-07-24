from PIL import Image
from PIL import ImageFilter

try:
    img = Image.open('image/my_image.png')
    img.show()
    print("Image opened success")
    
    img_gray = img.convert('L')
    img_gray.save('image_sl/my_image_grayscale.png')
    print("Image converted success")
    img_gray.show()

    img_blur_1 = img.filter(ImageFilter.BLUR)
    img_blur_1.save('image_sl/my_image_blurred_1.png')
    print("Image filtered success")
    img_blur_1.show()

    img_blur_2 = img_gray.filter(ImageFilter.GaussianBlur(radius=2))
    img_blur_2.save('image_sl/my_image_blurred_2.png')
    print("Image filtered success")
    img_blur_2.show()

except FileNotFoundError:
    print("Lỗi: Không tìm thấy tệp ảnh. Vui lòng đảm bảo tệp ảnh có cùng thư mục với script hoặc đường dẫn đã đúng.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
