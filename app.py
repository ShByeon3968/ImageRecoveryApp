import streamlit as st
from PIL import Image
from utils import preprocess_image, super_resolve, colorize_image

st.title("AI 기반 사진 복원 도구")
st.write("오래된 사진의 품질을 개선하거나 색상을 복원합니다.")

# 이미지 업로드
uploaded_file = st.file_uploader("사진을 업로드하세요", type=["jpg", "png", "jpeg"])
if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="원본 이미지", use_column_width=True)

    # 복원 옵션 선택
    option = st.selectbox("복원 옵션을 선택하세요", ["고해상도 복원", "색상 복원"])

    if st.button("복원 시작"):
        if option == "고해상도 복원":
            result = super_resolve(img)
        elif option == "색상 복원":
            result = colorize_image(uploaded_file.name)
        st.image(result, caption="복원된 이미지", use_column_width=True)
