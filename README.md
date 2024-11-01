# MEDICHAT

A simple real-time chatbot that utilises the power of vector database to retrieve
relevant medical articles similar to the diagnosis or symptoms prompted to the bot.
For this project, I have used ChromaDB as the vector database together with the 
model `all-MiniLM-L6-v2` for encoding document-data during the hydration process as 
well as the query text. This was made to work using the `sentence_transformer` module.

`django-channels` and `WebSocket` are responsible for its real-time feature.

## Installation

From your CLI, run the following code

```
git clone https://github.com/tha-orakkle/medichat.git
```

Create and activate a virtual environment

- **Linux users**
```
virtualenv venv
source venv/bin/activate
```
- For **Windows**, substitute the second line of code with this
```
.\venv\Scripts\activate.bat
```
Install all depencies
```
pip install -r requirements.txt
```

Run Program
```
python manange.py runserver
```


## Author
- Paul Adegbiran-Ayinoluwa (adegbiranayinoluwa.paul@yahoo.com)