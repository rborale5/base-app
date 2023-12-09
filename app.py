# import main Flask class and request object
from flask import Flask, request, jsonify, json
import threading
import requests, time


# create the Flask app
app = Flask(__name__)



@app.route('/slackCommand', methods=['POST'])
def handle_slack():
    query = request.form.get('text')
    response_url = request.form.get('response_url')
    response = {
        "response_type": "ephemeral",
        "text": "Working on your query: " + str(query),
    }
    send_immediate_response(response, response_url)

    def background_task(response_url):
        result = "Here's a response!!!"
        # Add ur logic here... and assign to following response.
        # time.sleep(60)
        response = {
            "response_type": "ephemeral",
            "text": str(result),
        }
        send_final_response(response, response_url)
    background_thread = threading.Thread(target=background_task, args=(response_url,))
    background_thread.start()
    return '', 202

# @app.route('/slackConfluence', methods=['POST'])
# def handle_confluence():
#     page_ids = request.form.get('text')
#     print(page_ids)
#     page_list = page_ids.split(',')

#     response_url = request.form.get('response_url')
#     # print(query)
#     # print("respone url: " + response_url)
#     # Immediate acknowledgment
#     response = {
#         "response_type": "ephemeral",
#         "text": "upload task started",
#     }
#     send_immediate_response(response, response_url)

#     def background_task(response_url):
#         result = llm_client.store_confluence_docs(page_list)
#         print(result)
#         response = {
#             "response_type": "ephemeral",
#             "text": str(result),
#         }
#         send_final_response(response, response_url)
#     background_thread = threading.Thread(target=background_task, args=(response_url,))
#     background_thread.start()

#     return '', 200

# @app.route('/uploadFile', methods=['POST'])
# def handle_file():
#     if 'file' not in request.files:
#         return 'No file part in the request.', 400
#     file = request.files['file']
#     if file.filename == '':
#         return 'No selected file.', 400
#     filename = secure_filename(file.filename)
#     if not filename.endswith('.pdf'):
#         return 'Only PDF File upload supported', 500

#     file.save('/tmp/' + filename)

#     def background_task():
#         llm_client.update_vector_with_pdf(filename)
#     background_thread = threading.Thread(target=background_task)
#     background_thread.start()

#     # llm_client.update_vector_with_pdf(filename)
#     return 'File successfully uploaded.', 200

# @app.route('/query', methods=['POST'])
# def handle_post():
#     data  = request.get_json()
#     query = data.get("query")
#     return  llm_client.query_llm(query)

def send_immediate_response(response, response_url):
    # Send the immediate acknowledgment to Slack
    requests.post(response_url, json=response)

def send_final_response(response, response_url):
    # Send the final response to Slack
    # headers = {'Content-type': 'application/json'}
    requests.post(response_url, json=response)

# @app.route('/kbconfluence', methods=['POST'])
# def handle_addition_of_conflucence_page():
#     data  = request.get_json()
#     page_ids = data.get("page_ids")
#     def background_task():
#         result = llm_client.store_confluence_docs(page_ids)
#         print(result)
#     background_thread = threading.Thread(target=background_task)
#     background_thread.start()

#     # return json.dumps(llm_client.store_confluence_docs(page_ids))
#     return json.dumps({"message": "upload task started."})

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return 'No file part in the request.', 400
#     file = request.files['file']
#     if file.filename == '':
#         return 'No selected file.', 400
#     filename = secure_filename(file.filename)
#     if not filename.endswith('.pdf'):
#         return 'Only PDF File upload supported', 500
#     file.save('/tmp/' + filename)

#     def background_task():
#         llm_client.update_vector_with_pdf(filename)
#     background_thread = threading.Thread(target=background_task)
#     background_thread.start()

#     return 'File successfully uploaded.', 200

@app.route('/health/ready')
def handle_readiness_check():
    resp = jsonify(health="healthy")
    resp.status_code = 200
    return resp

@app.route('/health/live')
def handle_liveness_check():
    resp = jsonify(health="healthy")
    resp.status_code = 200
    return resp


if __name__ == '__main__':
    # run app in debug mode on port 8000
    app.run(host='0.0.0.0', debug=True, port=8000)