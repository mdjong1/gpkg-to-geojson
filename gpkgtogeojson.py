import sys

import fiona

from geojson import Feature, FeatureCollection, dump, Polygon

if __name__ == "__main__":
    arguments = sys.argv
    if len(arguments) != 3:
        print("Invalid number of arguments used!")
        print("Usage: gpkgtogeojson.py <input GPKG file> <output GeoJSON file>")
        sys.exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    vertices = []
    features = []

    vertex_id = 1

    with fiona.open(input_file) as layer:
        for feature in layer:
            features.append(Feature(geometry=Polygon(feature["geometry"]["coordinates"])))

    feature_collection = FeatureCollection(features)

    with open(output_file, 'w') as f:
        dump(feature_collection, f)
