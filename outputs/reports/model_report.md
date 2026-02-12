# ΔG Modeling Report (v2)

**Dataset file:** `dataset_with_vec.parquet`  
**iso2vec used:** `True`  

## Test-set metrics (sorted by lowest RMSE)

| Model | MAE | RMSE | R² |
|---|---|---|---|
| **LGBM** | 2.056 | 2.737 | 0.648 |
| **HGB** | 2.123 | 2.775 | 0.638 |
| **XGB_tuned** | 2.052 | 2.787 | 0.635 |
| **CatBoost** | 2.078 | 2.826 | 0.624 |
| **RandomForest** | 2.151 | 2.838 | 0.621 |
| **Stacking** | 2.152 | 2.839 | 0.621 |
| **XGB_baseline** | 2.149 | 2.870 | 0.612 |
| **Ridge** | 3.041 | 3.829 | 0.310 |
