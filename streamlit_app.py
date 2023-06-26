import streamlit

streamlit.title('my parents new healthy dinner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & bluberry oatemal')
streamlit.text('kale,s[pinach & Rocket Smoothie')
streamlit.text('Hard-boiled free-range egg')

streamlit.header(' build your own fruit smoothie')

 ///pandas 
import pandas
my_fruit_list =pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
