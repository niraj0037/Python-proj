from PIL import Image
import os

def convert_folders_to_pdf(parent_folder, output_pdf):
    all_images = []
    
    try:
        # Get a sorted list of subfolders
        subfolders = sorted(os.listdir(parent_folder))
        
        # Iterate through each sorted subfolder
        for folder_name in subfolders:
            folder_path = os.path.join(parent_folder, folder_name)
            if os.path.isdir(folder_path):
                image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
                image_files.sort()  # Sort files alphabetically
                
                images = []
                for image_file in image_files:
                    image_path = os.path.join(folder_path, image_file)
                    images.append(Image.open(image_path))
                
                all_images.extend(images)
        
        if all_images:
            all_images[0].save(output_pdf, save_all=True, append_images=all_images[1:])
            print("PDF created successfully!")
        else:
            print("No images found in the provided folders.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
parent_folder = r'C:\Users\sunit\Downloads\2'
output_pdf = r'C:\Users\sunit\Downloads\OperaBrowser\333C_all_folders_output.pdf'
convert_folders_to_pdf(parent_folder, output_pdf)
