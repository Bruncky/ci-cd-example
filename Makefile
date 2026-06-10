PROJECT := hip-voyager-421200
IMAGE := test-app
REGION := europe-west1
DOCKER_REPO_NAME := my-docker-repo
TAG := 0.1

IMAGE_URI := $(REGION)-docker.pkg.dev/$(PROJECT)/$(DOCKER_REPO_NAME)/$(IMAGE):$(TAG)

default: pylint pytest

# -------------------------
# Python checks
# -------------------------

pylint:
	find . -iname "*.py" -not -path "./tests/*" | xargs -n1 pylint --output-format=colorized; true

pytest:
	PYTHONDONTWRITEBYTECODE=1 pytest -v --color=yes

# -------------------------
# Docker
# -------------------------

build:
	docker build --platform=linux/amd64 -t $(IMAGE_URI) .

push: build
	docker push $(IMAGE_URI)

run:
	docker run --rm -p 8080:8080 $(IMAGE_URI)

# -------------------------
# Debug helpers
# -------------------------

print-image:
	@echo $(IMAGE_URI)
