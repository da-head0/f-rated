###
http://f-rated.herokuapp.com/

# 🎥 머신러닝 기반 여성 영화 추천 사이트
![image](https://img.shields.io/badge/python-3.8.8-blue) ![image](https://img.shields.io/badge/-flask--mongoengine-lightgrey) ![image](https://img.shields.io/badge/-mongodb-brightgreen) ![image](https://img.shields.io/badge/pandas-1.2.3-blue) ![image](https://img.shields.io/badge/scikit--learn-0.24.1-yellow)


---
<image src="https://user-images.githubusercontent.com/61692777/112993181-e0ac0a00-91a3-11eb-9ced-5d1d3a8c688c.png" width="700">


역대 흥행 영화 분석 결과, **여성 감독은 전체의 3%, 여성 각본가는 전체의 5.4%에 불과합니다.** 

(IMDb 데이터셋 바탕, 1940-2020년 영화 기반, 전체 흥행 영화 탑 1000 분석)

이러한 영화 산업의 불균형을 타파하기 위해, 
2014년 영국의 바스 영화제의 프로듀서 홀리 타퀴니는 F-Rated 지표를 만들었습니다.

<image src="https://user-images.githubusercontent.com/61692777/112964576-6bc8d800-9183-11eb-98c5-381522f9feab.png" width="700">
---

본 사이트는 위 3가지 조건 중 2가지 이상을 만족하는 영화 890종을 바탕으로

영화의 키워드, 장르, 배우, 감독, 수상실적을 분석해 취향에 맞는 영화를 추천합니다.

<image src= "https://user-images.githubusercontent.com/61692777/112998138-b446bc80-91a8-11eb-9a14-a7153fea557b.png" width="700">
<image src="https://user-images.githubusercontent.com/61692777/112998258-d50f1200-91a8-11eb-9071-b2acd55e9886.png" width="700">


---
### 영화 제목, IMDb ID, 키워드로 영화 검색
<image src="https://user-images.githubusercontent.com/61692777/112994695-77c59180-91a5-11eb-8678-594551c505c9.png" width="700">

---
### 여성 영화 데이터베이스
<image src="https://user-images.githubusercontent.com/61692777/112994538-52388800-91a5-11eb-9979-c116c0872fd7.png" width="700">
<image src="https://user-images.githubusercontent.com/61692777/112994790-93309c80-91a5-11eb-9e44-ee5533d49eba.png" width="700">

---
### 머신러닝 알고리즘
- sklearn의 CountVectorizer로 영화의 키워드+장르+배우+감독+수상실적을 조합해 단어의 등장 빈도를 계산하고
- Cosine Similarity 방식으로 영화별 유사도를 측정, 가장 유사한 영화 3개를 추천합니다. 
- TF-IDF Vectorizer 대신 CountVectorizer를 사용한 이유는 배우/감독이 더 많은 영화에서 출연했다고 중요도를 낮추지 않기 위해서입니다.

---
### 스키마
<image src="https://user-images.githubusercontent.com/61692777/112963202-1b9d4600-9182-11eb-9258-611eae250151.png" width="700">
Mongodb, flask-mongoengine 사용

---
### 사용한 API, 패키지
- [Movie Database (IMDB Alternative) API Documentation](https://rapidapi.com/rapidapi/api/movie-database-imdb-alternative?endpoint=apiendpoint_843d3708-42a9-4240-8a68-2ced0372c20f)
- [IMDbPY](https://imdbpy.github.io/)

### 참고
- [Getting Started with a Movie Recommendation System](https://www.kaggle.com/ibtesama/getting-started-with-a-movie-recommendation-system)
