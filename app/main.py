import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse, JSONResponse
from helpers.sentiment_analyzer import extract_entities_and_analyze_sentiment, analyze_for_given_entities
from helpers.entity_extraction import get_entities


app = FastAPI(
    title="Sentity",
    description="Detect entities and analyze sentiment in a sentence",
    version="0.0.1",
)


@app.get("/", include_in_schema=False)
def read_docs():
    return RedirectResponse(url="/docs")


@app.post("/analyze")
def read_docs(data: dict = {"sentence" : "", "entities" : None, "perform_auto_entity_detection" : False}):
    entities = data.get("entities") if not data["perform_auto_entity_detection"] else get_entities(data.get("sentence"))
    if entities is None:
        return JSONResponse(status_code=400, content={"error": "No entities found"})
    
    return JSONResponse(analyze_for_given_entities(data.get("sentence"), entities))


#app.include_router(
#    addresses.router,
#    prefix="",
#    tags=["entities", "sentiment"],
#)

#if __name__ == "__main__":
#    import sys
#    port = int(sys.argv[1])
#    uvicorn.run("main:app", host="0.0.0.0", port=port,
#                debug=True, log_level="info", reload=True)
