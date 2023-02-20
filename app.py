from flask import Flask, render_template, jsonify
import openai
import numpy as np  # standard math module for python
from pprint import pprint

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


openai.api_key = open_file('openaiapikey.txt')


def gpt3_completion(prompt, engine='text-davinci-002', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['Mycos:', 'USER:']):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop)
    text = response['choices'][0]['text'].strip()
    return text


if __name__ == '__main__':
    conversation = list()
    while True:
        user_input = input('USER: ')
        conversation.append('USER: %s' % user_input)
        text_block = '\n'.join(conversation)
        prompt = open_file('prompt_chat.txt').replace('<<BLOCK>>', text_block)
        prompt = prompt + '\nMycos:'
        response = gpt3_completion(prompt)
        print('Mycos:', response)
        conversation.append('Mycos: %s' % response)

app = Flask (__name__)

STRAINS = [
  {
    'id':1,
    'title': 'White Widow',
    'type': 'Indica',
    'effects': 'sedative'
  },
  {
    'id':2,
    'title': 'Grand Daddy Purp (GDP)',
    'type': 'Indica',
    'effects': 'sedative'
  },
{
    'id':3,
    'title': 'OG',
    'type': 'Indica',
    'effects': 'sedative'
  },
{
    'id':4,
    'title': 'Gelato 41',
    'type': 'Indica',
    'effects': 'sedative'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         strains=STRAINS)

  @app.route("/api/strains")
  def list_strains():
    return jsonify(STRAINS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
