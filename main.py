import gseapy
import pandas as pd
def GO_path(gene):
    Results = gseapy.enrichr(gene_list=gene, gene_sets = ['KEGG_2021_Human', 'KEGG_2019_Human', 'Reactome_Pathways_2024', 
                                                                'WikiPathway_2023_Human', 'GO_Biological_Process_2023', 
                                                                'GO_Cellular_Component_2023', 'GO_Molecular_Function_2023',
                                                                'BioCarta_2016', 'Panther_2016', 'DisGeNET', 'Human_Phenotype_Ontology'
                                                            ])

    
    return Results