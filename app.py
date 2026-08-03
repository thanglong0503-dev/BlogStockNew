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
    # sắp xếp mới nhất lên đầu theo tên file, ví dụ 2026-Q2 > 2026-Q1
    return sorted(REPORTS_DIR.glob("*.html"), reverse=True)

@st.cache_data(show_spinner=False)
def read_html(path_str: str) -> str:
    return Path(path_str).read_text(encoding="utf-8")

reports = load_report_list()

if not reports:
    st.error("Chưa có báo cáo nào trong thư mục reports/.")
    st.stop()

labels = [p.stem for p in reports]  # "2026-Q2", "2026-Q1"...

with st.sidebar:
    st.markdown("### 📊 Báo cáo định kỳ")
    st.caption("Ngành Chứng khoán Việt Nam")
    selected_label = st.radio("Chọn kỳ báo cáo", labels, index=0)
    st.divider()
    st.caption(f"Đang xem: **{selected_label}**")
    st.caption(f"Tổng số kỳ đã lưu trữ: {len(labels)}")

selected_path = reports[labels.index(selected_label)]
html_data = read_html(str(selected_path))

# height=1 chỉ là giá trị khởi tạo — script auto-resize bên trong HTML
# (xem mục 3) sẽ tự chỉnh lại chiều cao thật, tránh scroll lồng scroll
components.html(html_data, height=1200, scrolling=False)
