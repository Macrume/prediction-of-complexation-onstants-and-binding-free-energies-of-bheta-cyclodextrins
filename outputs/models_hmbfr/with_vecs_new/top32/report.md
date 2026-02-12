# Modeling Report – with_vecs_new / top32

**Samples:** 980  
**Features:** 32  

## Test-set metrics (sorted by lowest RMSE)

| Model | MAE | RMSE | R² |
|---|---|---|---|
| **LGBM** | 2.0052 | 2.7230 | 0.6684 |
| **HGB** | 2.0199 | 2.7646 | 0.6582 |
| **XGB_tuned** | 2.0658 | 2.7905 | 0.6518 |
| **XGB_baseline** | 2.0826 | 2.8889 | 0.6268 |
| **RandomForest** | 2.2066 | 2.9284 | 0.6165 |
| **CatBoost** | 2.2029 | 3.0027 | 0.5968 |
| **Stacking** | 2.2886 | 3.0826 | 0.5750 |
| **Ridge** | 2.7789 | 3.6410 | 0.4072 |
