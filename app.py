import streamlit as st
import pandas as pd
from logic import compatible_tenants
from helpers import generate_compatibility_graph, generate_compatibility_table, get_tenant_ids

# Configure the page to use a wider layout.
st.set_page_config(layout="wide")

result = None

# Display a large image at the top.
st.image('./Media/cover.png', use_column_width=True)

# Insert a vertical space of 60px
st.markdown(f'<div style="margin-top: 60px;"></div>', unsafe_allow_html=True)

# Configure the sidebar with inputs and a button.
with st.sidebar:
    st.header("Who is already living in the apartment?")
    tenant1 = st.text_input("Tenant 1")
    tenant2 = st.text_input("Tenant 2")
    tenant3 = st.text_input("Tenant 3")
    
    num_roommates = st.text_input("How many new roommates do you want to find?")
    
    if st.button('SEARCH FOR NEW ROOMMATES'):
        # Verify that the number of roommates is a valid value
        try:
            topn = int(num_roommates)
        except ValueError:
            st.error("Please enter a valid number for the number of roommates.")
            topn = None
        
        # Get the tenant identifiers using the function
        tenant_ids = get_tenant_ids(tenant1, tenant2, tenant3, topn)
        if tenant_ids and topn is not None:
            # Call the compatible_tenants function with the corresponding parameters
            result = compatible_tenants(tenant_ids, topn)

# Check if 'result' contains an error message (string)
if isinstance(result, str):
    st.error(result)
# If not, and if 'result' is not None, display the bar graph and table
elif result is not None:
    cols = st.columns((1, 2))  # Divide the layout into 2 columns
    
    with cols[0]:  # This makes the graph and its title appear in the first column
        st.write("Compatibility level of each new roommate:")
        fig_graph = generate_compatibility_graph(result[1])
        st.pyplot(fig_graph)
    
    with cols[1]:  # This makes the table and its title appear in the second column
        st.write("Comparison between roommates:")
        fig_table = generate_compatibility_table(result)
        st.plotly_chart(fig_table, use_container_width=True)

