from PIL import Image

try:
    img = Image.open('image/test2.jpg')
    print("Image opened success")

    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            pixel_value = pixels[x,y]

            if img.mode == 'L': # Nếu là ảnh trắng đen (Grayscale)
                inverted_value = 255 - pixel_value
                pixels[x, y] = inverted_value # Gán giá trị đã đảo ngược trở lại pixel

            elif img.mode == 'RGB': # Nếu là ảnh màu RGB
                r, g, b = pixel_value # Tách các kênh màu
                inverted_r = 255 - r
                inverted_g = 255 - g
                inverted_b = 255 - b
                pixels[x, y] = (inverted_r, inverted_g, inverted_b) # Gán tuple màu mới cho pixel
            
            # Bạn có thể thêm các chế độ màu khác (ví dụ: 'RGBA' nếu ảnh có kênh alpha)
            else:
                # Nếu gặp chế độ màu không xác định, có thể bỏ qua hoặc báo lỗi
                print(f"Chế độ màu {img.mode} không được hỗ trợ để đảo ngược.")
                break # Thoát vòng lặp ngoài
    
    inverted_image_name = 'image_sl/test2_inverted.png' # Đặt tên file mới
    img.save(inverted_image_name)
    print(f"Đã tạo ảnh đảo màu và lưu thành '{inverted_image_name}'")
    img.show()

except FileNotFoundError:
    print("Lỗi: Không tìm thấy tệp ảnh. Vui lòng đảm bảo tệp ảnh có cùng thư mục với script hoặc đường dẫn đã đúng.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")