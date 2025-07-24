import os
from PIL import Image, ImageFilter # Import thêm ImageFilter nếu muốn làm mờ
import glob

# Định nghĩa thư mục chứa các ảnh của bạn
# Giả sử thư mục 'my_image_dataset' nằm cùng cấp với file .py này
image_folder = 'my_image_dataset'

# Đảm bảo thư mục đầu ra tồn tại
output_folder = 'processed_images'
os.makedirs(output_folder, exist_ok=True) # Tạo thư mục nếu chưa có (có thể tạo Folder ở ngoài và bỏ dòng này đi)

print(f"Đang tìm kiếm ảnh trong thư mục: {image_folder}")

# 1. Sử dụng glob để tìm tất cả các tệp .jpg và .png trong thư mục
all_image_paths = []
############ CÁCH NÀY DÙNG ĐỂ QUÉT ĐÚNG 1 LOẠI FILE DUY NHẤT CÓ TRONG LIST ẢNH 'my_image_dataset'##############

# pattern = os.path.join(image_folder, '**', '*.jpg') # Loại file .jpg, nếu các loại khác thì đặt khác
# all_image_paths = (glob.glob(pattern, recursive=True))

# Bạn có thể dùng list để chứa các loại file
############ CÁCH NÀY DÙNG ĐỂ QUÉT HẾT TẤT CẢ CÁC LOẠI FILE CÓ TRONG LIST 'my_image_dataset'################
image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif']
for ext in image_extensions:
    # **/*{ext} sẽ tìm kiếm trong tất cả các thư mục con của image_folder
    # Lưu ý: cần truyền recursive=True khi dùng **
    pattern = os.path.join(image_folder, '**', ext) 
    all_image_paths.extend(glob.glob(pattern, recursive=True))

if not all_image_paths:
    print(f"Không tìm thấy bất kỳ ảnh nào trong '{image_folder}' với các định dạng đã cho.")
else:
    print(f"Tìm thấy {len(all_image_paths)} ảnh:")
    for image_path in all_image_paths:
        print(f"- {image_path}")

    print("\n--- Bắt đầu xử lý ảnh ---")
    for img_path in all_image_paths:
        try:
            # 2. Mở từng ảnh bằng Pillow
            img = Image.open(img_path)
            print(f"\nĐang xử lý ảnh: {img_path}")

            # Lấy tên file và đuôi file để đặt tên cho ảnh đã xử lý
            base_name = os.path.basename(img_path) # Lấy 'my_image.png'
            name, ext = os.path.splitext(base_name) # Tách thành 'my_image' và '.png'

            # 3. Thực hiện một vài thao tác xử lý ảnh (ví dụ: chuyển grayscale và làm mờ)
            
            # Chuyển grayscale
            img_gray = img.convert('L')
            output_gray_path = os.path.join(output_folder, f"{name}_grayscale.png")
            img_gray.save(output_gray_path)
            print(f"  -> Đã lưu ảnh grayscale: {output_gray_path}")

            # Làm mờ (Gaussian Blur)
            img_blurred = img.filter(ImageFilter.GaussianBlur(radius=3))
            output_blurred_path = os.path.join(output_folder, f"{name}_blurred.png")
            img_blurred.save(output_blurred_path)
            print(f"  -> Đã lưu ảnh mờ: {output_blurred_path}")

        except FileNotFoundError:
            print(f"Lỗi: Không tìm thấy tệp '{img_path}'.")
        except Exception as e:
            print(f"Lỗi khi xử lý ảnh '{img_path}': {e}")

    print("\n--- Hoàn tất xử lý tất cả ảnh ---")