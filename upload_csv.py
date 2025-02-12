# import streamlit as st  
# import pandas as pd  
# import time  
  
# def load_csv():  
#     csv_file = st.file_uploader("Upload CSV", type=['csv'])  
#     if csv_file is not None:  
#         data = pd.read_csv(csv_file)  
#         st.success('Loading completed!')  
#         st.dataframe(data) # Use st.dataframe instead of st.write for better formatting  
  
# def main():  
#     st.title("CSV File Upload and Display")  
#     st.write("Welcome to this simple Streamlit app. Please upload your CSV file.")  
#     with st.spinner('Loading data...'):  
#         load_csv()  
  
# if __name__ == "__main__":  
#     main()  

import streamlit as st  
import pandas as pd  
import networkx as nx  
import matplotlib.pyplot as plt  
  
def load_csv():  
    csv_file = st.file_uploader("Upload CSV", type=['csv'])  
    if csv_file is not None:  
        data = pd.read_csv(csv_file)  
        st.success('Loading completed!')  
        st.dataframe(data) # Use st.dataframe instead of st.write for better formatting  
        return data  
  
def draw_hierachy(data):  
    if 'EMPLOYEE_ID' in data.columns and 'MANAGER_ID' in data.columns:  
        # Create directed graph  
        G = nx.from_pandas_edgelist(data, 'EMPLOYEE_ID', 'MANAGER_ID', create_using=nx.DiGraph())  
          
        # Draw the graph  
        pos = nx.spring_layout(G)  
        nx.draw(G, pos, with_labels=True, arrows=True)  
        st.pyplot()  
  
def main():  
    st.title("CSV File Upload and Display")  
    st.write("Welcome to this simple Streamlit app. Please upload your CSV file.")  
    data = None  
    with st.spinner('Loading data...'):  
        data = load_csv()  
    if data is not None:  
        draw_hierachy(data)  
  
if __name__ == "__main__":  
    main()  