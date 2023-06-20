# qa-systems
How To run fastapi :
1.Download app.py,dockerfile, and requirements.txt in the same directory
2.To run fastapi open the terminal with the location where app.py is saved.run the following code:
                      Uvicorn app: app –reload
3.Inside the browser localhost:8000/docs

How to run in Docker:
1.Open the terminal with the location where dockerfileis save to build the docker image .
        docker build -t fastapi-app .
2. docker run -p 9000:8000 fastapi2-app uvicorn app:app --host 0.0.0.0 --port 8000
3.Inside the browser type localhost:9000

