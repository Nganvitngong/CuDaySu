import streamlit as st
import time
from home import run_home
from chatbot import run_chatbot
from quiz import run_quiz
from discovery import run_discovery

# 1. Cấu hình trang (Phải nằm ở dòng đầu tiên)
st.set_page_config(layout="wide", page_title="Cú Dạy Sử", initial_sidebar_state="collapsed")

# 2. Khởi tạo dữ liệu người dùng
if "user_info" not in st.session_state:
    st.session_state.user_info = {"full_name": "Học viên", "phone": "Chưa cập nhật"}

u_name = st.session_state.user_info["full_name"]
u_img = f"https://api.dicebear.com/7.x/initials/png?seed={u_name.replace(' ', '')}"
brand_logo = "https://i.pinimg.com/736x/03/fc/49/03fc49fdce96bb618c07aaf4f5dbd6ba.jpg"

# 3. Hàm Dialog chỉnh sửa thông tin
@st.dialog("⚙️ Cài đặt tài khoản")
def show_settings():
    name = st.text_input("Họ và tên", value=st.session_state.user_info["full_name"])
    phone = st.text_input("Số điện thoại", value=st.session_state.user_info["phone"])
    if st.button("Lưu thay đổi", type="primary", use_container_width=True):
        st.session_state.user_info["full_name"] = name
        st.session_state.user_info["phone"] = phone
        st.rerun()

# 4. Quản lý điều hướng (Fix logic để không bị kẹt ở trang Home)
query_params = st.query_params
if "p" not in st.session_state:
    st.session_state.page = query_params.get("p", "home")
else:
    if "p" in query_params:
        st.session_state.page = query_params["p"]

# Xử lý nút "Khám phá ngay" từ file Home
if query_params.get("nav") == "login":
    st.session_state.page = "chatbot"
    st.query_params.clear()
    st.rerun()

if query_params.get("action") == "settings":
    show_settings()

# 5. SIÊU CSS (FIXED Z-INDEX CAO NHẤT)
st.markdown("""
<style>
    header[data-testid="stHeader"], footer { visibility: hidden; }
    .main .block-container { padding: 0 !important; }

    .nav-container {
      position: fixed !important; 
      top: 0; left: 0; right: 0; 
      height: 64px;
      display: flex !important; 
      justify-content: space-between; 
      align-items: center;
      padding: 0 50px; 
    
      /* 1. MÀU NỀN: */
      background: rgba(113, 12, 33, 0.85) !important;
    
      /* 2. ĐỘ BÓNG: Tăng độ đậm lên 0.2 (20%) để nhìn thấy rõ trên nền màu */
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15) !important;
    
      /* 3. HIỆU ỨNG NHÒE: Gom lại một chỗ cho sạch code */
      -webkit-backdrop-filter: blur(25px) !important;
       backdrop-filter: blur(25px) !important; 
    
       /* 4. VIỀN DƯỚI: Thay vì màu đen (0,0,0), hãy dùng màu trắng nhẹ để tạo ánh sáng */
       border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
       border-top: 1px solid rgba(255, 255, 255, 0.1) !important;  
        z-index: 99999999 !important; /* Đảm bảo nổi trên tất cả các loại Iframe */
    }

    .nav-links { display: flex; gap: 50px; }
    .nav-item {
        text-decoration: none !important; color: white !important;
        font-weight: 600; font-size: 18px; transition: 0.3s;
    }
    .active-nav {
        color: #2d3436 !important; background-color: rgba(255, 249, 219, 0.8) !important;
        padding: 8px 18px !important; border-radius: 10px; font-weight: 800;
    }

    .dropdown { position: relative; display: inline-block; }
    .dropdown-content {
        display: none; position: absolute; right: 0; top: 45px;
        background-color: white; min-width: 180px; border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.1); z-index: 10000000 !important;
        border: 1px solid #f0f0f0; overflow: hidden;
    }
    .dropdown:hover .dropdown-content { display: block; }
    .dropdown-item {
        color: #1e293b; padding: 12px 20px; text-decoration: none;
        display: block; font-size: 13px; font-weight: 600; transition: 0.2s;
    }
    .dropdown-item:hover { background-color: #f8fafc; color: #7d5fff; }
</style>
""", unsafe_allow_html=True)

# 6. RENDER HEADER (LUÔN RENDER ĐỂ TRÁNH LỖI MẤT MENU)
# Chúng ta chỉ ẩn nội dung menu bằng CSS nếu cần, nhưng thẻ HTML phải luôn tồn tại
st.markdown(f"""
<div class="nav-container">
    <div style="display: flex; align-items: center; gap: 12px; cursor: pointer;" onclick="window.parent.location.href='/?p=home'">
        <img src="{brand_logo}" width="34" style="border-radius: 8px;">
        <span style="font-size: 18px; font-weight: 800; color: white; letter-spacing: -0.5px;">CÚ DẠY SỬ</span>
    </div>
    <div class="nav-links">
        <a href="/?p=home" target="_self" class="nav-item {'active-nav' if st.session_state.page == 'home' else ''}">Trang chủ</a>
        <a href="/?p=chatbot" target="_self" class="nav-item {'active-nav' if st.session_state.page == 'chatbot' else ''}">Chatbot</a>
        <a href="/?p=quiz" target="_self" class="nav-item {'active-nav' if st.session_state.page == 'quiz' else ''}">Luyện đề</a>
        <a href="/?p=discovery" target="_self" class="nav-item {'active-nav' if st.session_state.page == 'discovery' else ''}">Khám phá</a>
    </div>
    <div class="dropdown">
        <div style="display: flex; align-items: center; gap: 12px; cursor: pointer;">
            <span style="font-size: 12px; font-weight: 800; color: white; text-transform: uppercase;">{u_name}</span>
            <img src="{u_img}" width="32" style="border-radius: 50%; border: 2px solid #7d5fff;">
        </div>
        <div class="dropdown-content">
            <a href="/?p={st.session_state.page}&action=settings" target="_self" class="dropdown-item">⚙️ Cài đặt tài khoản</a>
            <a href="/" target="_self" class="dropdown-item">🚪 Đăng xuất</a>
        </div>
    </div>
</div>
<div style="margin-top: 0px;"></div>
""", unsafe_allow_html=True)

# 7. HIỂN THỊ NỘI DUNG TRANG
if st.session_state.page == "home":
    # Thêm một chút padding để trang home không bị Header đè mất phần Hero
    st.markdown('<div style="height: 0px;"></div>', unsafe_allow_html=True)
    run_home()
else:
    st.markdown('<div style="margin-top: -10px;">', unsafe_allow_html=True)
    if st.session_state.page == "chatbot":
        run_chatbot()
    elif st.session_state.page == "quiz":
        run_quiz()
    elif st.session_state.page == "discovery":
        run_discovery()
    st.markdown('</div>', unsafe_allow_html=True)