# 🎬 Movie Recommender System

A simple yet powerful content-based movie recommender built with **Streamlit**, **Pandas**, and **Python**.  
It recommends 5 similar movies based on your selection using cosine similarity.  
Hosted on **Streamlit Cloud** with large model files downloaded via **Google Drive**.

---

## 🚀 Live Demo

🌐 [Try it on Streamlit Cloud](https://movie-recommendersystem-ggujhsrxblkku8tahasjky.streamlit.app/)  

---

## 📌 Features

- 🔎 Searchable dropdown for movie selection
- 🧠 Cosine similarity–based recommendation
- ☁️ Loads large `.pkl` file (`similarity.pkl`) from Google Drive using `gdown`
- 📱 Simple, responsive UI with Streamlit

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **Streamlit** – UI framework
- **Pandas** – data manipulation
- **Pickle** – for loading precomputed models
- **gdown** – to download `similarity.pkl` from Google Drive

---

## 📁 Project Structure

movie-recommender-system/
├── app.py # Main Streamlit app
├── movie_dict.pkl # Pickled movie metadata dictionary
├── requirements.txt # Dependencies
└── README.md # Project documentation


## 📂 similarity.pkl Handling

- **File size**: ~180MB (too large for GitHub)
- **Storage**: Hosted on **Google Drive**
- **Download logic**: Auto-downloads at runtime using `gdown`

Make sure your Google Drive file has **"Anyone with the link"** access enabled.
