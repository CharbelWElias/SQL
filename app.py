# Core Pkgs
import streamlit as st 
import pandas as pd

# DB Mgmt
import sqlite3 
conn = sqlite3.connect('admission.sqlite')
c = conn.cursor()


# Fxn Make Execution
def sql_executor(raw_code):
	c.execute(raw_code)
	data = c.fetchall()
	return data 


Admission = ['Serial No', 'GRE Score', 'TOEFL Score', 'SOP', 'LOR', 'CGPA', 'University Rating', 'Research', 'Admission Chance']




def main():
	st.title("SQLPlayground")
	

	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("HomePage")

		# Columns/Layout
		col1,col2 = st.columns(2)

		with col1:
			with st.form(key='query_form'):
				raw_code = st.text_area("SQL Code Here")
				submit_code = st.form_submit_button("Execute")

			# Table of Info

			with st.expander("Table Info"):
				table_info = {'Admission':Admission}
				st.json(table_info)
			
		# Results Layouts
		with col2:  
			if submit_code:
				st.info("Query Submitted")
				st.code(raw_code)

				# Results 
				query_results = sql_executor(raw_code)
				with st.expander("Results"):
					st.write(query_results)

				with st.expander("Pretty Table"):
					query_df = pd.DataFrame(query_results)
					st.dataframe(query_df)


	else:
		st.subheader("About")





if __name__ == '__main__':
	main()

