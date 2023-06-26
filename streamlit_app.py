import streamlit

streamlit.title('my parents new healthy dinner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & bluberry oatemal')
streamlit.text('kale,s[pinach & Rocket Smoothie')
streamlit.text('Hard-boiled free-range egg')

streamlit.header(' build your own fruit smoothie')
 
import pandas
my_fruit_list =pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("pick some fruits:",list(my_fruit_list.inedx))
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
                                        


