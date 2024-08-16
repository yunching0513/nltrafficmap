import pandas as pd
import geopandas as gpd
import json
import plotly.express as px
import streamlit as st

# 读取 CSV 文件
data_file = "Desktop/nltrafficmap/traffic_data.csv"
df = pd.read_csv(data_file)

# 将 'Provincie' 列重命名为 'Province'
df.rename(columns={'Provincie': 'Province'}, inplace=True)

# 读取 GeoJSON 文件
geojson_file = 'Desktop/nltrafficmap/netherlands_.geojson'
gdf = gpd.read_file(geojson_file)

# 合并地理数据和CSV数据
gdf = gdf.merge(df, on='Province')

# 将所有 Timestamp 类型列转换为字符串（防止 JSON 序列化错误）
for column in gdf.columns:
    if pd.api.types.is_datetime64_any_dtype(gdf[column]):
        gdf[column] = gdf[column].astype(str)

# GeoJSON 格式的字典
geojson_dict = json.loads(gdf.to_json())

# 使用 Plotly 绘制 Choropleth 地图
fig = px.choropleth(gdf,
                    geojson=geojson_dict,
                    locations=gdf.index,
                    color="Traffic deaths per 100,000 inhabitants",
                    hover_name="Province",
                    projection="mercator",
                    title="Netherlands Traffic Deaths per Province",
                    labels={"Traffic deaths per 100,000 inhabitants": "Deaths"},
                    color_continuous_scale="Reds")  # 设置为红色

# 设置地图边界和标题
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(
    margin={"r":0,"t":50,"l":0,"b":0},  # 调整 margin 以适应标题
    title={
        'text': "Netherlands Traffic Deaths per 100,000 Inhabitants 2011-2020",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)

# 在 Streamlit 中显示地图
st.plotly_chart(fig)
