
# 시각장애인 위험 요소 알림 서비스

## 1. 프로젝트 개요
#### - 프로젝트 유형 : PBL(Problem-Based-Learning)사업
#### - 프로젝트 수행기간 : 2019.01.11. ~ 2019.01.31


## 2. 프로젝트 기획배경 및 목표

### ㄱ. 프로젝트 기획배경
초기 기획 당시에는 제시된 문제해결을 통한 학습자 능력향상이라는 PBL사업의 취지를 고려하여 시간장애인을 위한 서비스를 기획하기로 함. 그리고 최종적으로 PBL사업의 큰 축인 자기 주도적 학습(Self-Directed-Learnig, SDL), 협동학습(Collaborative learning)를 고려하여 딥러닝을 활용한 시각장애인 알림 서비스를 기획함. 이렇게 구성된 프로젝트의 최종적인 서비스 구성도는 아래와 같음.
![](https://images.velog.io/images/cooo002/post/48ca51d0-66c0-481f-b5e9-52437f3f5804/image.png)

### ㄴ. 프로젝트 목표
>  - Cloud Computing, Deep-Learning, REST API 등을 활용한 서비스 개발
- Computer Vision API,  Speech Service REST API를 활용하여 위험상황의 인지가 힘든 시각장애인을 위한 위험 상황 알림 서비스 구현.
- 재난상황 및 기상정보에 따른 재난예비경보, 특보, 상황전파 등의 정보 수신 시 신속한 확인이 어려운 시각장애인을 위한 재난 특보 알리미 서비스 구현.
- 미세먼지로 인한 피해가 심각해짐에 따라 손쉽게 음성으로 현재 위치에 대한 미세먼지 정보를 음성으로 알려주는 서비스 구현
시각 장애인을 위해 음성 안내 및 간단한 인터페이스를 활용한 UI/UX설계


## 3. 프로젝트 수행내용

### ㄱ. 개발환경
![](https://images.velog.io/images/cooo002/post/150f9a6a-42f8-4c44-98a4-7f618bf451b2/image.png)

> #### **백엔드**
* 언어
-Python 2.7.16
* 개발환경
-MicroSoftware Azure Cloud Computer 
-MicroSoftware Azure Storage
-Visual Studio 2019 IDE
-Flask 1.0.2
* 라이브러리
-Naver Papago NMT API
-MS Azure Computer Vision API
-공공 데이터 포탈 재난 예비특보 조회 REST API
* 버전관리
-git

> #### **프론트**
* 언어
-Java SE 11(18.9 LTS)
* 개발환경
-AndroidStudio 3.3
-Software Development Kit 6.0 Marshmallow
* 라이브러리
-Google Speech API(TTS)
-Java Android Retrofit2 
-Google Geocorder API(GPS, NET)
* 버전관리
-git

### ㄴ. 프로젝트 참여인원 및 담당업무

> ### 정규준
* **프로젝트 활용기술**
Python, Flask, BeautifulSoup Library, datetime, Open API, Azure Speech API(TTS), Naver Papago NMT, Linux Virtual Machine
* **담당업무**
-Papago NMT를 이용한 번역 기능
-Speech API(TTS) 이용한 텍스트의 음성변환 기능
-공공데이터포털 Open API의 Data Parsing

> ### 김재석(*본인)
* **프로젝트 활용기술**
HTTP, REST API , Python, Blob Storage, Azure Virtual Machine, Computer Vison API
* **담당업무**
-파싱 결과 확인을 위한 웹 페이지 제작
-Azure Cloud Computer를 이용한 서버 구축
-Blob Storage를 활용한 이미지 저장 기능
-Azure Computer Vision API를 활용한 이미지 분석 기능

> ### 류원혁
* **프로젝트 활용기술**
HTTP, Android Studio, Android SDK 6.0, Android Library, Google Speech API, Google Retrofit2 Library, JAVA, Multipart From-data
* **담당업무**
-Java Android Retrofit2를 이용한 통신 기능
-Google TTS/STT를 이용한 응답 데이터 음성 변환
-Java SE 11(18.9 LTS), Software Development Kit 6.0 Marshmallow를 이용한 클라이언트 UI 및 기능 개발

> ### 김기빈
* **프로젝트 활용기술**
HTTP, Android Studio, Google Speech API(TTS, STT), HttpUrlConnection, Google Geocoding API, AsyncTask, Python,Android Developers(Location Manager)
* **담당업무**
-Java Android Retrofit2를 이용한 통신 기능
-Google TTS/STT를 이용한 응답 데이터 음성 변환
-Java SE 11(18.9 LTS), Software Development Kit 6.0 Marshmallow를 이용한 클라이언트 UI 및 기능 개발

### ㄷ. 세부수행 내역(담당 업무)
#### * **Azure Cloud Computer를 이용한 서버 구축**
![실제구성한 가상머신 정보](https://images.velog.io/images/cooo002/post/a65faa65-8540-4557-86b5-5241fc62422e/image.png)
![](https://images.velog.io/images/cooo002/post/f7b74691-8272-41a7-bd88-d44087439180/image.png)

> **Azrure Clould Computer 사용이유**
* Cloud환경에 대한 궁금증 및 학습 욕구
* 한정된 개발시간
* 하나의 플랫폼으로 여러 서비스를 이용할 수 있다는 장점
* 완성된 플랫폼 사용으로 통해 백엔드 배경지식의 부족함으로 일어날 수 있는 문제 해결

#### * **Azure Blob-Storage를 활용한 이미지 저장 기능**

> **Azrure Clould Blob Storage Service 사용이유**
* 간단한 이미지 업로드 기능
* REST API로 제공되는 Computer Vision API의 활용
* DashBoard와 같은 시각적 요소로 업로드된 이미지 관리


#### * **Azure Computer Vision API를 활용한 이미지 분석 기능**

> **Azrure Computer Vision API 사용이유**
* 서버를 구성한 Azure Cloud Computer와의 호환성
* REST API를 활용한 쉬운 사용법
* 서버 경량화
* 개발시간 단축

### ㄷ. 구동화면 및 세부설명

![](https://images.velog.io/images/cooo002/post/2b9447d9-7a04-4722-b883-8b7c104d375a/image.png)

#### * **간단한 UI/UX**
-어플리케이션 시작 또는 해당 버튼 선택 시 음성으로 각 버튼의 위치와 수행 기능 안내
#### * **위험상황 알림 기능**
-버튼 선택 시 Google Voice를 통하여 사용자의 음성을 인식, 현재 상황 촬영 및 분석 음성으로 안내
#### * **재난특보 알림 기능**
-버튼 선택 시 현재 위,경도 값을 이용해 해당 지역에 발생한 재난 특보 안내
#### * **미세먼지 정보 알림 서비스**
-버튼 선택 시 현재 위,경도 값을 이용해 해당 지역에 발생한 미세먼지 관련 정보 안내




