import geopandas as gpd

# 读取 GeoJSON 文件
geojson_file = '/Users/yunching0513/Desktop/chatbot/data visualization/map_data/netherlands_.geojson'
gdf = gpd.read_file(geojson_file)

# 打印 GeoJSON 数据的列名
print("GeoJSON 文件的列名:")
print(gdf.columns)

# 打印前几行数据以查看内容
print("\nGeoJSON 文件的前几行数据:")
print(gdf.head())

import pandas as pd

# 读取 CSV 文件
data_file = '/Users/yunching0513/Desktop/chatbot/data visualization/traffic_data/nl_traffic_deaths_2011-2020.csv'
df = pd.read_csv(data_file)

# 打印 CSV 数据的列名
print("CSV 文件的列名:")
print(df.columns)

# 打印前几行数据以查看内容
print("\nCSV 文件的前几行数据:")
print(df.head())
