from flask import Flask 

app = Flask(__name__)

# Create a idea repository 

ideas = {
    1 : {
        'id': 1,
        'idea_name':'kaleem',
        'idea_description': 'Python Developer'
    },
    2: {
        'id': 2,
        'idea_name':'shaheem',
        'idea_description':'Data analyst'
    }
}

'''
Create a Restful endpoint for fetching all the ideas
'''

@app.get("/IdeaApp/api/v1/ideas")
def get_all_idea():
    return ideas



if __name__ == '__main__':
    app.run(port=8080)

