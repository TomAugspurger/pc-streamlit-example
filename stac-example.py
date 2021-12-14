import streamlit as st
from streamlit_folium import folium_static

import requests
import pystac
import folium
import pystac_client
import random
import shapely.geometry



"# streamlit-folium"

with st.echo():
    catalog = pystac_client.Client.open("https://planetarycomputer.microsoft.com/api/stac/v1/")

    search = catalog.search(collections=["sentinel-2-l2a"], limit=500, query={"eo:cloud_cover": {"lt": "15"}})

    ic = next(search.get_item_collections())

    item = random.choice(ic)

    item.bbox

    y, x, *_ = shapely.geometry.box(*item.bbox).centroid.bounds

    m = folium.Map(location=(x, y), zoom_start=8)

    layer = folium.raster_layers.TileLayer(
        tiles=requests.get(item.assets["tilejson"].href).json()["tiles"][0],
        attr="Sentinel 2 L2A",
    )

    layer.add_to(m)
    folium_static(m)
