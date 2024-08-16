# Roommate Compatibility Finder

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.24.0-FF4B4B.svg)](https://streamlit.io)
[![Pandas](https://img.shields.io/badge/pandas-1.5.3-150458.svg)](https://pandas.pydata.org)
[![NumPy](https://img.shields.io/badge/numpy-1.23.5-013243.svg)](https://numpy.org)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.2.2-F7931E.svg)](https://scikit-learn.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7.1-11557c.svg)](https://matplotlib.org)
[![Seaborn](https://img.shields.io/badge/seaborn-0.12.2-76678C.svg)](https://seaborn.pydata.org)
[![Plotly](https://img.shields.io/badge/plotly-5.14.1-3F4F75.svg)](https://plotly.com)

## Overview
This project is a web application that leverages data analysis and machine learning techniques to identify compatible roommates based on personal attributes and preferences.


## Techniques and Concepts

### Data Processing
- Data loading and manipulation with Pandas
- Categorical data preprocessing using One-Hot Encoding

### Similarity Analysis
- Creation of a similarity matrix using dot product of encoded vectors
- Value rescaling for improved interpretation

### Recommendation System
- Implementation of a similarity-based recommendation system for roommate matching

### Data Visualization
- Generation of bar charts to display compatibility levels
- Creation of interactive tables for comparing roommate attributes

### User Interface Development
- Design of an interactive user interface with Streamlit
- Implementation of widgets for data input and result visualization

### Code Modularization
- Organization of code into separate modules for improved maintainability and reusability

## Project Structure

- `app.py`: Main Streamlit application
- `ayudantes.py`: Helper functions for graph and table generation
- `logica.py`: Core logic for data processing and compatibility matching
- `dataset_inquilinos.csv`: Dataset containing roommate information (not included in shared documents)

## Technical Highlights

1. **Data Preprocessing**: Utilization of One-Hot Encoding for categorical data transformation.

2. **Similarity Calculation**: Implementation of dot product calculations for creating a similarity matrix.

3. **Data Rescaling**: Application of min-max scaling to normalize similarity scores.

4. **Data Visualization**: 
   - Creation of bar plots using Seaborn for compatibility visualization.
   - Development of interactive tables with Plotly for detailed attribute comparison.

5. **Web Application Development**: Integration of data processing, analysis, and visualization into a Streamlit web application.

This project demonstrates the application of modern Python technologies in data processing, similarity analysis, data visualization, and interactive web application development.
