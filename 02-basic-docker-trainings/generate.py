import os

image_folder = "images"
readme_filename = "README.md"

def generate_readme(image_folder, readme_filename):
    images = sorted([img for img in os.listdir(image_folder) if img.endswith('.png')])
    
    readme_content = ""
    for i, img_name in enumerate(images, start=1):
        readme_content += f"{i}. Zrzut ekranu numer {i}:\n![{i}](images/{img_name})\n\n"
    
    with open(readme_filename, "w") as readme_file:
        readme_file.write(readme_content)
    
    print(f"Plik '{readme_filename}' został wygenerowany z {len(images)} zrzutami ekranu.")

generate_readme(image_folder, readme_filename)

