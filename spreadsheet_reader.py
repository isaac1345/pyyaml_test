'''
This maps out the spreadsheet to dictionary relationship.
Once datasets can be populated from the spreadsheet, the dictionary can be used to create the yaml

Referencing one_status_common_datasets.xlsx

'''


# %%

# Create a dict that maps to spreadsheet columns

sample_dict = {"datasets": {
        "id": id_enum,
        "name": "Featureclass_Name(valid characters only)",
        "unique_id": "OBJECTID",
        "adapter_type": "FGDB", # Based on data source, will require logic to interpret
        "datasource": {
            "layer": "Datasource" # The path to the dataset
        },
        "columns": [
            "Fields_to_Summarize",
            "Fields_to_Summarize2",
            "Fields_to_Summarize3",
            "Fields_to_Summarize4",
            "Fields_to_Summarize5",
            "Fields_to_Summarize6",
        ],
        "geom": {
            "geom_column": "GEOMETRY",
            "geom_type": geom_type,
            "crs": 4326
        },
        "operators": [
            "overlay",
            {
                "proximity": {
                "distance": "Buffer_Distance"
                },
            },
        ]
    }
}


