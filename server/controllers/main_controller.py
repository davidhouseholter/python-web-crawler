
from asyncio import create_task
import os
import redis
from rq import Queue, Connection
from flask import render_template, Blueprint, jsonify, request, current_app, send_from_directory

from server.tasks.start_spider import start_spider


main_controller = Blueprint("main", __name__,)

# @main_controller.route("/", methods=["GET"])
# def home():
#     return render_template("main/home.html")

# Path for our main Svelte page
@main_controller.route("/", methods=["GET"])
def base():
    #root_dir = os.path.dirname(os.getenv())
    return send_from_directory(os.path.join('..', 'client', 'public'), 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@main_controller.route("/<path:path>")
def home(path):
    return send_from_directory(os.path.join('..', 'client', 'public'), path)

@main_controller.route("/tasks", methods=["POST"])
def run_task():
    content = request.json
    print(content['seed'])
    task_type = content["type"]
    seed = content["seed"]
    print(seed)
    with Connection(redis.from_url(current_app.config["REDIS_URL"])):
        q = Queue()
        #task = q.enqueue(create_task, task_type)
        task = q.enqueue(start_spider, seed)
    if task:
        response_object = {
            "status": "success",
            "data": {
                "task_id": task.get_id(),
                "task_status": task.get_status(),
                "task_result": task.result,
            },
        }
    else:
        response_object = {"status": "error"}
    return jsonify(response_object), 202


@main_controller.route("/tasks/<task_id>", methods=["GET"])
def get_status(task_id):
    with Connection(redis.from_url(current_app.config["REDIS_URL"])):
        q = Queue()
        task = q.fetch_job(task_id)
    if task:
        response_object = {
            "status": "success",
            "data": {
                "task_id": task.get_id(),
                "task_status": task.get_status(),
                "task_result": task.result,
            },
        }
    else:
        response_object = {"status": "error"}
    return jsonify(response_object)
