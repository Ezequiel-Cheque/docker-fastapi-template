import uvicorn
from pathlib import Path
from src.cashier.app import *

if __name__ == "__main__":
    
    uvicorn.run(
        f"{Path(__file__).stem}:app",
        host="0.0.0.0",
        port=3001,
        reload=True,
        debug=True,
        log_level="info",
        workers=1,
        factory=False
    )