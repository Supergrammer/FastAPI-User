### Create and Activate anaconda environment
# conda create --file environment.yaml
# conda activate FastAPI-User

if [ $# -ne 1 ]; then
    echo "[Usage] runserver.sh mode (development/production)"
    exit 0
fi

if [ $1 = "development" ]; then
    ### Run FastAPI-User Back-end Server development mode
    MODE="development" uvicorn app.main:app --reload

elif [ $1 = "production" ]; then
    ### Run FastAPI-User Back-end Server production mode
    MODE="production" uvicorn app.main:app --host 0.0.0.0 --port 80 --workers 4
    
else
    echo "[Usage] runserver.sh mode (development/production)"
    exit 0
fi