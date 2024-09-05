import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide", initial_sidebar_state='collapsed')
# st.set_page_config('Hello Forum',initial_sidebar_state='collapsed')


# ------ Header Section -----
with st.container():
    st.subheader("Hi, I am Aleena :wave:")
    st.title("3D Generalist")
    st.write("I am a passionate 3D Artist")
    st.write("[Learn More >](https://pythonandvba.com)")

# ----- WHAT I DO -----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        # st.write("######")
        st.write(
            """
            Here are some of the things I specialize in:
            - 3D Modeling
            - Texturing
            - Rigging
            - Animation
            """
        )
        st.write("I love bringing ideas to life through 3D art!")
    with right_column:
        st.image("https://via.placeholder.com/300", caption="3D Work Example")




# ----Adding projects-----

with st.container():

    st.write("---")
    row1 = st.columns(3)

    with row1[0]:

        tile = st.container()
        tile.markdown(
            """
            <div style="background-color: #4682B4; padding: 100px; border-radius: 5px;">
                <h2 style="color: white; text-align: center;">Animation</h2>
                <p style="color: white; text-align: center;">Explore amazing animations here!</p>

            </div>
            """,
            unsafe_allow_html=True

        )
        # tile.title("Motion Graphics")
        tile.page_link("pages/motion.py", label="see more")
        # ("Go to [motion](motion)")

    with row1[1]:
        tile = st.container()
        tile.markdown(
            """
            <style>
            .hover-container {
                background-color: #4682B4;
                padding: 20px;
                border-radius: 10px;
                height: 300px;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .hover-container:hover {
                transform: scale(1.05);
                box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
            }
            .hover-container h2, .hover-container p {
                color: white;
                text-align: center;
            }
            .hover-container a {
                display: inline-block;
                padding: 10px 20px;
                background-color: white;
                color: #4682B4;
                text-decoration: none;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
            }
            </style>
            <div class="hover-container">
                <h2>Graphic Designer</h2>
                <p>Explore creative designs and projects!</p>
                <a href="?page=graphic">See more</a>
            </div>
            """,
            unsafe_allow_html=True
        )




    with row1[2]:
        tile = st.container(height=300)
        tile.title("Graphic Designer")
        tile.page_link("pages/graphic.py", label="see more")



with st.container():
    st.write("---")


