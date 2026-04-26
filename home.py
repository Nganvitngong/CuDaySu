import streamlit as st
import streamlit.components.v1 as components

def run_home():
    # 1. Cấu hình hệ thống (Giữ nguyên)
    st.markdown("""
        <style>
            ::-webkit-scrollbar { display: none; }
            html, body { -ms-overflow-style: none; scrollbar-width: none; overflow-x: hidden !important; }
            .stAppViewContainer, .stApp, .main, .block-container { background: transparent !important; padding: 0 !important; max-width: 100% !important; }
            header, footer, [data-testid="stHeader"] { display: none !important; }
        </style>
    """, unsafe_allow_html=True)

    # 2. Toàn bộ nội dung giao diện
    html_content = """
    <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@100;400;700;800;900&display=swap&subset=vietnamese" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Be Vietnam Pro', sans-serif; overflow-x: hidden; }
        ::-webkit-scrollbar { display: none; }

        .fixed-background {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.7)), 
                              url('https://i.pinimg.com/736x/1e/c4/c8/1ec4c8abfad522beca105366d71012f0.jpg');
            background-size: cover;
            background-position: center;
            z-index: -1;
        }

        .content-wrapper {
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding-bottom: 150px;
        }

        .hero { text-align: center; color: white; font-family: 'Be Vietnam Pro', sans-serif !important; padding: 100px 20px 40px; }
        .hero h1 { font-size: 65px; font-weight: 800; margin: 0; }
        
        .btn-explore {
            background: #52e067; color: white !important;
            padding: 16px 50px; border-radius: 100px;
            font-weight: bold; text-decoration: none !important;
            display: inline-block; margin-top: 25px;
            box-shadow: 0 10px 30px rgba(82,224,103,0.4);
            font-size: 18px;
        }

        .features-grid {
            display: flex; gap: 25px; justify-content: center;
            flex-wrap: wrap; padding: 20px; width: 100%; max-width: 1150px;
        }
        .card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            width: 310px; border-radius: 25px; overflow: hidden;
            transition: 0.4s; color: white; text-align: center;
        }
        .card:hover { transform: translateY(-15px); border-color: #52e067; }
        .card img { width: 100%; height: 170px; object-fit: cover; }
        .card-body { padding: 20px; }
        .card-body h3 { color: #52e067; margin-bottom: 8px; font-size: 20px; }

        .video-section {
            display: flex; flex-direction: column; gap: 35px;
            width: 100%; max-width: 1000px; padding: 20px; margin-top: 40px;
        }
        .video-popup {
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 30px; width: 100%; display: flex; 
            overflow: hidden; min-height: 280px; transition: 0.4s;
        }
        .video-popup:hover { border-color: #52e067; transform: scale(1.01); }
        .v-info { flex: 1; padding: 35px; color: white; display: flex; flex-direction: column; justify-content: center; }
        .v-info h3 { color: #52e067; margin-bottom: 12px; font-size: 24px; }
        .v-info p { font-size: 14px; opacity: 0.8; line-height: 1.5; }
        .v-frame { flex: 1.4; background: #000; min-height: 220px; }
        .v-frame iframe { width: 100%; height: 100%; border: none; }

        /* --- STYLE MỚI CHO KHO KHÓA HỌC --- */
        .course-section {
            width: 100%;
            max-width: 1150px;
            padding: 60px 20px;
            text-align: center;
        }
        .course-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-top: 30px;
        }
        .course-item {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 20px;
            overflow: hidden;
            transition: 0.3s;
            color: white;
            display: flex;
            flex-direction: column;
        }
        .course-item:hover { transform: translateY(-10px); border-color: #52e067; }
        .course-item img { width: 100%; height: 160px; object-fit: cover; }
        .course-content { padding: 15px; flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between; }
        .course-content h4 { font-size: 15px; margin-bottom: 15px; height: 40px; overflow: hidden; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; }
        .btn-learn {
            background: #52e067; color: white; border: none; padding: 10px; border-radius: 10px;
            font-weight: bold; cursor: pointer; transition: 0.3s; width: 100%;
        }
        .btn-learn:hover { background: #45c956; }

        /* --- MODAL HÀNG DỌC CHO KHÓA HỌC --- */
        .modal-course {
            display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.9); z-index: 20000; justify-content: center; align-items: center;
            backdrop-filter: blur(8px);
        }
        .modal-container {
            background: white; width: 90%; max-width: 800px; padding: 30px;
            border-radius: 25px; display: flex; flex-direction: column; gap: 20px;
        }
        .modal-video-box { position: relative; padding-bottom: 56.25%; height: 0; border-radius: 15px; overflow: hidden; background: #000; }
        .modal-video-box iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }
        .modal-container h2 { color: #333; font-size: 24px; border-left: 5px solid #52e067; padding-left: 15px; }
        .modal-container textarea { width: 100%; height: 150px; padding: 15px; border-radius: 15px; border: 1px solid #ddd; resize: none; font-family: inherit; }
        .btn-close-modal { background: #ff4757; color: white; border: none; padding: 12px; border-radius: 10px; font-weight: bold; cursor: pointer; }

        /* Style Góp ý (Giữ nguyên) */
        .feedback-trigger { position: fixed; bottom: 30px; right: 30px; background: #FFD1DC; padding: 15px 25px; border-radius: 50px; cursor: pointer; font-weight: bold; color: #555; z-index: 10000; }
        .feedback-modal { display: none; position: fixed; bottom: 100px; right: 30px; width: 350px; background: #FFF0F5; border-radius: 20px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); z-index: 10000; }
        .feedback-modal h2 { color: #DB7093; margin-bottom: 15px; font-size: 20px; text-align: center; }
        .feedback-modal input, .feedback-modal textarea { width: 100%; padding: 12px; margin-bottom: 15px; border: 1px solid #FFC0CB; border-radius: 100px; outline: none; }
        .feedback-modal textarea { height: 100px; resize: none; border-radius: 15px; }
        .feedback-modal button { width: 100%; padding: 12px; background: #DB7093; color: white; border: none; border-radius: 100px; font-weight: bold; cursor: pointer; }

        @media (max-width: 900px) {
            .course-grid { grid-template-columns: repeat(2, 1fr); }
            .video-popup { flex-direction: column; }
        }
    </style>

    <div class="fixed-background"></div>
    <div class="content-wrapper">
        <div class="hero">
            <h1 style="font-family: 'Be Vietnam Pro', sans-serif !important; font-size: 75px; font-weight: 900; color: white; text-shadow: 0 5px 20px rgba(0,0,0,0.6); margin: 0;">
               Cú Dạy Sử
            </h1>
            <p>Khám phá Lịch sử Việt Nam qua lăng kính AI hiện đại</p>
            <a href="/?p=chatbot" target="_parent" class="btn-explore">Khám phá ngay</a>
        </div>

        <div class="features-grid">
            <div class="card">
                <img src="https://i.pinimg.com/736x/16/1f/5c/161f5c81d2da6626d1ed2b2efdf57202.jpg">
                <div class="card-body"><h3>Chatbot AI</h3><p>Hỏi đáp lịch sử thông minh 24/7.</p></div>
            </div>
            <div class="card">
                <img src="https://images.unsplash.com/photo-1434030216411-0b793f4b4173?q=80&w=2000">
                <div class="card-body"><h3>Luyện đề</h3><p>Hệ thống đề thi chấm điểm tức thì.</p></div>
            </div>
            <div class="card">
                <img src="https://images.unsplash.com/photo-1461360370896-922624d12aa1?q=80&w=2000">
                <div class="card-body"><h3>Khám phá</h3><p>Tư liệu hình ảnh sử Việt hào hùng.</p></div>
            </div>
        </div>

        <div class="video-section">
            <div class="video-popup">
                <div class="v-info">
                    <h3>Lịch sử Việt Nam qua 4000 năm</h3>
                    <p>Tóm tắt nhanh các thời kỳ Lịch sử Việt Nam qua 4000 năm.</p>
                </div>
                <div class="v-frame"><iframe src="https://www.youtube.com/embed/MjeFdeEBZBo" allowfullscreen></iframe></div>
            </div>
            <div class="video-popup">
                <div class="v-info">
                    <h3>Chiến tranh lạnh bắt đầu như thế nào?</h3>
                    <p>Toàn bộ chiến tranh lạnh trong 60 phút.</p>
                </div>
                <div class="v-frame"><iframe src="https://www.youtube.com/embed/EG9gZmMGAr0?si=Db2Q2q5ETB_2y5h5" allowfullscreen></iframe></div>
            </div>
            <div class="video-popup">
                <div class="v-info">
                    <h3>30 năm tìm đường cứu nước</h3>
                    <p>Quá trình Bác Hồ giải phóng Việt Nam.</p>
                </div>
                <div class="v-frame"><iframe src="https://www.youtube.com/embed/2gtZpukMrn0" allowfullscreen></iframe></div>
            </div>
        </div>

        <section class="course-section">
            <h2 style="color: #52e067; font-size: 35px; font-weight: 900; text-shadow: 0 4px 10px rgba(0,0,0,0.3);">KHÓA HỌC LỊCH SỬ</h2>
            <div class="course-grid" id="courseGrid"></div>
            <button id="btnLoadMore" onclick="toggleCourses()" class="btn-explore" style="font-size: 14px; padding: 12px 40px; margin-top: 40px; background: rgba(255,255,255,0.2); border: 1px solid #52e067;">Xem thêm (6/17)</button>
        </section>
    </div>

    <div id="courseModal" class="modal-course">
        <div class="modal-container">
            <div class="modal-video-box"><iframe id="courseIframe" src="" frameborder="0" allowfullscreen></iframe></div>
            <h2 id="courseModalTitle">Tên bài học</h2>
            <textarea placeholder="Ghi chú kiến thức quan trọng vào đây... (Hệ thống không lưu lại ghi chú này)"></textarea>
            <button onclick="closeCourseModal()" class="btn-close-modal">ĐÓNG BÀI HỌC & QUAY LẠI</button>
        </div>
    </div>

    <div class="feedback-trigger" onclick="toggleFeedback()">Góp ý 🌼</div>
    <div class="feedback-modal" id="feedbackModal">
        <h2>Gửi góp ý cho Cú 🌼</h2>
        <input type="text" id="fbName" placeholder="Tên của bạn...">
        <textarea id="fbContent" placeholder="Ý kiến của bạn về ứng dụng..."></textarea>
        <button onclick="sendToSupabase()" id="btnSend">Gửi góp ý</button>
    </div>

    <script>
        // DỮ LIỆU KHÓA HỌC (ĐÃ ĐỒNG NHẤT TỪ COURSERA.PY)
        const courses = [
            {id: 1, title: "Bài 1. Liên hợp quốc", img: "https://kimlientravel.com.vn/upload/image/tru-so-Lien-Hop-Quoc-1.jpg", vid: "https://www.youtube.com/embed/HKNKn-Uc63Q"},
            {id: 2, title: "Bài 2. Trật tự thế giới Chiến tranh lạnh", img: "https://haylamdo.com/lich-su-12-cd/images/ly-thuyet-bai-2-trat-tu-the-gioi-trong-chien-tranh-lanh-2.PNG", vid: "https://www.youtube.com/embed/BcAdCWwdd28"},
            {id: 3, title: "Bài 3. Trật tự thế giới sau Chiến tranh lạnh", img: "https://vnn-imgs-f.vgcloud.vn/2019/08/22/14/nhung-su-kien-chan-dong-the-gioi-thoi-chien-tranh-lanh-i.jpg", vid: "https://www.youtube.com/embed/6BDm2wPADCo"},
            {id: 4, title: "Sự ra đời và phát triển của ASEAN", img: "https://vnanet.vn/Data/Articles/2018/08/06/321304/vna_potal_ky_niem_51_nam_ngay_thanh_lap_hiep_hoi_cac_quoc_gia_dong_nam_a_881967-882018_stand.jpg", vid: "https://www.youtube.com/embed/ImO4j3Ww4fs"},
            {id: 5, title: "Bài 5. Cộng đồng ASEAN: Từ hiện thực", img: "https://kenhgiaovien.com/sites/default/files/styles/700xauto/public/2024-08/slide4_335.jpg", vid: "https://www.youtube.com/embed/l4b5Z3myIKo"},
            {id: 6, title: "Bài 6. Cách mạng tháng Tám năm 1945", img: "https://kenhgiaovien.com/sites/default/files/styles/700xauto/public/2024-10/slide5_238.jpg", vid: "https://www.youtube.com/embed/Z_I9wVcj06Q"},
            {id: 7, title: "Bài 7. Kháng chiến chống Pháp (1945-1954)", img: "https://kenhgiaovien.com/sites/default/files/styles/700xauto/public/2024-10/slide2_540.jpg", vid: "https://www.youtube.com/embed/bac8VAtSJTQ"},
            {id: 8, title: "Bài 8. Kháng chiến chống Mỹ (1954-1975)", img: "https://i.ytimg.com/vi/abUHqag-CeA/maxresdefault.jpg", vid: "https://www.youtube.com/embed/jkXvoFlrH9c"},
            {id: 9, title: "Bài 9. Đấu tranh bảo vệ Tổ quốc sau 1975", img: "https://file.thanhuyhanoi.vn/thanhuy/public/0/1/2024/4/30/50003827/6860897a-cc67-4436-936b-1612d552bcf5.jpg", vid: "https://www.youtube.com/embed/BowRRt-YUEw"},
            {id: 10, title: "Bài 10. Công cuộc Đổi mới từ năm 1986", img: "https://img.loigiaihay.com/picture/2020/0206/dai-hoi-8.png", vid: "https://www.youtube.com/embed/gIkx5UJITbw"},
            {id: 11, title: "Bài 11. Thành tựu bài học Đổi mới", img: "https://cdn.vnreview.vn/31159-e8018ac4b32f2af16002e3f953769b3f_hvn_700x400_jpg", vid: "https://www.youtube.com/embed/Cal667eqsJQ"},
            {id: 12, "title": "Bài 12. Đối ngoại giành độc lập (đầu XX-1945)", img: "https://images.baodantoc.vn/uploads/2021/12/14/root49/22.jpg", vid: "https://www.youtube.com/embed/CdDQZJyOxvw"},
            {id: 13, "title": "Bài 13. Đối ngoại kháng chiến Pháp - Mỹ", img: "https://llct.1cdn.vn/2022/06/09/lyluanchinhtri.vn-home-media-k2-items-cache-_38b583516eb5c2e3d4af5ae22c6d48cf_l.jpg", vid: "https://www.youtube.com/embed/iRkWueLQ6To"},
            {id: 14, "title": "Bài 14. Đối ngoại Việt Nam từ 1975", img: "https://thepeninsulaqatar.com/get/maximage/20230910_1694355319-862.jpeg?1694355319", vid: "https://www.youtube.com/embed/RQUYzGIOhO4"},
            {id: 15, "title": "Bài 15. Cuộc đời và sự nghiệp Hồ Chí Minh", img: "https://imgcdn.tapchicongthuong.vn/thumb/w_1000/tcct-media/25/5/12/chu-tich-ho-chi-minh-anh-hung-giai-phong-dan-toc-viet-nam--chien-si-loi-lac-cua-phong-trao-cong-san-va-cong-nhan-quoc-te_6821ad36943d3.png", vid: "https://www.youtube.com/embed/9mGdBP-c-M0"},
            {id: 16, "title": "Bài 16. Hồ Chí Minh - Anh hùng giải phóng", img: "https://www.ntu.edu.vn/uploads/46/images/news/9602/img/chu-tich-ho-chi-minh-anh-hung-giai-phong-dan-toc-viet-nam-nha-van-hoa-kiet-xua.jpg", vid: "https://www.youtube.com/embed/vpVcsRVsefI"},
            {id: 17, "title": "Bài 17. Dấu ấn Hồ Chí Minh thế giới", img: "https://s-aicmscdn.vietnamhoinhap.vn/plql-media/24/1/10/mmm_659eaaf00d9c5.jpg", vid: "https://www.youtube.com/embed/b0E7RmfIMRo"}
        ];

        let currentMode = 6;
        function renderCourses() {
            const grid = document.getElementById('courseGrid');
            grid.innerHTML = '';
            courses.slice(0, currentMode).forEach(c => {
                grid.innerHTML += `
                    <div class="course-item">
                        <img src="${c.img}">
                        <div class="course-content">
                            <h4>${c.title}</h4>
                            <button class="btn-learn" onclick="openCourseModal('${c.vid}', '${c.title}')">VÀO HỌC NGAY</button>
                        </div>
                    </div>
                `;
            });
            const btn = document.getElementById('btnLoadMore');
            if(currentMode === 6) btn.innerText = "Xem thêm (6/17)";
            else if(currentMode === 13) btn.innerText = "Xem thêm (13/17)";
            else btn.innerText = "Thu gọn danh sách";
        }

        function toggleCourses() {
            if(currentMode === 6) currentMode = 13;
            else if(currentMode === 13) currentMode = 17;
            else currentMode = 6;
            renderCourses();
        }

        function openCourseModal(vid, title) {
            document.getElementById('courseIframe').src = vid;
            document.getElementById('courseModalTitle').innerText = title;
            document.getElementById('courseModal').style.display = 'flex';
        }

        function closeCourseModal() {
            document.getElementById('courseModal').style.display = 'none';
            document.getElementById('courseIframe').src = '';
        }

        function toggleFeedback() {
            const modal = document.getElementById('feedbackModal');
            modal.style.display = modal.style.display === 'block' ? 'none' : 'block';
        }

        // Khởi tạo lần đầu
        renderCourses();

        async function sendToSupabase() {
            // Giữ nguyên logic Supabase của bạn
            const name = document.getElementById('fbName').value;
            const content = document.getElementById('fbContent').value;
            const btn = document.getElementById('btnSend');
            if(!name || !content) { alert("Vui lòng điền đủ tên và nội dung nha!"); return; }
            btn.innerText = "Đang gửi..."; btn.disabled = true;
            const SUBAPASE_URL = "https://kdudfhkvpzfzkxcselxg.supabase.co";
            const SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtkdWRmaGt2cHpmemt4Y3NlbHhnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzYzMjA4MjMsImV4cCI6MjA5MTg5NjgyM30.K-meGsEa0NtOZStbdwOdH-MLM7KrSD2c7uvsY41-G4U";
            try {
                const response = await fetch(`${SUBAPASE_URL}/rest/v1/feedbacks`, {
                    method: 'POST',
                    headers: { 'apikey': SUPABASE_KEY, 'Authorization': `Bearer ${SUPABASE_KEY}`, 'Content-Type': 'application/json', 'Prefer': 'return=minimal' },
                    body: JSON.stringify({ user_name: name, content: content, created_at: new Date() })
                });
                if (response.ok) { alert("Cảm ơn bạn! Góp ý đã được gửi tới Cú. 🌼"); document.getElementById('fbName').value = ""; document.getElementById('fbContent').value = ""; toggleFeedback(); }
            } catch (error) { alert("Lỗi gửi góp ý!"); } finally { btn.innerText = "Gửi góp ý"; btn.disabled = false; }
        }
    </script>
    """
    
    # Tăng height lên 2500 để chứa đủ danh sách 17 khóa học khi mở rộng
    components.html(html_content, height=2500, scrolling=True)

if __name__ == "__main__":
    run_home()