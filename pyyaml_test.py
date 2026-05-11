'''
Test of writing a yaml 
must install pyyaml to use

https://stackoverflow.com/questions/12470665/how-can-i-write-data-in-yaml-format-in-a-file
d = {'A':'a', 'B':{'C':'c', 'D':'d', 'E':'e'}}
with open('result.yml', 'w') as yaml_file:
    yaml.dump(d, yaml_file, default_flow_style=False)


'''

# %%
import yaml

# %%

sample_dict = {"datasets": {
        "id": 0,
        "name": None,
        "unique_id": "OBJECTID",
        "adapter_type": "FGDB",
        "datasource": {
            "layer": None
        },
        "columns": [
            None,
        ],
        "geom": {
            "geom_column": "GEOMETRY",
            "geom_type": "point",
            "crs": 4326
        },
        "operators": [
            "overlay",
            {
                "proximity": {
                "distance": 100
                },
            },
        ]
    }
}

with open('result.yml', 'w') as yaml_file:
    yaml.dump(sample_dict, yaml_file, default_flow_style=False)
# %%
