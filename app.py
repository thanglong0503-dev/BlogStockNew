import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Báo cáo Ngành Chứng khoán VN",
    page_icon="📊",
    layout="wide",
)

REPORTS_DIR = Path("reports")

@st.cache_data(show_spinner=False)
def load_report_list():
    return sorted(REPORTS_DIR.glob("*.html"), reverse=True)

@st.cache_data(show_spinner=False)
def read_html(path_str: str) -> str:
    return Path(path_str).read_text(encoding="utf-8")

reports = load_report_list()
if not reports:
    st.error("Chưa có báo cáo nào trong thư mục reports/.")
    st.stop()

labels = [p.stem for p in reports]

with st.sidebar:
    st.markdown("### 📊 Báo cáo định kỳ")
    st.caption("Ngành Chứng khoán Việt Nam")
    selected_label = st.radio("Chọn kỳ báo cáo", labels, index=0)
    st.divider()
    st.caption(f"Đang xem: **{selected_label}**")

selected_path = reports[labels.index(selected_label)]
html_data = read_html(str(selected_path))

# height đủ lớn để hiển thị toàn bộ nội dung, không cắt, không cuộn lồng
components.html(html_data, height=10200, scrolling=False)
