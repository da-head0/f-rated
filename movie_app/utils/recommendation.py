import pandas as pd
from pymongo import MongoClient
import json


def recommendation_by_title(get_title):
    host = 'cluster0.xc44g.mongodb.net'
    user = 'aimb'
    password = 'mimomimo'
    database_name = 'frated'

    client = MongoClient(f"mongodb+srv://{user}:{password}@{host}/{database_name}?retryWrites=true&w=majority")    # db = client.frated

    # 데이터베이스, 콜렉션 선택
    db = client['frated']
    test = db.movie

    df = pd.DataFrame(list(test.find()))

    df2 = df[['Title', 'Director', 'Actors', 'keywords', 'Genre', 'Awards', 'Year']]

    # Actor, Genre 3개만 남겨 분석
    df2['Actors'] = df['Actors'].str.split(',').str[:3]
    df2['Genre'] = df['Genre'].str.split(',').str[:3]

    # 한 column에 스트링 형태로 합치기
    df2['soup'] = df2['Genre'].astype(str) + df2['Actors'].astype(str) + df2['keywords'].astype(str) + df2['Director'] + df2['Awards']

    df2['soup'] = df2['soup'].astype(str) # 이래야 에러가 안남

    # CountVectorizer를 가져오고 Count Matrix를 생성
    from sklearn.feature_extraction.text import CountVectorizer

    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(df2['soup'])

    # ount_matrix를 기반으로 코사인 유사성 행렬을 계산
    from sklearn.metrics.pairwise import cosine_similarity

    cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

    # DataFrame의 인덱스를 재설정하고 역방향 매핑을 구성
    df2 = df2.reset_index()
    indices = pd.Series(df2.index, index=df2['Title'])

    #Import TfIdfVectorizer from scikit-learn
    from sklearn.feature_extraction.text import TfidfVectorizer

    #TF-IDF Vectorizer 객체를 정의하고. 'the', 'a'와 같은 단어를 제거.
    tfidf = TfidfVectorizer(stop_words='english')

    #데이터를 적합하고 변환하여 필요한 TF-IDF 행렬을 구성
    tfidf_matrix = tfidf.fit_transform(df2['soup'])

    #Output the shape of tfidf_matrix
    tfidf_matrix.shape

    # Import linear_kernel
    from sklearn.metrics.pairwise import linear_kernel

    # Compute the cosine similarity matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    """
    [[1.        , 0.00683247, 0.00448538, ..., 0.00713922, 0.00545785, 0.        ],
    [0.00683247, 1.        , 0.03984185, ..., 0.00198376, 0.00195305, 0.        ],
    [0.00448538, 0.03984185, 1.        , ..., 0.00233544, 0.00229929, 0.        ],
    ...,
    [0.00713922, 0.00198376, 0.00233544, ..., 1.        , 0.08253358, 0.        ],
    [0.00545785, 0.00195305, 0.00229929, ..., 0.08253358, 1.        , 0.01009746],
    [0.        , 0.        , 0.        , ..., 0.        , 0.01009746, 1.        ]]
    cosine_sim은 이런 형태"""

    # 영화 제목을 입력하여 가장 유사한 영화를 출력
    def get_recommendations(get_title, cosine_sim=cosine_sim):
        # Get the index of the movie that matches the title
        idx = indices[get_title]

        # Get the pairwsie similarity scores of all movies with that movie
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 3 most similar movies
        sim_scores = sim_scores[1:4] # 10개도 가능

        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]

        # Return the top 3 most similar movies
        return df2['Title'].iloc[movie_indices]

        """
        823    The Darkest Minds
        878    Wonder Woman 1984
        790           Fast Color
        762          Division 19
        812          Being Frank
        이렇게 뜸
        """
    results = get_recommendations(get_title, cosine_sim2)
    #resultslist = results.to_list() 
    # results.to_string(index=False)
    return results.to_list()


def msg_processor(msg_code):
    '''
    msg_processor returns a msg object with 'msg', 'type'
    where 'msg' corresponds to the message user sees
    and 'type' is the color of the alert element

    codes:
        - 0 : Successfully added to database
        - 1 : User does not exist
        - 2 : Unable to retrieve tweets
        - 3 : Successfully deleted user
    '''

    msg_code = int(msg_code)

    msg_list = [
        (
            'Successfully added to database',
            'success'
        ),
        (
            'Movie does not exist',
            'warning'
        ),
        (
            'Unable to retrieve data',
            'warning'
        ),
        (
            'Successfully deleted Movie',
            'info'
        )
    ]

    return {
        'msg':msg_list[msg_code][0],
        'type':msg_list[msg_code][1]
    }