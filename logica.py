# 1. SETUP
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# 2. DATA LOADING
df = pd.read_csv('tenants_dataset.csv', index_col='tenant_id')
df.columns = [
    'schedule', 'biorhythm', 'education_level', 'reading', 'animation', 
    'cinema', 'pets', 'cooking', 'sports', 'diet', 'smoker',
    'visits', 'tidiness', 'music_type', 'loud_music', 'perfect_plan', 'instrument'
]

# 3. ONE HOT ENCODING
# Perform one-hot encoding
encoder = OneHotEncoder()
df_encoded = encoder.fit_transform(df)
df_encoded_dense = df_encoded.toarray()  # Convert to dense array

# Get the names of encoded variables after performing one-hot encoding
encoded_feature_names = encoder.get_feature_names_out()

# 4. SIMILARITY MATRIX
# Calculate the similarity matrix using dot product, ensuring to use dense data
similarity_matrix = np.dot(df_encoded_dense, df_encoded_dense.T)  # Use dense data for calculation

# Define the target range
range_min = -100
range_max = 100

# Find the minimum and maximum values in similarity_matrix
min_original = np.min(similarity_matrix)
max_original = np.max(similarity_matrix)

# Rescale the matrix
rescaled_similarity_matrix = ((similarity_matrix - min_original) / (max_original - min_original)) * (range_max - range_min) + range_min

# Convert to Pandas
df_similarity = pd.DataFrame(rescaled_similarity_matrix,
                             index=df.index,
                             columns=df.index)

# 5. SEARCH FOR COMPATIBLE TENANTS
'''
Input:
* tenant_ids: the current tenant(s) MUST BE A LIST even if it's just one data point
* topn: the number of compatible tenants to search for
Output:
List with 2 elements.
Element 0: the characteristics of compatible tenants
Element 1: the similarity data
'''
def find_compatible_tenants(tenant_ids, topn):
    # Check if all tenant IDs exist in the similarity matrix
    for tenant_id in tenant_ids:
        if tenant_id not in df_similarity.index:
            return 'At least one of the tenants not found'
    
    # Get the rows corresponding to the given tenants
    tenant_rows = df_similarity.loc[tenant_ids]
    
    # Calculate the average similarity between tenants
    average_similarity = tenant_rows.mean(axis=0)
    
    # Sort tenants based on their average similarity
    similar_tenants = average_similarity.sort_values(ascending=False)
    
    # Exclude reference tenants (those in the list)
    similar_tenants = similar_tenants.drop(tenant_ids)
    
    # Take the topn most similar tenants
    topn_tenants = similar_tenants.head(topn)
    
    # Get the records of similar tenants
    similar_records = df.loc[topn_tenants.index]
    
    # Get the records of searched tenants
    searched_records = df.loc[tenant_ids]
    
    # Concatenate searched records with similar records in columns
    result = pd.concat([searched_records.T, similar_records.T], axis=1)
    
    # Create a Series object with the similarity of found similar tenants
    similarity_series = pd.Series(data=topn_tenants.values, index=topn_tenants.index, name='Similarity')
    
    # Return the result and the Series object
    return (result, similarity_series)

