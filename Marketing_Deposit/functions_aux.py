import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict, cross_val_score
from imblearn.under_sampling import NearMiss
import seaborn as sns
import matplotlib.pyplot as plt
import visuals


d_colors = {
    pair[0]: pair[1] for pair in zip(['yes', 'no'], sns.color_palette()[:2])
}

colors = [
    d_colors['yes'],
    d_colors['no']
]


def categorize(balance: int) -> str:
    """Seja b = balance. Aplica a classificação:
    b < 0: negativo,
    0 <= b < 2500: low,
    2500 <= b < 5000: moderate,
    5000 <= b < 10,000: high,
    10,000 <= b: very high.

    Args:
        balance (int): valor do patrimônio.

    Returns:
        str: categoria associada ao valor do patrimônio.
    """
    if balance < 0:
        return 'negative'
    elif 0 <= balance < 2500:
        return 'low'
    elif 2500 <= balance < 5000:
        return 'moderate'
    elif 5000 <= balance < 10_000:
        return 'high'
    return 'very high'


def prop_yes(df: pd.DataFrame, col: str, r: str='k'):
    """Recebe um dataframe, uma coluna e um parâmetro de retorno.
    Percorre as saídas da coluna e retorna a proporção dessas saí-
    das, em forma de dicionário {saída: proporção} com o valor 'yes'
    na coluna 'y' (classe). A depender do parâmetro r, retorna uma
    lista ou um dicionário.

    Args:
        df (pd.DataFrame): dataframe,
        col (str): coluna de df a serem avaliadas as proporções,
        r (str, optional): r = k (key) ou v (values), retornará
        uma lista, r = d (dict), retornará um dicionário.
        Defaults to 'k'.

    Returns:
        Lista ou dicionário:
        r = k: lista com as saídas de col,
        r = v: lista com as proporções,
        r = d: dicionário {saída: proporção}.
    """
    if len(df[col].unique()) == 2:
        p = {
            k: df.loc[df[col] == k].shape[0] / \
                df.shape[0]
            for k in ['no', 'yes']
        }
    else:
        p = {}
        for out in df[col].unique():
            df_ = df.loc[df[col] == out, 'y']
            n_total = df_.shape[0]
            n_yes = df_[df_ == 'yes'].shape[0]

            p[out] = n_yes / n_total

    if r == 'k':
        return list(p.keys())
    elif r == 'v':
        return list(p.values())
    return p


def array_scalers(Xs: list) -> list:
    """Recebe uma lista de arrays e os retorna escalados
    (normalizados) com StandarScaler.

    Args:
        Xs (list): lista de arrays a serem escalados.

    Returns:
        list: lista de arrays escalados.
    """
    scaled_Xs = []
    for X in Xs:
        scaler = StandardScaler().fit(X)
        X = scaler.transform(X)

        scaled_Xs.append(X)

    return scaled_Xs


