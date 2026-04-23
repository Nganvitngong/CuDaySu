import streamlit as st

def run_chatbot():
    # --- CSS GIỮ NGUYÊN ĐỂ FIT VỚI HEADER ---
    st.markdown("""
        <style>
            .main .block-container {
                padding: 0 !important;
                max-width: 100% !important;
                height: calc(100vh - 64px) !important;
                overflow: hidden !important;
            }
            
            /* Ép container chứa iframe bung lụa */
            [data-testid="stIFrame"] {
                position: fixed;
                top: 64px; 
                left: 0;
                width: 100vw !important;
                height: calc(100vh - 64px) !important;
                z-index: 1;
            }
            
            footer {display: none !important;}
            header {display: none !important;}
        </style>
    """, unsafe_allow_html=True)

    bot_url = "https://agent.jotform.com/019dab22261d75be9a6011d575ae864209c7"
    
    # Dùng hàm chuyên dụng để nhúng Iframe
    # Hàm này KHÔNG gây cảnh báo gỡ bỏ (vì nó không phải là v1.html)
    st.components.v1.iframe(
        src=bot_url,
        height=0, # Vẫn để 0 vì CSS ở trên đã ép nó theo màn hình
    )

if __name__ == "__main__":
    run_chatbot()