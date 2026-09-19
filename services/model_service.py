from nassau_analysis.models.predict import load_selected_model
_model=None
def get_model():
    global _model
    if _model is None: _model=load_selected_model()
    return _model
