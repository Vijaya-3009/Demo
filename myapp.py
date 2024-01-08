import streamlit as st
st.set_page_config(page_title='Demon Slayer')
st.header("Main Lead")
col1,col2=st.columns(2)
with col1:
  st.subheader("Tanjiro Kamado")
  st.image("./Tanjiro.jpg", caption="Tanjiro Kamado", width=300,use_column_width=True)
  st.write("Tanjiro Kamado is a Demon Slayer")
with col2:
  st.subheader("Nezuko Kamado")
  st.image("./nezuko.jpg", caption="Nejuko Kamado", width=300,use_column_width=True)
  st.write("Nezuko Kamado is a Demon")
        
          
