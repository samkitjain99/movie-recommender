import streamlit as st
import pandas as pd
import difflib

# Load data
movies_data = pd.read_csv('movies_data.csv')
import joblib

# Load the similarity matrix using joblib (matches how it was saved)
similarity = joblib.load("similarity_compressed.pkl")

st.title('🎬 Movie Recommender System')
st.write("Find similar movies by typing your favorite movie name below.")

# Input movie name
movie_name = st.text_input("Enter movie name:")

if st.button("Recommend"):
    list_of_all_titles = movies_data['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if not find_close_match:
        st.error("❌ No similar movie found. Try again.")
    else:
        close_match = find_close_match[0]
        index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
        similarity_score = list(enumerate(similarity[index_of_the_movie]))
        sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

        st.subheader(f"🎥 Movies similar to: **{close_match}**")
        for i, movie in enumerate(sorted_similar_movies[1:11], start=1):
            index = movie[0]
            title_from_index = movies_data[movies_data.index == index]['title'].values[0]
            st.write(f"{i}. {title_from_index}")




