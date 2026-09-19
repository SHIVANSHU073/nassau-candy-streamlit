# Nassau Candy Distributor — Streamlit

Interactive decision-support application for the Nassau Candy factory reallocation project.

## Architecture
The application consumes the reusable `nassau-candy-analysis` Python package from GitHub rather than duplicating the analytical workflow.

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

The raw order-level CSV is intentionally excluded.

## Model integration
The analysis repository contains the benchmark metrics and a compact packaged Gradient Boosting deployment artifact used by the application. The benchmark metrics and deployment artifact are therefore documented separately.

## Important interpretation
Historical values, model predictions and counterfactual simulations are kept distinct. Alternative-factory scenarios are model-based proxies because the supplied data contains no within-product factory variation and no factory capacity or logistics-cost constraints.
