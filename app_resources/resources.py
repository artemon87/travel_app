from flask import request, jsonify
from flask_restful import Resource
from .travelers import Member
from .resource_helpers import disbursement, read_from_file
import logging


"""
Setting up logger
"""
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
FORMATTER = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s -%(lineno)s: \t%(message)s")
console_handler = logging.StreamHandler()
console_handler.setFormatter(FORMATTER)
logger.addHandler(console_handler)



class Calculate(Resource):
    def __init__(self):
        self.travelers = []

    def get(self):
        data = read_from_file(name = 'final_disbursement.json')
        return jsonify({'data' : data})

    def put(self):
        pass

    def post(self):
        content = None
        try:
            if request.json:
                content = request.json
            else:
                """
                Only json content is supported
                """
                return jsonify({'status' : 'failed', 
                                'message' : 'content is not in json format'}) # 204
        except ValueError as e:
            logger.warning(e)
            return jsonify({'status' : 'failed', 
                            'message' : 'missing json content'}) # 204
        """
        iterate over a dict and append each member to 
        a list of travelers
        """
        try:
            for name, expense in content['travelers'].items():
                self.travelers.append(Member(name = name, expenses = expense))
        except KeyError as e:
            logger.warning(e)
            return jsonify({'status' : 'failed', 
                            'message' : "missing traveler's data"})

        result = disbursement(arr = self.travelers)
        return jsonify({'status' : 'success', 'message' : 'data was submitted', 'result' : result})
        
        

        
