# ΔG Modeling Report (v2)

**Dataset file:** `dataset_without_vec.parquet`  
**iso2vec used:** `False`  

## Test-set metrics (sorted by lowest RMSE)

| Model | MAE | RMSE | R² |
|---|---|---|---|
| **RandomForest** | 1.991 | 2.679 | 0.662 |
| **XGB_tuned** | 2.053 | 2.759 | 0.642 |
| **CatBoost** | 2.061 | 2.801 | 0.631 |
| **LGBM** | 2.174 | 2.817 | 0.627 |
| **HGB** | 2.172 | 2.892 | 0.607 |
| **XGB_baseline** | 2.090 | 2.894 | 0.606 |
| **Stacking** | 2.343 | 3.079 | 0.554 |
| **Ridge** | 3.093 | 3.867 | 0.297 |
