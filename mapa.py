import geopandas as gpd

# Cambia la ruta a la ubicación donde descomprimiste los archivos
shapefile_path = "gadm36_MEX_shp/gadm36_MEX_1.shp"

# Cargar el shapefile localmente
gdf = gpd.read_file(shapefile_path)

# Filtrar el estado de Guanajuato
guanajuato = gdf[gdf['NAME_1'] == 'Guanajuato']

# Revisar si se cargó correctamente
print(guanajuato)

# Exportar a GeoJSON
guanajuato.to_file("guanajuato_map.geojson", driver="GeoJSON")
