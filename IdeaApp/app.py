from flask import Flask,request

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

'''
Create a Restful enpoint for creating an new idea
'''
@app.post("/IdeaApp/api/v1/ideas")
def create_idea():
    # Login to create idea
    try :
        # first read the request body
        request_body = request.get_json()

        # check if passed idea is not present already
        if request_body["id"] and request_body["id"] in ideas:
            return 'idea with the same id is already present',400
        # Insert the passed idea into the ideas dictionary
        ideas[request_body["id"]] = request_body
        # Return the response saying idea saved successfully
        return 'Idea created and saved successfully',201
    except KeyError:
        return 'id is missing',400
    except:
        return "Some internal server error",500

if __name__ == '__main__':
    app.run(port=8080)

