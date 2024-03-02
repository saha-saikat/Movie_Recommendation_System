import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ab4ad38915c7c5d0688d701fe6ccb090'.format(movie_id))
    data=response.json()

    return "https://image.tmdb.org/t/p/w500"+data['poster_path']



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])

    recommended_movie=[]
    recommended_movie_posters=[]
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id


        recommended_movie.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie,recommended_movie_posters

movie_dict = pickle.load(open('movies.pkl','rb'))
movies =pd.DataFrame(movie_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendetion System')

selected_movie_name=st.selectbox(
'How would you like to be contacted?',
    movies['title'].values)



if st.button('Show Recommendation'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])