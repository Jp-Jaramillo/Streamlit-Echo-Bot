import streamlit as st


st.title("JuanJaramillo_Echo Bot")
with st.chat_message("assistant"):
    st.image("DashboardPowerBi.png", caption="CIT 144 – Demographics Data Visualization")



# initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# react to user input
if prompt := st.chat_input("What is up?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    #display assistant response in chat message container
    response = f"Echo: {prompt}"

    # add assistant response to message history
    with st.chat_message("assistant"):
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
