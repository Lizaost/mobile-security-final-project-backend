from app import app


@app.route('/comments/<id>', methods=['GET'])
def get_comment(id):
    return "Getting a comment with id " + str(id)


@app.route('/posts/<id>/comments', methods=['GET'])
def get_post_comments(id):
    return "Getting comments for post with id " + str(id)


@app.route('/comments', methods=['POST'])
def create_comment():
    return "Creating a new comment"
