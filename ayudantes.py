import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
import streamlit as st

# FUNCTION TO GENERATE THE COMPATIBILITY GRAPH
def generate_compatibility_graph(compatibility):
    compatibility = compatibility / 100  # Ensure it's on a scale of 0 to 1 for percentages
    
    # Configure the Seaborn graph
    fig, ax = plt.subplots(figsize=(5, 4))  # Adjust the graph size as needed
    
    # Create the bar graph with values converted to percentages
    sns.barplot(x=compatibility.index, y=compatibility.values, ax=ax, color='lightblue', edgecolor=None)
    
    # Remove borders
    sns.despine(top=True, right=True, left=True, bottom=False)
    
    # Configure axis labels and rotate x-axis labels
    ax.set_xlabel('Tenant Identifier', fontsize=10)
    ax.set_ylabel('Similarity (%)', fontsize=10)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    
    # Adjust y-axis labels to display percentages correctly
    ax.set_yticklabels(['{:.1f}%'.format(y * 100) for y in ax.get_yticks()], fontsize=8)
    
    # Add percentage labels above each bar
    for p in ax.patches:
        height = p.get_height()
        ax.annotate('{:.1f}%'.format(height * 100),
                    (p.get_x() + p.get_width() / 2., height),
                    ha='center', va='center',
                    xytext=(0, 5),
                    textcoords='offset points', fontsize=8)
    return fig

# FUNCTION TO GENERATE THE ROOMMATES TABLE
def generate_compatibility_table(result):
    # Change the name of the 'index' column and adjust column widths
    result_0_with_index = result[0].reset_index()
    result_0_with_index.rename(columns={'index': 'ATTRIBUTE'}, inplace=True)
    
    # Configure the Plotly table
    fig_table = go.Figure(data=[go.Table(
        columnwidth = [20] + [10] * (len(result_0_with_index.columns) - 1),  # Adjust the first value for the width of the 'ATTRIBUTE' column
        header=dict(values=list(result_0_with_index.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[result_0_with_index[col] for col in result_0_with_index.columns],
                   fill_color='lavender',
                   align='left'))
    ])
    
    # Configure the layout of the Plotly table
    fig_table.update_layout(
        width=700, height=320,  # Adjust as needed
        margin=dict(l=0, r=0, t=0, b=0)
    )
    return fig_table

# FUNCTION TO GENERATE THE LIST OF SEED TENANTS
def get_tenant_ids(tenant1, tenant2, tenant3, topn):
    # Create a list with the entered tenant identifiers and convert them to integers
    tenant_ids = []
    for tenant in [tenant1, tenant2, tenant3]:
        try:
            if tenant:  # If there's any text in the input
                tenant_ids.append(int(tenant))  # Convert to integer and add to the list
        except ValueError:
            st.error(f"The tenant identifier '{tenant}' is not a valid number.")
            tenant_ids = []  # Empty the list if there's an error
            break  # Exit the loop
    return tenant_ids
