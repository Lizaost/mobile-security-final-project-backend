from app import app


@app.route('/users', methods=['GET'])
def get_all_users():
    return "Getting all users"


@app.route('/users', methods=['POST'])
def create_user():
    return "Creating a new user"


@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    return "Getting a user with id " + str(id)


@app.route('/users/<id>', methods=['PUT'])
def edit_user(id):
    return "Editing a user with id " + str(id)