import streamlit as st  
import pandas as pd  
import time  
  
def load_csv():  
    csv_file = st.file_uploader("Upload CSV", type=['csv'])  
    if csv_file is not None:  
        data = pd.read_csv(csv_file)  
        st.success('Loading completed!')  
        st.dataframe(data) # Use st.dataframe instead of st.write for better formatting  
  
def main():  
    st.title("CSV File Upload and Display")  
    st.write("Welcome to this simple Streamlit app. Please upload your CSV file.")  
    with st.spinner('Loading data...'):  
        load_csv()  
  
if __name__ == "__main__":  
    main()  