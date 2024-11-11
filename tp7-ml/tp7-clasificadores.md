## Clasificador aleatorio

|                | Predicted Positive | Predicted Negative |
|----------------|--------------------|--------------------|
| Actual Positive| 357 (True Positive)| 355 (False Negative) |
| Actual Negative| 2844 (False Positive)| 2826 (True Negative) |

| Métrica       | Fórmula                                  | Valor   |
|---------------|------------------------------------------|---------|
| Precision      | TP / (TP + FP)                           | 0.1116  |
| Accuracy     | (TP + TN) / (TP + TN + FP + FN)          | 0.4987  |
| Sensitivity  | TP / (TP + FN)                           | 0.5014  |
| Specificity | TN / (TN + FP)                           | 0.4982  |

## Clasificador por clase mayoritaria
|                | Predicted Positive | Predicted Negative |
|----------------|--------------------|--------------------|
| Actual Positive| 0 (True Positive)| 712 (False Negative) |
| Actual Negative| 0 (False Positive)| 5670 (True Negative) |

| Métrica       | Valor       |
|---------------|-------------|
| Accuracy      | 0.888       |
| Precision     | Indefinido  |
| Sensitivity   | 0           |
| Specificity   | 1           |

