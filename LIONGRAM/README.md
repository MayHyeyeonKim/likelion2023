# LIKELION - LIONGRAM

LIONGRAM is a Django-based clone of Instagram.

---
## Modeling
![modeling_image](https://github.com/MayHyeyeonKim/likelion2023/blob/main/LIONGRAM/django_LIONGRAM_modeling.JPG?raw=true)

**Description:**
This image illustrates the modeling process for the LIONGRAM application.
<br>
---

## Troubleshooting

#### [1] Pillow-related errors
![Pillow_Err](https://github.com/MayHyeyeonKim/likelion2023/blob/main/LIONGRAM/images/pillowErr.png?raw=true)

**Solution:**
Pillow is a Python image processing library used for opening, manipulating, saving, and performing various image operations. One of the reasons Pillow errors occur is the absence or improper configuration of the Pillow library.

A solution to resolve Pillow errors is to install Pillow by running the following command: **"python3 -m pip install Pillow."**

This library is commonly used in Python projects that involve image processing and manipulation.
<br>
<br>
#### [2] CSRF-related errors
![CSRF_Err](https://github.com/MayHyeyeonKim/likelion2023/blob/main/LIONGRAM/images/CSRFErr.png?raw=true)

**Solution:**
CSRF stands for Cross-Site Request Forgery, an attack that involves executing malicious web requests with the authority of an authenticated user. To mitigate this, we used CSRF tokens as a solution.

As a solution, "added {% csrf_token %} to post_form.html as shown in the image below."
 ![CSRF_Err](https://github.com/MayHyeyeonKim/likelion2023/blob/main/LIONGRAM/images/CSRFErrSolution.png?raw=true)
