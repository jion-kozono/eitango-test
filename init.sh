docker-compose run \
  --entrypoint "poetry init \
    --name app \
    --dependency fastapi \
    --dependency uvicorn[standard]" \
  app