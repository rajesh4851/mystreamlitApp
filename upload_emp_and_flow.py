# import streamlit as st  
# import pandas as pd  
# import graphviz as gv  
  
# def load_csv():  
#     csv_file = st.file_uploader("Upload CSV", type=['csv'])  
#     if csv_file is not None:  
#         data = pd.read_csv(csv_file)  
#         st.success('Loading completed!')  
#         st.dataframe(data) # Use st.dataframe instead of st.write for better formatting  
#         return data  
  
# def draw_flow(data):  
#     if 'EMPLOYEE_ID' in data.columns and 'MANAGER_ID' in data.columns:  
#         # Create directed graph  
#         dot = gv.Digraph()  
#         for index, row in data.iterrows():  
#             dot.edge(str(row['MANAGER_ID']), str(row['EMPLOYEE_ID']))  
#         st.graphviz_chart(dot.source)  
  
# def main():  
#     st.title("CSV File Upload and Display")  
#     st.write("Welcome to this simple Streamlit app. Please upload your CSV file.")  
#     data = None  
#     with st.spinner('Loading data...'):  
#         data = load_csv()  
#     if data is not None:  
#         draw_flow(data)  
  
# if __name__ == "__main__":  
#     main()  


import streamlit as st  
import pandas as pd  
import graphviz as gv  
  
def load_csv():  
    csv_file = st.file_uploader("Upload CSV", type=['csv'])  
    if csv_file is not None:  
        data = pd.read_csv(csv_file)  
        st.success('Loading completed!')  
        st.dataframe(data)  # Use st.dataframe instead of st.write for better formatting  
        return data  
  
def draw_flow(data):  
    if 'EMPLOYEE_ID' in data.columns and 'MANAGER_ID' in data.columns:  
        # Create directed graph  
        dot = gv.Digraph(format='svg')  
  
        for index, row in data.iterrows():  
            # Add nodes with custom attributes  
            dot.node(str(row['EMPLOYEE_ID']), shape='oval', color='blue', style='filled', fillcolor='lightblue')  
            dot.node(str(row['MANAGER_ID']), shape='box', color='black')  
  
            # Add edges with custom attributes  
            dot.edge(str(row['MANAGER_ID']), str(row['EMPLOYEE_ID']), color='red')  
  
        st.graphviz_chart(dot.source)  
  
def main():  
    st.title(" Employee Hierarchy Visualizer from CSV")  
    st.write("Welcome to this simple employee visualization app. Please upload your CSV file.")  
    data = None  
    with st.spinner('Loading data...'):  
        data = load_csv()  
    if data is not None:  
        draw_flow(data)  
  
if __name__ == "__main__":  
    main()  