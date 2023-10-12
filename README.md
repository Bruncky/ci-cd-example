# CI/CD Example

This is a classic and very simple example of how CI/CD can be used to improve your workflow. Take a few minutes to look at the files to understand what's going on, but the gist of it is this:

- Inside `api/` there is a very simple API that has nothing more than the root address
- Using a `Dockerfile`, we are creating an image containing the API for later deployment
- `tests/` contains the sample test you've already seen in the lecture, but it now also contains `Dockerfile.test`, which will be used in our CI workflow
- The CI workflow, found inside `.github/workflows`, uses this specialized `Dockerfile.test` to build our image and run the tests against it

Now, we have two tasks:

1. Use some CD magic to connect it to Google Cloud Run
2. Make a change to any of the files to test the entire CI/CD workflows
