### Modeling
![modeling_image](https://github.com/MayHyeyeonKim/likelion2023/blob/main/LIONGRAM/django_LIONGRAM_modeling.JPG?raw=true)

**Solution:**
You can describe your modeling solution here.

### Trouble Shooting

#### 1
![Pillow_Err](https://github.com/MayHyeyeonKim/likelion2023/blob/main/LIONGRAM/images/pillowErr.png?raw=true)

**Solution:**
python3 -m pip install Pillow

#### 2
![CSRF_Err](https://github.com/MayHyeyeonKim/likelion2023/blob/main/LIONGRAM/images/CSRFErr.png?raw=true)

**Solution:**
 - added {% csrf_token %} to post_form.html as shown in the image below.
 ![CSRF_Err](https://github.com/MayHyeyeonKim/likelion2023/blob/main/LIONGRAM/images/CSRFErrSolution.png?raw=true)
