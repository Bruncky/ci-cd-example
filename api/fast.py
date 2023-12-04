from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Allows all origins
    allow_credentials = True,
    allow_methods=['*'],  # Allows all methods
    allow_headers=['*'],  # Allows all headers
)

@app.get('/')
def root():
    response = {
        'greeting': 'Servus, griaß di!',    # This is a typical Bavarian greeting ;)
        'timestamp': datetime.now()
    }

    return response


# PROJECT="le-wagon-1437"
# IMAGE="new-cd-example"
# REGION="europe-west1"
# DOCKER_REPO_NAME="my-first-repo"
# TAG="0.1"
# IMAGE_URI=${REGION}-docker.pkg.dev/${PROJECT}/${DOCKER_REPO_NAME}/${IMAGE}:${TAG}
