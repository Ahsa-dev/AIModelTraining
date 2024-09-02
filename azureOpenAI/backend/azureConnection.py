import os
import sys
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../credentials')))
from config import DEPLOYMENT_NAME, ENDPOINT_URL, SEARCH_KEY, SEARCH_ENDPOINT, SEARCH_INDEX

endpoint = os.getenv("ENDPOINT_URL", ENDPOINT_URL)
deployment = os.getenv("DEPLOYMENT_NAME", DEPLOYMENT_NAME)
search_endpoint = os.getenv("SEARCH_ENDPOINT", SEARCH_ENDPOINT)
search_key = os.getenv("SEARCH_KEY", SEARCH_KEY)
search_index = os.getenv("SEARCH_INDEX_NAME", SEARCH_INDEX)

token_provider = get_bearer_token_provider(
  DefaultAzureCredential(),
  "https://cognitiveservices.azure.com/.default")
      
client = AzureOpenAI(
  azure_endpoint=endpoint,
  azure_ad_token_provider=token_provider,
  api_version="2024-05-01-preview",
)

def azureRequest(company):
  # return f"me llegó una compañía mela: {company}"
  completion = client.chat.completions.create(
    model=deployment,
    messages= [
    {
      "role": "user",
      "content": f"¿Qué sabes sobre {company}?"
    }],
    max_tokens=800,
    temperature=0.4,
    top_p=0,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False,
    extra_body={
      "data_sources": [{
        "type": "azure_search",
        "parameters": {
          "endpoint": f"{search_endpoint}",
          "index_name": f"{search_index}",
          "semantic_configuration": "default",
          "query_type": "semantic",
          "fields_mapping": {},
          "in_scope": True,
          "role_information": "Eres un Especialista en Evaluación de Propuestas de Proyectos, tu objetivo principal de esta posición es evaluar la capacidad técnica y la experiencia de las empresas que se postulan para proyectos de desarrollo impulsados por el Banco Interamericano de Desarrollo (BID), asegurando que los seleccionados cumplan con los más altos estándares de calidad y experiencia en proyectos similares. Resume cuál es su experiencia con proyectos sociales, casos de éxito y sus años de experiencia en el mercado.",
          "filter": None,
          "strictness": 3,
          "top_n_documents": 5,
          "authentication": {
            "type": "api_key",
            "key": f"{search_key}"
          }
        }
      }]
    }
  )
  return completion.model_dump_json(indent=2)