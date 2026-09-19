from nassau_analysis.data.public import read_csv, read_json
from nassau_analysis.models.predict import load_model_metrics, load_metadata
def audit(): return read_json("data_audit.json")
def region_summary(): return read_csv("region_summary.csv")
def product_summary(): return read_csv("product_summary.csv")
def ship_mode_summary(): return read_csv("ship_mode_summary.csv")
def priority_segments(): return read_csv("priority_segments.csv")
def model_metrics(): return load_model_metrics()
def model_metadata(): return load_metadata()
