import streamlit as st

st.set_page_config(page_title="Secret Letter 💌", page_icon="💌")

st.title("You Got a Letter 💌")

st.write("Click the envelope to open your secret message 👇")

# Letter button
if st.button("💌 CLICK ME", use_container_width=True):
    st.success("I Love You ❤️")
    st.balloons()
