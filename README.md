# This is a sample Hello World application from Python FastAPI

```hcl
1. This used the Open API standard
2. You can access the open API via https://localhost:8000/docs
3. You can disable OpenAPI docs by setting openapi_url to an empty string in production. like below
    from pydantic import BaseSettings

    class Settings(BaseSettings):
        openapi_url: str = ""

```
### Setup in Linux

```hcl
    pip install -r requirements.txt
    sh startup.sh
```

## Detailed documents are pointed here https://devdocs.io/fastapi/
