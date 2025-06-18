import streamlit as st
import pandas as pd
import pickle
import os
import gdown

# ========== Google Drive Download ==========
SIMILARITY_FILE = "similarity.pkl"

# Replace below with your actual Google Drive file ID
GDRIVE_FILE_ID = "1gagpSKa5xW_XB99zNJuxU650gQkM4Kd_"  # <-- CHANGE THIS
GDRIVE_URL = f"https://drive.google.com/uc?id={GDRIVE_FILE_ID}"

# Download the similarity file if not found
if not os.path.exists(SIMILARITY_FILE):
    with st.spinner("Downloading similarity matrix..."):
        gdown.download(GDRIVE_URL, SIMILARITY_FILE, quiet=False)

# ========== Load Data ==========
with open('movie_dict.pkl', 'rb') as f:
    movies_dict = pickle.load(f)

movies = pd.DataFrame(movies_dict)

with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

# ========== Recommender Logic ==========
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended = [movies.iloc[i[0]].title for i in movie_list]
    return recommended

# ========== Streamlit UI ==========
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Select a movie:",
    movies['title'].values
)

if st.button("Recommend"):
    st.subheader("Top 5 Recommendations:")
    for movie in recommend(selected_movie):
        st.write("✅", movie)
