from app import app


@app.route('/posts', methods=['GET'])
def get_all_posts():
    return "Getting all posts"


@app.route('/posts/<id>', methods=['GET'])
def get_post(id):
    return "Getting post with id " + str(id)


@app.route('/users/<id>/posts', methods=['GET'])
def get_user_posts(id):
    return "Getting all posts of a user with id " + str(id)


@app.route('/posts', methods=['POST'])
def create_post():
    return "Creating a new post"
