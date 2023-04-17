import traceback
import sys
from flask import request
from flask.views import MethodView
from logger.logger import logger
from views.view_setup import validate_field, format_api_response

from trix_tts_core.trix_tts import TrixVoice


class TrixTTSAPI(MethodView):
    def post(self):
        """
            curl -H "Content-Type: application/json" -X POST -d '{"text":"hi trix"}' http://localhost:7001/trix/tts
        :return:
        """
        try:
            if not request.is_json:
                raise Exception("Missing JSON in request")

            validate_field("text")
            text = request.json.get('text')

            # Initialize trix and generate voice
            tx = TrixVoice().trix_in(text)
            TrixVoice().trix_voice(tx)

            payload = {
                'text': text
            }
            return format_api_response(payload, "success"), 200
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            logger.error(f'Error: {exc_type}, {exc_obj}, {tb[2]}, {tb[1]}, {traceback.format_exc()}')
            return format_api_response(f'Error: {exc_obj}', "error"), 400
