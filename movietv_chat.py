from tmdbv3api import TMDb, Movie
import gradio as gr

TMDB_API_KEY = "08b21329bec4932b0077ddf67292b4a2"  
tmdb = TMDb()
tmdb.api_key = TMDB_API_KEY
movie = Movie()

def get_movie_details(query):
    """Fetch movie details from TMDb API based on a query."""
    try:
        search_results = movie.search(query)
        print("Debugging search_results:", search_results) 
        if search_results:
            top_result = search_results[0]
            print("Debugging top_result:", top_result.__dict__)  
            return (
                f"Title: {top_result.title}\n"
                f"Release Date: {top_result.release_date}\n"
                f"Overview: {top_result.overview}\n"
            )
        else:
            return "Sorry, I couldn't find any movies matching your query."
    except Exception as e:
        return f"Error fetching movie details: {str(e)}"

def generate_response(user_input):
    """Generate a response based on user input."""
    
    tmdb_response = get_movie_details(user_input)

    
    if "Error fetching" in tmdb_response or "Sorry," in tmdb_response:
        return (
            "This query might require ChatGPT for a better response.\n"
            "Please open ChatGPT, input the following question, and paste the response here:\n\n"
            f"User Query: \"{user_input}\""
        )

    
    return tmdb_response


iface = gr.Interface(
    fn=generate_response,
    inputs="text",
    outputs="text",
    title="Movie/TV Show Chatbot",
    description=(
        "Ask me about movies or tv shows! For example: \"Interstellar\" "
    ),
)

if __name__ == "__main__":
    iface.launch()
