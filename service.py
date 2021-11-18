from flask import Flask, request
import logging as logger
import application
import configuration

app = Flask(__name__)


@app.route('/insertData', methods=['GET'])
def insert_data():
    try:
        string_value = request.args.get("stringName", "")
        result = application.insert_data(string_value)
        response = {
            'status': 'ok',
            'message': 'Data stored successfully',
            'content': result
        }

        return response
    except Exception as e:
        logger.error(str(e))
        message = 'Unable to insert records'
        return message


@app.route('/fetchAllRecords', methods=['GET'])
def fetch_all_records():
    try:
        result_list = application.fetch_all_records()
        response = {
            'status': 'ok',
            'message': 'Fetched successfully',
            'content': result_list
        }

        return response
    except Exception as e:
        logger.error(str(e))
        message = 'Unable to fetch records'
        return message


@app.route('/performOperation', methods=['GET'])
def perform_operation():
    try:
        string_id = request.args.get("stringId", "")
        op_type = request.args.get("opType", "")
        message = application.perform_operation(string_id, op_type)
        response = {
            'status': 'ok',
            'message': message,
            'stringId': string_id
        }
        return response
    except Exception as e:
        logger.error(str(e))
        message = 'Unable to perform given operation'
        return message


@app.route('/fetchOperationCount', methods=['GET'])
def fetch_operation_count():
    try:
        string_id = request.args.get("stringId", "")
        op_list, message = application.fetch_operation_count(string_id)
        response = {
            'status': 'ok',
            'message': message,
            'content': op_list
        }
        return response
    except Exception as e:
        logger.error(str(e))
        message = 'Unable to fetch operation records'
        return message


if __name__ == '__main__':
    app.run(
        host=configuration.app_host,
        port=configuration.app_port
    )