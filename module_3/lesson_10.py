# import re
# import fitz
#
# pdf_file = "python-task.pdf"
# url_regex = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=\n]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
# with fitz.open(pdf_file) as file:
#     for page in file:
#         text = page.get_text()
#         for img in page.get_images():
#             rsm = img[0]
#             image = file.extract_image(rsm)
#             with open(f"{rsm}.{image['ext']}", "wb") as f:
#                 f.write(image["image"])
#     for match in re.finditer(url_regex, text):
#         url = match.group()
#         with open('links.txt', 'a') as f:
#             f.write(url + '\n')
#
#
#
#
#
#
# # time, memory
#
#
#
#
#
#
#
#
#
# import os
# import re
# import fitz
#
# file_path = 'python-task.pdf'
# images_path = '.'
# pdf_file = fitz.open(file_path)
# page_nums = len(pdf_file)
# images_list = []
#
# for page_num in range(page_nums):
#     page_content = pdf_file[page_num]
#     images_list.extend(page_content.get_images())
#
# if len(images_list) == 0:
#     raise ValueError(f'No images found in {file_path}')
#
# for i, image in enumerate(images_list, start=1):
#     xref = image[0]
#     base_image = pdf_file.extract_image(xref)
#     image_bytes = base_image['image']
#     image_ext = base_image['ext']
#     image_name = str(i) + '.' + image_ext
#     with open(os.path.join(images_path, image_name), 'wb') as image_file:
#         image_file.write(image_bytes)
#         image_file.close()
#
# url_regex = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=\n]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
# with fitz.open(file_path) as doc:
#     for page in doc:
#         text = page.get_text()
#         for match in re.finditer(url_regex, text):
#             url = match.group()
#             with open('links.txt', 'a') as f:
#                 f.write(url + '\n')

# version control

# contributor

# private, public
# git (github, gitlab, mercurial, bitbucket)

# commit, branch

'''

git status - git holatini tekshirish
git add .  - git ga barcha fayllarni qo'shish
git add file.txt  - git ga file.txt faylini qo'shish
git add file.txt  - git ga file.txt faylini qo'shish
git pull - olish
git push - yuborish

echo "# p11_group" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/xolmomin/p11_group.git
git push -u origin main

git branch

'''



