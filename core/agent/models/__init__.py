from .google import *

support_models = {
    "google_genai":{
        "get_model":get_google_genai_model,
        "list":["google_genai:gemini-2.5-flash-lite"]
    }
}   