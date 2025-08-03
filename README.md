# 🎬 Movie Recommender System

A beautiful, AI-powered movie recommendation system built with Streamlit and Machine Learning.

## ✨ Features

- **12 Personalized Recommendations** - Get 12 movie suggestions based on your selection
- **Beautiful UI** - Modern, responsive design with gradients and animations
- **Movie Posters** - Real movie posters from TMDB API
- **Movie Information** - Detailed movie data including genres, ratings, and release dates
- **AI-Powered** - Machine learning-based recommendation algorithm

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd AIML
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the app**
```bash
streamlit run app.py
```

4. **Open your browser**
Navigate to `http://localhost:8501`

## 📦 Deployment Options

### Option 1: Streamlit Cloud (Recommended)

1. **Push your code to GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Deploy on Streamlit Cloud**
- Go to [share.streamlit.io](https://share.streamlit.io)
- Sign in with GitHub
- Click "New app"
- Select your repository and set the path to `app.py`
- Click "Deploy"

### Option 2: Heroku

1. **Create Heroku app**
```bash
heroku create your-app-name
```

2. **Add buildpacks**
```bash
heroku buildpacks:add heroku/python
```

3. **Deploy**
```bash
git push heroku main
```

### Option 3: Railway

1. **Connect your GitHub repo to Railway**
2. **Set environment variables if needed**
3. **Deploy automatically**

## 📁 Project Structure

```
AIML/
├── app.py                 # Main Streamlit application
├── movie_list.pkl        # Movie data (pickle file)
├── similarity.pkl        # Similarity matrix (pickle file)
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
└── tmdb_5000_movies.csv # Original movie dataset
```

## 🔧 Configuration

### Environment Variables (Optional)
- `TMDB_API_KEY`: Your TMDB API key (currently using demo key)

### Data Files Required
- `movie_list.pkl`: Contains movie information
- `similarity.pkl`: Contains similarity matrix for recommendations

## 🎯 How It Works

1. **User selects a movie** from the dropdown
2. **System loads movie data** from pickle files
3. **AI algorithm finds similar movies** using cosine similarity
4. **Fetches movie posters** from TMDB API
5. **Displays 12 recommendations** in a beautiful grid layout

## 🛠️ Technologies Used

- **Frontend**: Streamlit
- **Backend**: Python
- **ML**: Scikit-learn (Cosine Similarity)
- **Data**: TMDB API, Pandas
- **Styling**: Custom CSS with gradients and animations

## 📊 Features

- ✅ Beautiful, modern UI
- ✅ 12 movie recommendations
- ✅ Movie posters and details
- ✅ Responsive design
- ✅ Error handling
- ✅ Loading animations
- ✅ Hover effects

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues:
1. Check that all required files are present
2. Ensure dependencies are installed
3. Verify your internet connection (for poster fetching)
4. Check the console for error messages

---

**Made with ❤️ using Streamlit and Machine Learning** 