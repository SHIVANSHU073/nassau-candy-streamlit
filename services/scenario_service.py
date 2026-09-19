from nassau_analysis.simulation.features import build_scenario_row
from nassau_analysis.data.public import read_csv
from .model_service import get_model
import pandas as pd
def factories(): return read_csv("factory_coordinates.csv")
def product_mapping(): return read_csv("product_factory_mapping.csv")
def scenario_predictions(product,region,ship_mode,order_year,order_month):
    model=get_model(); mapping=product_mapping()
    current=mapping.loc[mapping["product_name"]==product,"factory"].iloc[0]
    rows=[]
    for factory in factories()["factory"]:
        X=build_scenario_row(product,region,ship_mode,factory,order_year,order_month)
        rows.append({"factory":factory,"predicted_recorded_lead_time_days":float(model.predict(X)[0]),"current_factory":factory==current})
    out=pd.DataFrame(rows); baseline=out.loc[out["current_factory"],"predicted_recorded_lead_time_days"].iloc[0]
    out["delta_vs_current_days"]=out["predicted_recorded_lead_time_days"]-baseline
    out["simulated_improvement_days"]=-out["delta_vs_current_days"]
    out["evidence_type"]="Model-based counterfactual proxy"; out["confidence_score"]=0.25
    return out,current
