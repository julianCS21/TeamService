from dotenv import load_dotenv
from src.core.dependencies import get_settings
import uvicorn
from src.app import application

if __name__ == "__main__":
    load_dotenv()
    settings = get_settings()
    uvicorn.run(application, host="0.0.0.0", port=settings.port)
