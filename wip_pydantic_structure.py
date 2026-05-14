# Last modified 20260514 BMANG
# work-in-progress using pydantic to for data validation

from typing import Annotated, Literal, Optional

from annotated_types import Gt

from pydantic import BaseModel, SecretStr, StringConstraints, ValidationError
print("imports complete")

class SomeGeometry(BaseModel):
    # string input
    geom_column: str
    # multipart needed? curve?
    # input is point, line, polygon
    # TO-DO make case insensitive?
    geom_type: Literal["point", "line", "polygon"]
    # integer input greater than 0
    crs: Annotated[int, Gt(0)]

class SomeOperators(BaseModel):
    # input is adjacent, buffer, overlay, proximity
    # TO-DO make case insensitive?
    operators: Literal["adjacent", "buffer", "overlay", "proximity"]

class OperatorDistance(BaseModel):
    # optional, float input greater than 0
    distance: Optional[Annotated[float, Gt(0)]] = None

class SomeName(BaseModel):
    # should this be uuid?
    # integer input
    id: int
    # string input
    name: str
    # integer input
    unique_id: str
    # input is fgdb, kml, oracle, shp
    # TO-DO make case insensitive?
    adapter_type: Literal["fgdb", "kml", "oracle", "shp"]
    # SecretStr for UNC paths?
    # dict input
    datasource: dict[str, SecretStr]
    # optional, list of string input
    columns: Optional[list[str]] = None
    # optional, string input
    definition: Optional[str] = None
    # class / object input
    geom: SomeGeometry

sample_dict = {
    "id": 0,
    "name": "Featureclass_Name",
    "unique_id": "OBJECTID",
    "adapter_type": "FGDB",
    "datasource": {
        "layer": "Datasource"
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
        "geom_type": "point",
        "crs": 4326
    }
}
#print(sample_dict)
try:
    # load via kwargs
    test = SomeName(**sample_dict)
    print(test)
except ValidationError as e:
    print(e.errors())
