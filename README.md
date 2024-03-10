# 연대 X 숙대 리빙랩 연합 해커톤
### 2024.03.09 - 2024.03.10

## 기술 설명
* OpenAI API 생성형 AI 모델 사용
* AWS EC2를 이용하여 배포
<br />

## 시작 가이드
### Requirements
* Python 3.10.12
* openai 1.13.3


### Installation
```shell
git clone https://github.com/Yeinalee/six.git
cd ./six
```
### Environment Settings
```shell
cd ./six
python -m venv six
pip install openai
pip install django
pip install djangorestframework
pip install requests
pip install boto3
```

### Usage
```shell
source six/bin/activate
cd ./sixsense
python mangage.py runserver
```

<br />

## 구현 예시
* 클라이언트가 한 단락의 글을 작성하면, 다음 단락 생성
<img width="1251" alt="image" src="https://github.com/Yeinalee/six/assets/84684759/ba4ed926-b2c1-409f-8f75-35213a8b495e">
* 클라이언트와 생성형 AI가 작성한 글을 바탕으로 이미지 생성 </br> </t> 과거의 기록을 모두 활용하여 영어로 요약하고 영어로 요약한 내용을 바탕으로 이미지 생성
<img width="1132" alt="image" src="https://github.com/Yeinalee/six/assets/84684759/1c4f37e0-dcc8-4e23-b932-f3d49f2b1af3">
