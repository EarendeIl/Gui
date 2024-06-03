import folium
"""
6
7
11
lang 参数通常有以下选择：

zh_cn: 中文简体
en: 英文"""
# 高德地图API密钥
style = 7
lang = "zh_cn"
amap_api_key = 'b6acf9a34babd2e400c2628043c8d2c9'

# 中心点坐标（这里以北京天安门为例）
center_lat, center_lng = 39.908823, 116.397470

# 创建一个地图对象，使用默认的瓦片图层
m = folium.Map(
    location=[center_lat, center_lng],
    zoom_start=10,  # 调整缩放级别以匹配图片的范围
    prefer_canvas=True  # 优化大量数据的渲染
)

# 添加高德地图的瓦片图层（选择适合的样式）
tile_url = f"http://wprd03.is.autonavi.com/appmaptile?style={style}&x={{x}}&y={{y}}&z={{z}}&lang={lang}&size=1&scl=1&ltype=7&key={amap_api_key}"
folium.TileLayer(
    tiles=tile_url,
    attr='高德地图'
).add_to(m)

# 添加一个输入框和搜索按钮元素
input_html = """
<style>
    html, body {
        width: 100%;
        height: 100%;
        margin: 0;
        padding: 0;
        display: flex;
        flex-direction: column;
    }

    #map {
        flex-grow: 1;
    }

    .input-container {
        display: flex;
        justify-content: center;
        padding: 20px;
        background-color: white;
        z-index: 1000;
    }

    .input-container input {
        width: 300px; /* 输入框的固定宽度为 300 像素 */
        margin-right: 1px; /* 输入框之间的间隔 */
        height: 35px; /* 增加输入框的高度 */
    }

    .input-container button {
        height: 35px;
        padding: 0 10px;
    }

    .leaflet-container { font-size: 1.2rem; }
</style>

<div class="input-container">
    <div class="search-box">
        <b>POI名称：</b>
        <input id="poiName" type="text">
    </div>
    <div>
        <button id="searchButton">搜索</button>
        <b>经纬度：</b>
        <input id="coordinates" type="text">
    </div>
</div>
"""
m.get_root().html.add_child(folium.Element(input_html))

