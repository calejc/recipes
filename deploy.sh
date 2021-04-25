sudo docker build -t recipe-parser .
gcloud builds submit --tag gcr.io/recipe-parser-311719/recipe-parser:latest
gcloud run deploy --image gcr.io/recipe-parser-311719/recipe-parser:latest --platform managed
