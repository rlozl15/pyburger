# python 3.11 버전을 사용한 기본 이미지
FROM python:3.11

# Python 출력 버퍼링을 비활성화
ENV PYTHONUNBUFFERED 1

# 작업 디렉토리 설정
WORKDIR /app

# requirements.txt 파일을 컨테이너에 복사
COPY requirements.txt .

# 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# 8000번 포트 개방
EXPOSE 8000