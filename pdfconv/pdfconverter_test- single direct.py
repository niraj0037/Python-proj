from PIL import Image
import os

def convert_images_to_pdf(folder_path, output_pdf):
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    image_files.sort()  # Sort files alphabetically
    
    images = []
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        images.append(Image.open(image_path))
    
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    print("PDF created successfully!")
    
    # Delete individual image files that were converted to PDF
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        pdf_created = image_file.replace(image_file[image_file.find('.'):], ".pdf")
        if pdf_created == os.path.basename(output_pdf):
            os.remove(image_path)
            print(f"{image_file} deleted successfully!")
    # print("Individual image files converted to PDF and deleted successfully!")

# Example usage:
folder_path = r'C:\Users\sunit\Downloads\2\abcd'
output_folder = r'C:\Users\sunit\Downloads\OperaBrowser'
output_pdf = os.path.join(output_folder, "output.pdf")
convert_images_to_pdf(folder_path, output_pdf)
