import streamlit as st
from PIL import Image

# Use this if you want a backround image
# page_bg_img = '''
# <style>
# body {
# background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");#Put the URL in the quotes
# background-size: cover;
# }
# </style>
# '''
# st.markdown(page_bg_img, unsafe_allow_html=True)


page = st.sidebar.selectbox("What Page Would you Like to Go To",
                            ("==Select==",
                             "Home",
                             "Classes",
                             "Social Media",
                             "About Us"))

if page == "==Select==":
    'Select the page you want to go to in the menu on the left'


elif page == "Home":
    'FHS Computer Club is a club at Franklin High School in Massachussetts'
    '\n\n\nWe build many different projects and teach others about computer skills such as programming'
    'Go to the classes tab to see more!'


elif page == "Classes":
    "FHS Computer Club offers MANY classes to take"
    "Click on the checkboxes for time, date, and  more"

    if st.checkbox("Python"):

        st.write(''' #Python
        Ah, so your interested in Python. No? Well, let me tell you about the possiblilities of Python.
        This website here, its built completely in Python. Python can do so much more, with a library for almost anything
        you can think of

        The classes will start as soon as enough people register, and the date/time will be decided then

        Instructor: Arav Tyagi(Treasurer, programmer of this website)'''
        )

# elif page == "Social Media":
#     st.markdown()
# image = Image.open('pictureName.jpg')
# st.image(image, width=200,
#          se_column_width=True)
