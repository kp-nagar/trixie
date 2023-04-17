from views.trix_tts import TrixTTSAPI


def register_urls_in_blueprint(trix_blueprint):
    trix_blueprint.add_url_rule('/trix/tts', view_func=TrixTTSAPI.as_view('trix_tts_api'), methods=['POST'])