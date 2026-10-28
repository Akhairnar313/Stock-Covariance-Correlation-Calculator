import numpy as np
import pandas as pd


def print_precision(values):
    print(values.to_string(float_format=lambda value: f"{value:.10f}"))


def calculate_sample_means(matrix):
    return matrix.mean(axis=0)


def calculate_covariance_matrix(matrix):
    return (matrix.T @ matrix) / (matrix.shape[0] - 1)


def calculate_correlation_matrix(covariance):
    covariance_values = covariance.to_numpy() if isinstance(covariance, pd.DataFrame) else np.asarray(covariance)
    diagonal_values = np.sqrt(np.diag(covariance_values))
    d_matrix = np.diag(diagonal_values)
    inverse_d_matrix = np.linalg.inv(d_matrix)
    correlation_values = inverse_d_matrix @ covariance_values @ inverse_d_matrix

    if isinstance(covariance, pd.DataFrame):
        return pd.DataFrame(correlation_values, index=covariance.index, columns=covariance.columns)

    return correlation_values


def print_return_analysis(label, returns):
    means = calculate_sample_means(returns)
    returns_diff = returns - means
    covariance = calculate_covariance_matrix(returns_diff)
    correlation = calculate_correlation_matrix(covariance)

    print(f"\n-------------------------------{label}------------------------------------------\n")
    print_precision(returns)
    print(f"\n-------------------------------SAMPLE MEANS ({label})------------------------------------------\n")
    print_precision(means)
    print(f"\n-------------------------------MEAN DIFFERENCE RETURNS ({label})------------------------------------------\n")
    print_precision(returns_diff)
    print(f"\n-------------------------------COVARIANCE MATRIX ({label})------------------------------------------\n")
    print_precision(covariance)
    print(f"\n-------------------------------CORRELATION MATRIX ({label})------------------------------------------\n")
    print_precision(correlation)