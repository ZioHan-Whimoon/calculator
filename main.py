import streamlit as tf
import math

# 웹앱 제목 설정
st.title("🔢 다기능 계산기 웹앱")
st.write("사칙연산, 모듈러, 지수, 로그 연산을 지원하는 계산기입니다.")

# 사이드바에서 연산 종류 선택
operation = st.sidebar.selectbox(
    "원하는 연산을 선택하세요",
    ["사칙연산 (+, -, *, /)", "모듈러 연산 (%)", "지수 연산 (^)", "로그 연산 (log)"]
)

st.markdown("---")

# 1. 사칙연산
if operation == "사칙연산 (+, -, *, /)":
    st.subheader("➕ 사칙연산")
    num1 = st.number_input("첫 번째 숫자를 입력하세요", value=0.0)
    op = st.selectbox("연산자를 선택하세요", ["+", "-", "*", "/"])
    num2 = st.number_input("두 번째 숫자를 입력하세요", value=0.0)
    
    if st.button("계산하기"):
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("0으로 나눌 수 없습니다!")
                result = None
        
        if result is not None:
            st.success(f"결과: {num1} {op} {num2} = {result}")

# 2. 모듈러 연산 (나머지 구하기)
elif operation == "모듈러 연산 (%)":
    st.subheader("🧩 모듈러 연산 (나머지 계산)")
    num1 = st.number_input("나누어질 수 (피제수)를 입력하세요", value=0.0)
    num2 = st.number_input("나눌 수 (제수)를 입력하세요", value=1.0)
    
    if st.button("계산하기"):
        if num2 != 0:
            result = num1 % num2
            st.success(f"결과: {num1} % {num2} = {result}")
        else:
            st.error("0으로 나눌 수 없습니다!")

# 3. 지수 연산
elif operation == "지수 연산 (^)":
    st.subheader("📈 지수 연산")
    base = st.number_input("밑(Base)을 입력하세요", value=2.0)
    exponent = st.number_input("지수(Exponent)를 입력하세요", value=3.0)
    
    if st.button("계산하기"):
        result = base ** exponent
        st.success(f"결과: {base} ^ {exponent} = {result}")

# 4. 로그 연산
elif operation == "로그 연산 (log)":
    st.subheader("🪵 로그 연산")
    log_type = st.radio("로그 종류를 선택하세요", ["자연로그 (ln)", "상용로그 (log10)", "밑이 지정된 로그 (log_base)"])
    
    x = st.number_input("진수(x)를 입력하세요 (0보다 커야 합니다)", value=1.0)
    
    if log_type == "밑이 지정된 로그 (log_base)":
        base = st.number_input("밑(Base)을 입력하세요 (0보다 크고 1이 아니어야 합니다)", value=2.0)
    
    if st.button("계산하기"):
        if x <= 0:
            st.error("진수는 0보다 커야 합니다!")
        else:
            if log_type == "자연로그 (ln)":
                result = math.log(x)
                st.success(f"결과: ln({x}) = {result}")
            elif log_type == "상용로그 (log10)":
                result = math.log10(x)
                st.success(f"결과: log10({x}) = {result}")
            elif log_type == "밑이 지정된 로그 (log_base)":
                if base <= 0 or base == 1:
                    st.error("올바르지 않은 밑입니다!")
                else:
                    result = math.log(x, base)
                    st.success(f"결과: log_{base}({x}) = {result}")