def col_encoder(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """Aplica o LabelEncoder às colunas informadas em cols.

    Args:
        df (pd.DataFrame): dataframe original,
        cols (list): lista das colunas a serem pré-processadas
        com LabelEncoder.

    Returns:
        pd.DataFrame: dataframe com as colunas em cols pré-
        processadas. Antes de ser retornado, o df será conver-
        tido completamente para int32.
    """
    df_ = df[cols].apply(LabelEncoder().fit_transform)
    df2 = df.drop(cols, axis=1)

    df = pd.merge(
        df_,
        df2,
        how='inner',
        left_index=True,
        right_index=True
    )
    df = df.astype('int32')

    return df


def plot_features(features: np.array, cols: np.array) -> None:
    """Plota um barplot das features na ordem de cols.

    Args:
        features (np.array): features (atributos),
        cols (np.array): array com os respectivos nomes dos
        atributos.
    """
    # transformando os coeficientes em um array 1D
    list_coefs = features.reshape(len(cols), 1)

    # criando um dicionário com par (coluna, valor coef)
    d_coefs = {
        par[0]: par[1][0] for par in zip(cols, list_coefs)
    }

    # reordenando em termos dos valores
    d_coefs = {
        k: v for k, v in sorted(d_coefs.items(), key=lambda i: i[1], reverse=True)
    }

    f, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(
        y=[k for k in d_coefs.keys()],
        x=[v for v in d_coefs.values()]
    );


def plot_scores(clf, X: np.array, y: np.array, k: int=5, text_xy: list=[], bins: int='auto') -> None:
    """Plota um histograma de cross_val_score(clf, X, y, cv=k), com
    informações sobre sua média, mediana e desvio padrão (std). Na
    variável text_xy é informada a posição do bloco de texto contendo
    as informações mencionadas.

    Args:
        clf ([type]): classificador,
        X (np.array): array de dados,
        y (np.array): array das classes,
        k (int, optional): k-fold para avaliação do cross_val_score.
        Defaults to 5,
        text_xy (list, optional): posição inicial do bloco de texto
        referente à média, mediana e std. Se não for informada, tais
        informações não serão exibidas. Defaults to [],
        bins (int, optional): número de bins do histograma. Defaults
        to 'auto'.
    """
    scores = cross_val_score(clf, X, y, cv=k)


    f, ax = plt.subplots(figsize=(8, 6))

    sns.histplot(scores, bins=bins);
    plt.title('Cross Validation');
    plt.xlabel('Score');

    if len(text_xy) != 0:
        ax.text(
            text_xy[0], text_xy[1], f'Média: {round(scores.mean(), 4)}',
            fontsize=12
        );
        ax.text(
            text_xy[0], text_xy[1] - .3, f'Mediana: {round(np.median(scores), 4)}',
            fontsize=12
        );
        ax.text(
            text_xy[0], text_xy[1] - .6, f'Std: {round(scores.std(), 4)}',
            fontsize=12
        );


def plot_report_confusion(y_test: np.array, y_pred: np.array) -> None:
    """Plota classification_report(y_test, y_pred) e, em seguida,
    a matriz de confusão.

    Args:
        y_test (np.array): array dos dados de teste,
        y_pred (np.array): array dos dados preditos.
    """
    print(metrics.classification_report(y_test, y_pred))

    print(
        pd.crosstab(
            y_test, y_pred,
            rownames=['Real'],
            colnames=['     Predito'],
            margins=True
        )
    )


def score_metrics(
    model, X_train: np.array, X_test: np.array, y_train: np.array,
    y_test: np.array, y_pred: np.array) -> None:
    """Imprime as métricas de MAE e RSME entre y_test e y_pred e,
    em seguida, imprime a acurácia dos dados de teste e treino.

    Args:
        model ([type]): classificador,
        X_train (np.array): array dos dados de treino,
        X_test (np.array): array dos dados de teste,
        y_train (np.array): array das classes de treino,
        y_test (np.array): array das classes de teste,
        y_pred (np.array): array das classes preditas.
    """
    print(
        f'MAE: {metrics.mean_absolute_error(y_test, y_pred)}\n'
        f'RSME: {np.sqrt(metrics.mean_squared_error(y_test, y_pred))}'
    )

    print(
        'Acurácia (teste, treino): '
        f'({model.score(X_test, y_test)}, {model.score(X_train, y_train)})'
    )


def full_preprocess(df: pd.DataFrame, which: str='tt') -> tuple:
    """Realiza o pré-processamento total do dataframe:
    separação entre dados e classe,
    rebalancea das classes com NearMiss;
    se which = 'pip', os dados serão retornados;
    se which = 'tt', os dados serão separados em treino e
    teste e normalizados com array_scalers;
    se which = 'cv', somente o array de dados será norma-
    lizado com array_scaler.

    Args:
        df (pd.DataFrame): dataframe a ser pré-processado
        which (str, optional): parâmetro que controla o grau
        de pré-processamento. Defaults to 'tt'.

    Returns:
        tuple: dados e classes pré-processados: X,y
    """
    # separação de dados e classe
    X = df.drop('y', axis=1)
    y = df['y']

    # rebalanceando as classes
    X, y = NearMiss().fit_resample(X, y)

    if which == 'pip':
        return X, y
    elif which == 'tt':
        # separação em treino e test (estratificado)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, stratify=y
        )

        # escalando-os
        X_train, X_test = array_scalers([X_train, X_test])
        return X_train, X_test, y_train, y_test
    elif which == 'cv':
        X = array_scalers([X])[0]
        return X, y
    else:
        raise 'Invalid preprocess: which -> tt: train_test; cv: cross_val or pip: pipeline'
