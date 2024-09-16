import os
import re
from PIL import Image, ImageDraw, ImageFont

def get_new_filename(filename):
    # Find the index of ']' or ')'
    match = re.search(r'[)\]]', filename)
    if match:
        index = match.start()
        # Extract the filename starting from the index
        new_filename = filename[index+2:].strip()
        return new_filename
    else:
        return filename

def convert_folders_to_pdf(parent_folder, output_pdf):
    all_images = []
    folder_names = []  # Store folder names with page numbers
    
    try:
        # Get a list of subfolders
        subfolders = [f for f in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, f))]
        
        # If there are no subfolders, process images from the parent folder directly
        if not subfolders:
            subfolders = [parent_folder]
        
        # Keep track of the page number
        page_number = 1
        
        # Iterate through each subfolder
        for folder_name in subfolders:
            folder_path = os.path.join(parent_folder, folder_name)
            image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
            image_files.sort()  # Sort files alphabetically
            
            images = []
            for image_file in image_files:
                image_path = os.path.join(folder_path, image_file)
                images.append(Image.open(image_path))
            
            all_images.extend(images)
            folder_names.append((folder_path, page_number))  # Store folder path with page number
            page_number += len(images)
        
        if all_images:
            # Create PDF
            all_images[0].save(output_pdf, save_all=True, append_images=all_images[1:])
            
            # Add text image with folder names and page numbers
            text_image = Image.new('RGB', (1600, 1200), color='white')
            draw = ImageDraw.Draw(text_image)
            font = ImageFont.truetype("arial.ttf", 48)
            for idx, (folder_path, start_page) in enumerate(folder_names, 1):
                folder_name = os.path.basename(folder_path)  # Extract only the folder name without the full path
                folder_name = get_new_filename(folder_name)  # Get the new filename
                text = f"{idx}. {folder_name[:50]} (Page {start_page})"
                draw.text((40, 40 + idx * 60), text, fill='black', font=font, align='left', spacing=20, stroke_width=0)
            text_image.save(output_pdf, append=True)
            
            print("PDF created successfully!")
        else:
            print("No images found in the provided folders.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

parent_folder = input("inputfolder: ")
output_name = input("outputFileName: ")
output_pdf = rf'C:\Users\sunit\Downloads\OperaBrowser\{output_name}.pdf'
convert_folders_to_pdf(parent_folder, output_pdf)
