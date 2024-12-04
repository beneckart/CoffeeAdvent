import openai
import os
from openai import OpenAI
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai.api_key)

class CoffeeTasting(BaseModel):
    notes: List[str]

def extract_tasting_notes(message):

    response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "Extract the main tasting notes or flavor descriptors from the following message."},
            #{"role": "system", "content": "The following message describes a coffee tasting. Extract its main tasting notes and flavor descriptors."},
            {"role": "user", "content": message}
        ],
        response_format=CoffeeTasting,
        #max_tokens=1500,
        temperature=0,
        #n=1,
    )
    # Accessing response as a Pydantic model
    tasting = response.choices[0].message.parsed

    return tasting

def get_embeddings(notes): # notes is list
    embeddings = []
    for note in notes:
        response = client.embeddings.create(
            model='text-embedding-3-large', #'text-embedding-ada-002',
            input=note.lower(),
        )
        embeddings.append(response.data[0].embedding)
    return embeddings

if __name__ == '__main__':
    shane_str = """Wee little beans, prob Ethiopian. Light bodied. Got some white floral, jasmine early on and then some serious lemon acidity as it cooled, maybe a little white peach. Black tea, chamomile, lemon. I feel like I could use a cup of coffee to wash this down.

But Ben, in an attempt to try to pad my scores (and to make your work easier), I'll cut the fluff and just go with: black tea, chamomile, lemon.'"""

    mom_str = """On her way to Orange Beach to go shelling"""

    notes = extract_tasting_notes(mom_str)
    print(notes)
