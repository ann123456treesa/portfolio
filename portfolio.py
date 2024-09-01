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
        tile = st.container(height=300)
        tile.title("Motion Graphics")
        tile.page_link("pages/motion.py", label="see more")
        # ("Go to [motion](motion)")

    with row1[1]:
        tile = st.container(height=300)
        tile.title("Animation")
        tile.page_link("pages/animation.py", label="see more")

    # with row1[2]:
    #     tile = st.container(height=300)
    #     tile.title("Grpahic design")
    #     tile.markdown("read more [graphic](graphic)")

    with row1[2]:
        tile = st.container(height=300)
        tile.title("Graphic Designer")
        tile.page_link("pages/graphic.py", label="see more")



