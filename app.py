import streamlit as st
import streamlit.components.v1 as components

# Thiết lập giao diện trang rộng để hiển thị HTML tốt hơn (tùy chọn)
st.set_page_config(layout="wide")

# Mở và đọc nội dung file HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# Render HTML lên Streamlit
# Bạn có thể thay đổi height theo chiều cao thực tế của giao diện HTML
components.html(html_data, height=800, scrolling=True)
