# Udemy100-1
Python -- Udemy -- 100 Projects in 100 Days 

# Repo Purpose
Whilst learning Python, will use this repo to also practice Git / Github

# Python 3.13 TCL move issue
Upgrading from 3.12 to 3.13 presented errors when using tkinter library
Specifcally it was looking for it in a Python313/lib folder
However it appears to have moved to Python313/tcl836 folder
If experiencing this set Environment Variables as follows to change the pointer:

1. Open **Environment Variables** from win search bar.
2. Create a new **System variable** with:
   - **Variable name**: `TCL_LIBRARY`
   - **Variable value**: `C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python313\tcl\tcl8.6`
3. Restart your terminal or IDE.
