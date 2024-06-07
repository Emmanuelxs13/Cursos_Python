# En este ejercicio, intentaremos identificar datos atípicos, basados en datos de consumo, una relativa geografía de consumo y nivel salarial:

# Importamos las librerías necesarias:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
