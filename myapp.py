import streamlit as st
st.set_page_config(page_title='Demon Slayer')
st.header("メインリード")
col1,col2,col3=st.columns(3)
with col1:
  st.subheader("竈門 炭治郎")
  st.image("./Tanjiro.jpg", caption="Tanjiro Kamado", width=300,use_column_width=True)
  st.write("Tanjiro Kamado is a Demon Slayer")
with col2:
  st.subheader("竈門 禰豆子")
  st.image("./nezuko.jpg", caption="Nejuko Kamado", width=300,use_column_width=True)
  st.write("Nezuko Kamado is a Demon")
with col3:
  st.subheader("炭治郎と鬼との戦い")
  st.image("./Tanjiro.gif", caption="Tanjiro fight", width=300,use_column_width=True)
  st.write("Tanjiro's fight with blood moon")
        
          
