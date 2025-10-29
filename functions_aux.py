import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report, precision_recall_fscore_support




def get_confusion_values(df: pd.DataFrame, y_true: str, y_pred: str) -> pd.DataFrame:
    df_ = df.copy()

    df_['tp'] = (df_[y_true] == 1) & (df_[y_pred] == 1)
    df_['tn'] = (df_[y_true] == 0) & (df_[y_pred] == 0)
    df_['fp'] = (df_[y_true] == 0) & (df_[y_pred] == 1)
    df_['fn'] = (df_[y_true] == 1) & (df_[y_pred] == 0)

    return df_


def get_confusion_metrics(df: pd.DataFrame, y_true: str, y_pred: str) -> dict:
    df_ = get_confusion_values(df, y_true, y_pred)

    tpr = df_['tp'].sum() / (df_[y_true] == 1).sum()
    tnr = df_['tn'].sum() / (df_[y_true] == 0).sum()
    fpr = df_['fp'].sum() / (df_[y_true] == 0).sum()
    fnr = df_['fn'].sum() / (df_[y_true] == 1).sum()
    npv = df_['tn'].sum() / (df_['tn'].sum() + df_['fn'].sum())
    acc = (df_['tp'].sum() + df_['tn'].sum()) / len(df_)
    ppv = df_['tp'].sum() / (df_['tp'].sum() + df_['fp'].sum())
    f1 = 2 * (ppv * tpr) / (ppv + tpr)

    return {
        'tpr': tpr,
        'tnr': tnr,
        'fpr': fpr,
        'fnr': fnr,
        'npv': npv,
        'acc': acc,
        'ppv': ppv,
        'f1': f1
    }


def eval_cnfn(y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    tp, fp, fn, tn = confusion_matrix(y_true, y_pred, normalize='pred').ravel()

    tpr = tp / (tp + fn) if (tp + fn) > 0 else 0
    tnr = tn / (tn + fp) if (tn + fp) > 0 else 0
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
    fnr = fn / (fn + tp) if (fn + tp) > 0 else 0
    npv = tn / (tn + fn) if (tn + fn) > 0 else 0
    acc = (tp + tn) / (tp + tn + fp + fn) if (tp + tn + fp + fn) > 0 else 0
    ppv = tp / (tp + fp) if (tp + fp) > 0 else 0
    f1 = 2 * (ppv * tpr) / (ppv + tpr) if (ppv + tpr) > 0 else 0

    print('Classification Report:')
    print(classification_report(y_true, y_pred, target_names=['0', '1']))

    return {
        'tpr': tpr,
        'tnr': tnr,
        'fpr': fpr,
        'fnr': fnr,
        'npv': npv,
        'acc': acc,
        'ppv': ppv,
        'f1': f1
    }