# 修改后的 JavaScript 点击事件，显示完整的经纬度并更新到输入框
click_js = f"""
var previousMarker = null; // 存储上一个点击的标记
var isProcessingClick = false; // 标志是否正在处理点击事件
var isProcessingSearch = false; // 标志是否正在处理搜索事件
function addClickListener(map) {{
    map.on('click', function(e) {{
        if (isProcessingClick) return; // 如果正在处理点击事件，则返回
        isProcessingClick = true;

        var lat = e.latlng.lat.toFixed(6);
        var lng = e.latlng.lng.toFixed(6);
        if (previousMarker !== null) {{
        map.removeLayer(previousMarker); // 移除上一个标记
        }}
        var url = 'https://restapi.amap.com/v3/geocode/regeo?key={amap_api_key}&location=' + lng + ',' + lat + '&extensions=all';
        fetch(url)
            .then(response => response.json())
            .then(data => {{
                var poiName = '地图选点';
                if (data.regeocode && data.regeocode.pois && data.regeocode.pois.length > 0) {{
                    poiName = data.regeocode.pois[0].name;
                }}
                var marker = L.marker([lat, lng]).addTo(map);
                marker.bindPopup('POI名称: ' + poiName + '<br>经度: ' + lng + '<br>纬度: ' + lat).openPopup();
                document.getElementById('poiName').value = poiName;
                document.getElementById('coordinates').value = lng + ',' + lat;
                previousMarker = marker; // 更新上一个标记
                isProcessingClick = false; // 完成点击事件处理
            }})
            .catch(error => {{
                console.error('Error fetching POI data:', error);
                document.getElementById('poiName').value = '';
                document.getElementById('coordinates').value = '获取POI信息时出错\\n经度: ' + lng + '\\n纬度: ' + lat;
                isProcessingClick = false; // 完成点击事件处理
            }});
    }});
}}
    document.addEventListener('DOMContentLoaded', function() {{
        var map = L.map('map', {{
                maxZoom: 22, // 设置最大缩放级别为22
                minZoom: 4 // 设置最小缩放级别为4
            }}).setView([39.908823, 116.39747], 11);
                        // 自定义比例尺控件
            var customScaleControl = L.control.scale({{
                maxWidth: 200, // 设置比例尺控件的最大宽度
                metric: true, // 显示米单位
                imperial: false, // 不显示英制单位
                position: 'bottomright', // 设置比例尺控件的位置为地图右下角
            }});

            customScaleControl.addTo(map);

            // 添加OpenStreetMap图层
            var osmLayer = L.tileLayer("https://tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png", {{
                attribution: "&copy; OpenStreetMap贡献者",
                maxZoom: 19
            }}).addTo(map);

            // 设置最大边界限制平移
            var maxBounds = L.latLngBounds(
                L.latLng(-85, -180), // 西南角
                L.latLng(85, 180)    // 东北角
            );

            map.setMaxBounds(maxBounds);
            // 添加高德地图图层
            var gaodeLayer = L.tileLayer("http://wprd03.is.autonavi.com/appmaptile?style={style}&x={{x}}&y={{y}}&z={{z}}&lang={lang}&size=1&scl=1&ltype=7&key=b6acf9a34babd2e400c2628043c8d2c9", {{
                attribution: "高德地图",
                maxZoom: 18
            }}).addTo(map);

            addClickListener(map);

// 添加搜索按钮点击事件
document.getElementById('searchButton').addEventListener('click', searchLocation);

// 添加回车键搜索事件
document.getElementById('poiName').addEventListener('keydown', function(event) {{
    if (event.keyCode === 13) {{ // 如果按下的是回车键
        searchLocation();
    }}
}});

    // 搜索位置函数
    // 在搜索位置函数中，获取搜索结果中的实际 POI 名称，并将其作为地图标记的弹出窗口内容
function searchLocation() {{
    if (isProcessingSearch) return; // 如果正在处理搜索事件，则返回
    isProcessingSearch = true;
    // 移除上一个标记
    if (previousMarker !== null) {{
        map.removeLayer(previousMarker);
    }}
    var searchKeyword = document.getElementById('poiName').value.trim();
    if (searchKeyword !== '') {{
        var searchUrl = 'https://restapi.amap.com/v3/place/text?key={amap_api_key}&keywords=' + searchKeyword;
        fetch(searchUrl)
            .then(response => response.json())
            .then(data => {{
                if (data.status === '1' && data.count > 0) {{
                    var firstResult = data.pois[0]; // 获取第一个搜索结果
                    var location = firstResult.location.split(',');
                    var lng = location[0];
                    var lat = location[1];
                    var poiName = firstResult.name; // 获取实际的 POI 名称
                    var marker = L.marker([lat, lng]).addTo(map);
                    marker.bindPopup('POI名称: ' + poiName + '<br>经度: ' + lng + '<br>纬度: ' + lat).openPopup();
                    map.setView([lat, lng], 14); // 将地图视图移动到搜索结果位置
                    document.getElementById('coordinates').value = lng + ',' + lat;
                    previousMarker = marker; // 更新上一个标记
                    isProcessingSearch = false; // 完成搜索事件处理

                }} else {{
                    console.error('No search results found.');
                    alert('未找到相关结果，请尝试其他关键词。');
                    isProcessingSearch = false; // 完成搜索事件处理
                }}
            }})
            .catch(error => {{
                console.error('Error fetching search data:', error);
                alert('搜索位置信息时出错，请稍后重试。');
                isProcessingSearch = false; // 完成搜索事件处理
            }});
    }} else {{
        alert('请输入搜索关键词。');
        isProcessingSearch = false; // 完成搜索事件处理

    }}
}}
}});
 //添加自定义 JavaScript 到地图
"""
m.get_root().html.add_child(folium.Element(f'<script>{click_js}</script>'))

# 保存地图为 HTML 文件
m.save('map_location.html')
