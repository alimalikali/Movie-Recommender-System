import pickle
import streamlit as st
import requests

# Custom CSS for beautiful styling
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .movie-card {
        background: white;
        border-radius: 15px;
        padding: 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    
    .movie-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    .movie-title {
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 0.5rem;
        text-align: center;
    }
    
    .stat-card h3 {
        color: #2c3e50 !important;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .stat-card h2 {
        color: #34495e !important;
        font-weight: bold;
        font-size: 1.5rem;
    }
    
    .selectbox-container h3 {
        color: #2c3e50 !important;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .movie-card h3 {
        color: #2c3e50 !important;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .movie-card p {
        color: #34495e !important;
        font-weight: 500;
        margin-bottom: 0.3rem;
    }
    
    .recommendation-section h2 {
        color: #2c3e50 !important;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .recommendation-section p {
        color: #34495e !important;
        font-weight: 500;
    }
    
    .recommendation-section {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: bold;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    
    .selectbox-container {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
    }
    
    .stat-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        flex: 1;
        margin: 0 0.5rem;
    }
    
    .footer {
        text-align: center;
        padding: 2rem;
        color: #7f8c8d;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

def fetch_poster(movie_id):
    try:
        url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    except:
        return "https://via.placeholder.com/300x450/cccccc/666666?text=No+Poster"

def recommend(movie, movies, similarity):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:13]:  # Changed from 1:6 to 1:13 to get 12 recommendations
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

# Main App
def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🎬 Movie Recommender System</h1>
        <p>Discover your next favorite movie with AI-powered recommendations</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data
    try:
        movies = pickle.load(open('movie_list.pkl','rb'))
        similarity = pickle.load(open('similarity.pkl','rb'))
        
        # Stats section
        st.markdown("""
        <div class="stats-container">
            <div class="stat-card">
                <h3>📊 Total Movies</h3>
                <h2>{}</h2>
            </div>
            <div class="stat-card">
                <h3>🎯 Recommendations</h3>
                <h2>12 per movie</h2>
            </div>
            <div class="stat-card">
                <h3>🌟 AI Powered</h3>
                <h2>ML Based</h2>
            </div>
        </div>
        """.format(len(movies)), unsafe_allow_html=True)
        
        # Movie selection section
        st.markdown("""
        <div class="selectbox-container">
            <h3>🎭 Select Your Movie</h3>
        </div>
        """, unsafe_allow_html=True)
        
        movie_list = movies['title'].values
        selected_movie = st.selectbox(
            "Choose a movie you love to get personalized recommendations:",
            movie_list,
            index=0
        )
        
        # Show selected movie info
        if selected_movie:
            selected_movie_data = movies[movies['title'] == selected_movie].iloc[0]
            col1, col2 = st.columns([1, 2])
            
            with col1:
                poster_url = fetch_poster(selected_movie_data.movie_id)
                st.image(poster_url, width=200, caption=selected_movie)
            
            with col2:
                st.markdown(f"""
                <div class="movie-card">
                    <h3>🎬 {selected_movie}</h3>
                    <p><strong>Genre:</strong> {selected_movie_data.get('genres', 'N/A')}</p>
                    <p><strong>Release Date:</strong> {selected_movie_data.get('release_date', 'N/A')}</p>
                    <p><strong>Rating:</strong> {selected_movie_data.get('vote_average', 'N/A')}/10</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Recommendation button
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button('🎯 Get Recommendations', use_container_width=True):
                with st.spinner('🎬 Finding the perfect movies for you...'):
                    recommended_movie_names, recommended_movie_posters = recommend(selected_movie, movies, similarity)
                
                # Recommendations section
                st.markdown("""
                <div class="recommendation-section">
                    <h2>🎉 Your Personalized Recommendations</h2>
                    <p>Based on your selection of <strong>{}</strong>, here are movies you might love:</p>
                </div>
                """.format(selected_movie), unsafe_allow_html=True)
                
                # Display recommendations in a beautiful grid (4x3 layout)
                for row in range(3):  # 3 rows
                    cols = st.columns(4)  # 4 columns per row
                    for col_idx, col in enumerate(cols):
                        movie_idx = row * 4 + col_idx
                        if movie_idx < len(recommended_movie_names):
                            with col:
                                st.markdown(f"""
                                <div class="movie-card">
                                    <div class="movie-title">{recommended_movie_names[movie_idx]}</div>
                                </div>
                                """, unsafe_allow_html=True)
                                st.image(recommended_movie_posters[movie_idx], width=150, caption=recommended_movie_names[movie_idx])
        
        # Footer
        st.markdown("""
        <div class="footer">
            <p>🎬 Powered by Machine Learning & TMDB API</p>
            <p>Discover amazing movies tailored just for you!</p>
        </div>
        """, unsafe_allow_html=True)
        
    except FileNotFoundError:
        st.error("❌ Error: Could not find the required data files (movie_list.pkl, similarity.pkl)")
        st.info("Please make sure the pickle files are in the same directory as this app.")
    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")

if __name__ == "__main__":
    main()





