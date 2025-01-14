import streamlit as st



select_movie = st.Page(
    page="view/select_movie.py",
    title="Choose The movie",
    icon="🤔",
    default=True
)



recommended_movies = st.Page(
    page="view/recommended_movies.py",
    title="Movies Recommended",
    icon="🎬",
    default=False
)


pg = st.navigation(pages=[select_movie,recommended_movies])

pg.run()