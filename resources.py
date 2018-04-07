from flask import request, jsonify
from flask_restful import Resource
from travelers import Member
import logging

"""
Setting up logger
"""
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)




class Calculate(Resource):
    def __init__(self):
        self.travelers = []
        self.total_expense = None
        self.output_file = None

    def get(self):
        pass

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
                                'message' : 'content is not in json format'}), 204
        except ValueError as e:
            logger.warning(e)
            return jsonify({'status' : 'failed', 
                            'message' : 'missing json content'}), 204
        """
        iterate over a dict and append each member to 
        a list of travelers
        """
        for name, expense in content['travelers']:
            self.travelers.append(Member(name = name, expenses = expense))
        

        
