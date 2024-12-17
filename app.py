import streamlit as st
import gseapy as gp
import pandas as pd
import matplotlib.pyplot as plt
import os
import main
# Title and Description
st.title("Gene Enrichment Analysis App")
st.subheader("Created by : Prabhat Tripathi, SysBio@IIITA")
st.write("Enter a list of genes to perform GO and pathway enrichment analysis using GSEAPy.")

# Input Section
genes_input = st.text_area("Enter your genes (one per line):", height=200)
try:
    # Submit Button
    if st.button("Submit"):
        gene_list = [gene.strip() for gene in genes_input.split("\n") if gene.strip()]

    
        Result = main.GO_path(gene_list)
        gene_sets = ['KEGG_2021_Human', 'KEGG_2019_Human', 'Reactome_Pathways_2024', 
                                                                        'WikiPathway_2023_Human', 'GO_Biological_Process_2023', 
                                                                        'GO_Cellular_Component_2023', 'GO_Molecular_Function_2023',
                                                                        'BioCarta_2016', 'Panther_2016', 'DisGeNET', 'Human_Phenotype_Ontology']
    try:
        for geneset in gene_sets:
            st.subheader(geneset)
            result = Result.results[Result.results["Gene_set"]==geneset]
            st.dataframe(result)
            # Convert DataFrame to CSV
            csv_file = result.to_csv(index=False,sep="\t").encode('utf-8')
        
            # Download Button
            st.download_button(
                label="Download Results as CSV",
                data=csv_file,
                file_name=f"{geneset}.txt",
                mime="text/csv"
            )
    except:
        st.write("")
except:
    st.subheader("Error has been occurred, Please try later")