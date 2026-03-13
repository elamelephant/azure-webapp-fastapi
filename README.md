# This is an Sample Hello World application from Python FastAPI

```hcl
1. This used Open API standared
2. you can accesss open API via https://localhost:8000/docs
3. you can disable You can disable OpenAPI docs by setting openapi_url to an empty string in production. like below
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
