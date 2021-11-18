import logging as logger
import uuid
import storage_layer

storage_layer_obj = storage_layer.StringManipulationStorage()


def insert_data(string_value):
    """
    Function to insert the string into database
    :param string_value:
    :return:
    """
    try:
        object_id = unique_id_generator('sm')
        string_obj = {
            'id': object_id,
            'val': string_value
        }
        storage_layer_obj.insert_data(string_obj)
        return object_id

    except Exception as ex:
        logger.error(str(ex))
        raise Exception(str(ex))


def unique_id_generator(prefix):
    """
    Function to generate unique_id
    :param doc_type:
    :param prefix:
    :return:
    """
    try:
        uid = '{}_{}'.format(prefix, str(uuid.uuid4().hex))
        return uid
    except Exception as ex:
        status_message = "Failed in unique ID generation: ", str(ex)
        logger.error(status_message)
        raise Exception(str(ex))


def fetch_all_records():
    """
    Function to all the string from database
    :return:
    """
    try:
        string_list = storage_layer_obj.fetch_all_records()
        final_list = []
        for each_record in string_list:
            each_record.pop('_id', None)
            final_list.append(final_list)
        return string_list

    except Exception as ex:
        logger.error(str(ex))
        raise Exception(str(ex))


def perform_operation(string_id, op_type):
    """
    Function to perform given operation on string
    :param string_id:
    :param op_type:
    :return:
    """
    try:
        string_record = storage_layer_obj.fetch_record_by_id(string_id)
        string_value = string_record.get('val', '')
        operated_string = ""
        message = "No such string record found"

        if string_record:
            if op_type.lower() == 'reverse':
                operated_string = reverse_string(string_value)
            elif op_type.lower() == 'reverse_word':
                operated_string = reverse_string_by_words(string_value)
            elif op_type.lower() == 'flip':
                operated_string = flip_string(string_value)
            elif op_type.lower() == 'sort':
                operated_string = sort_string(string_value)
            else:
                message = "Operation not defined"
        if operated_string:
            operations = string_record.get('op', [])
            op_obj = {
                'opType': op_type,
                'val': operated_string
            }
            operations.append(op_obj)
            string_record['op'] = operations
            storage_layer_obj.update_record_by_id(string_record)
            message = "String record updated successfully"

        return message

    except Exception as ex:
        logger.error(str(ex))
        raise Exception(str(ex))


def reverse_string(string_value):
    """
    Function to reverse a given string
    :param string_value:
    :return:
    """
    try:
        return string_value[::-1]
    except Exception as ex:
        logger.error(str(ex))
        raise Exception(str(ex))


def reverse_string_by_words(string_value):
    """
    Function to reverse a string by its words
    :param string_value:
    :return:
    """
    try:
        word_list = string_value.split(' ')
        return ' '.join(reversed(word_list))
    except Exception as ex:
        logger.error(str(ex))
        raise Exception(str(ex))


def flip_string(string_value):
    """
    Function to flip a string from its half
    :param string_value:
    :return:
    """
    try:
        length_of_string = int(len(string_value))
        first_half = string_value[:int(length_of_string/2)]
        second_half = string_value[int(length_of_string/2):]
        return second_half+first_half

    except Exception as ex:
        logger.error(str(ex))
        raise Exception(str(ex))


def sort_string(string_value):
    """
    Function to sort a given string
    :param string_value:
    :return:
    """
    try:
        return ''.join(sorted(string_value))
    except Exception as ex:
        logger.error(str(ex))
        raise Exception(str(ex))


def fetch_operation_count(string_id):
    """
    Function to fetch all operations performed
    :param string_id:
    :return:
    """
    try:
        storage_record = storage_layer_obj.fetch_record_by_id(string_id)
        operation_record = storage_record.get('op', [])
        if operation_record:
            message = "Successfully fetched list of operations"
        else:
            message = "No performed operations found"

        return operation_record, message

    except Exception as ex:
        logger.error(str(ex))
        raise Exception(str(ex))