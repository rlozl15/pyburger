# PyBurger 프로젝트
이 프로젝트는 이한영의 장고 입문에 실린 PyBurger 프로젝트를 기반으로 한 클론 코딩 프로젝트입니다.   
햄버거 목록을 보여주고, 키워드로 검색할 수 있는 PyBurger 사이트를 구축하며 Django 프레임워크의 동작을 이해하는 것을 목표로 했습니다.  
또한, 책 내용 이외에 Docker에 대해 학습하여 Docker 기반의 개발 환경을 구축하고, 컨테이너에서 프로젝트를 실행할 수 있도록 설정했습니다.

## 기간
2024.10.24 ~ 2024.10.27

## 주요 학습 내용
1. **Django 기반 웹 애플리케이션 구성**   
   Django 서버 실행, 데이터 모델 정의 및 ORM 사용, view와 template을 활용해 웹 페이지를 구성했습니다.

3. **Docker 기반 개발 환경 설정**   
   Docker와 Docker Compose로 개발 환경을 구성하여, 애플리케이션을 일관된 개발 환경인 컨테이너에서 실행할 수 있도록 구축했습니다. 

## 기술 스택
    - 백엔드: Django
    - 프론트엔드: HTML, Django 템플릿
    - 데이터베이스: Django ORM (SQLite3)
    - 컨테이너: Docker

## 설정 및 실행
1. **저장소 클론**
    ``` bash
    git clone https://github.com/rlozl15/pyburger.git
    cd pyburger
    ```

2. **Docker 환경 준비**   
   Docker Desktop을 실행합니다.

3. **Docker 이미지 빌드 및 실행**
    ``` bash
    docker-compose up -d --build
    ```

4. **Django 앱 및 마이그레이션**   
   데이터베이스 테이블을 생성하고 앱을 등록하기 위한 마이그레이션을 수행합니다.
    ``` bash
    docker-compose exec app python manage.py migrate
    ```

5. **버거 데이터 임의 추가**
    ``` bash
    docker-compose exec app python manage.py loaddata burgers/fixtures/burgers.json
    ```

6. **Django 서버 확인**
   - http://localhost:8000 에서 Django 애플리케이션에 접근할 수 있습니다.
   ![img.png](static/img.png)
     
