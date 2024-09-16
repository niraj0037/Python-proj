from PIL import Image, ImageDraw, ImageFont
import os

def convert_folders_to_pdf(parent_folder, output_pdf):
    all_images = []
    folder_names = []  # Store folder names
    
    try:
        # Get a sorted list of subfolders
        subfolders = sorted(os.listdir(parent_folder))
        
        # Iterate through each sorted subfolder
        for index, folder_name in enumerate(subfolders, 1):
            folder_path = os.path.join(parent_folder, folder_name)
            if os.path.isdir(folder_path):
                image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
                image_files.sort()  # Sort files alphabetically
                
                images = []
                for image_file in image_files:
                    image_path = os.path.join(folder_path, image_file)
                    images.append(Image.open(image_path))
                
                all_images.extend(images)
                folder_names.append(f"{index}. {folder_name}")  # Store folder name
        
        if all_images:
            # Create PDF
            all_images[0].save(output_pdf, save_all=True, append_images=all_images[1:])
            
            # Add text image with folder names
            text_image = Image.new('RGB', (1600, 1200), color='white')
            draw = ImageDraw.Draw(text_image)
            font = ImageFont.truetype("arial.ttf", 48)
            text = "\n".join(folder_names)
            draw.text((40, 40), text, fill='black', font=font, align='left', spacing=20, stroke_width=0)
            text_image.save(output_pdf, append=True)
            
            print("PDF created successfully!")
        else:
            print("No images found in the provided folders.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
parent_folder = r'C:\Users\sunit\Downloads\2'
output_pdf = r'C:\Users\sunit\Downloads\OperaBrowser\Cee_all_folders_output.pdf'
convert_folders_to_pdf(parent_folder, output_pdf)
