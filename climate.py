import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go

CO2 = np.array(
    [288.6455, 288.7726, 288.9053, 289.0437, 289.188, 289.3384, 289.4954, 289.6592, 289.8304, 290.0092, 290.1957,
     290.3899, 290.5917, 290.801, 291.0174, 291.2405, 291.4697, 291.7044, 291.9442, 292.1885, 292.4368, 292.6884,
     292.943, 293.1996, 293.4572, 293.7147, 293.9709, 294.2247, 294.4751, 294.721, 294.9626, 295.2014, 295.439,
     295.6769, 295.9167, 296.1599, 296.4082, 296.6631, 296.9261, 297.1977, 297.4772, 297.7637, 298.0562, 298.3535,
     298.6545, 298.9584, 299.2648, 299.5734, 299.8839])

dCO2 = CO2[1:] - CO2[0:-1]  # difference in CO2 over years

Sun = np.array(
    [4.3, 4.08, 4.19, 4.38, 4.87, 4.73, 4.76, 4.55, 4.53, 4.39, 4.43, 4.49, 4.5, 4.39, 4.59, 4.71, 4.76, 4.34, 4.3,
     4.15, 3.86, 3.69, 3.61, 3.58, 3.53, 3.7, 3.99, 4.11, 4.07, 4.03, 3.99, 3.99, 4.19, 4.28, 4.4, 4.44, 4.54, 4.72,
     4.9, 5.06, 5.06, 5.15, 5.1, 5.15, 5.03, 5.02, 5.08, 5.14, 5.26])

dSun = Sun[1:] - Sun[0:-1]

SOx = np.array(
    [3.8, 4.1, 4.1, 4.2, 4.3, 4.8, 5.2, 5.5, 5.4, 5.6, 5.7, 5.8, 5.8, 6.2, 6.7, 7.2, 7.7, 8.3, 8.3, 8.2, 8.3, 8.8,
     9.5, 9.7, 10.3, 10.7, 10.8, 10.7, 11.1, 11.7, 12.1, 12.6, 13.3, 14.5, 15.5, 16, 16.6, 17.7, 17.9, 18.8, 20.2,
     22.2, 21.4, 22.1, 23.1, 22.9, 25, 26.6, 25.3])

dSOx = SOx[1:] - SOx[0:-1]

OT = np.array(
    [0.0007, 0.0003, 0.0001, 0.0005, 0.0005, 0.0005, 0.0012, 0.0029, 0.0019, 0.0012, 0.0061, 0.0052, 0.0031, 0.0019,
     0.001, 0.0006, 0.0005, 0.0259, 0.0779, 0.1092, 0.0721, 0.037, 0.0218, 0.0284, 0.039, 0.0299, 0.0216, 0.0093,
     0.0034, 0.0013, 0.0182, 0.0168, 0.012, 0.0045, 0.0017, 0.0006, 0.0097, 0.0464, 0.0265, 0.0189, 0.0101, 0.0091,
     0.0102, 0.0039, 0.003, 0.0016, 0.0192, 0.024, 0.0098])

dOT = OT[1:] - OT[0:-1]

Temp = np.array(
    [-0.201, -0.307, -0.198, -0.285, -0.315, -0.361, -0.211, -0.279, -0.393, -0.428, -0.406, -0.128, -0.002, -0.294,
     -0.277, -0.247, -0.226, -0.307, -0.364, -0.335, -0.264, -0.369, -0.31, -0.172, -0.389, -0.331, -0.416, -0.453,
     -0.383, -0.36, -0.163, -0.156, -0.343, -0.224, -0.139, -0.233, -0.364, -0.448, -0.49, -0.375, -0.307, -0.496,
     -0.522, -0.495, -0.458, -0.485, -0.406, -0.415, -0.241])

dTemp = Temp[1:] - Temp[0:-1]

CET = np.array(
    [9.65, 9.02, 10.38, 9.62, 8.98, 9.05, 9.75, 8.98, 9.3, 9.43, 9.51, 9.17, 9.24, 7.42, 9.09, 8.56, 9.45, 9.02, 9.83,
     8.57, 8.7, 8.27, 8.22, 8.99, 8.73, 8.49, 8.17, 9.97, 9.3, 8.65, 9.33, 9.42, 10.07, 9.69, 9.56, 9.11, 8.83, 9.32,
     9, 9.13, 9.43, 8.84, 9.27, 8.55, 9.17, 10.05, 9.36, 9.8, 9.88])

dCET = CET[1:] - CET[0:-1]

SOI = np.array(
    [-0.16, -0.03, -0.88, 0.55, -0.15, -0.15, 1.91, 0.08, 0.59, 0.27, 0.44, -1.8, 0.17, 1.27, 0.79, -0.59, -0.6,
     -0.25, -0.38, -0.68, 0.7, 0.47, -1.27, 0.16, 0.56, -0.28, 0.52, 0.99, 0.21, -0.25, -1.55, -0.68, 0.57, 0.16,
     -0.65, 0.07, 0.1, 0.47, 0.39, -1.79, 0.21, -0.2, 0.28, 0.29, 1.26, -0.64, -0.98, -0.68, -0.93])

dSOI = SOI[1:] - SOI[0:-1]

NAO = np.array(
    [0.31, -0.07, 1.58, 0.54, -0.42, -0.12, -0.8, 0.12, 0.47, -0.11, -0.22, 0.05, -0.92, -0.36, -0.01, 0.09, 1.09,
     0.64, 0.58, 0.19, -0.32, -0.64, 0.01, 0.64, 0.6, 0.03, -0.64, -0.1, 0.87, -0.24, 0.35, 0.85, 0.53, 0.04, 0.08,
     -0.4, -0.43, 0.87, 0.62, 0.1, 0.28, 0.56, 0.63, -0.1, -0.05, 0.48, 0.21, 0.87, 0.8])

dNAO = NAO[1:] - NAO[0:-1]

Year = np.array(
    [1866, 1867, 1868, 1869, 1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883,
     1884, 1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901,
     1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914])


def MovingLinReg(F, A, b):
    number_of_rows = len(A)
    number_of_columns = len(A[0])
    print(number_of_rows, number_of_columns)

    # Coefficient matrix X
    X = np.zeros((number_of_rows, number_of_columns))
    for i in range(number_of_rows - number_of_columns):
        X[i] = (np.matmul(np.linalg.inv(A[i:i + number_of_columns][:]), b[i:i + number_of_columns]))

    for i in range(number_of_columns):
        X[i + number_of_rows - number_of_columns] = np.matmul(
            np.linalg.inv(np.roll(A, -i, axis=0)[-number_of_columns:][:]),
            np.roll(b, -i, axis=0)[-number_of_columns:])

    X = np.roll(X, number_of_columns // 2, axis=0)

    print(X, '\n\n\n')

    TotalYearlyAbsoluteChange = np.sum(np.abs(A) * np.abs(X), axis=1)
    print(TotalYearlyAbsoluteChange)

    IndividualContributionMatrix = np.abs(X * A) / TotalYearlyAbsoluteChange[:, None]

    print(IndividualContributionMatrix)

    df = pd.DataFrame(IndividualContributionMatrix, columns=F, index=Year[1:])

    print(df["CO2"])
    # print(df.iloc[:,0])

    # sns.barplot(x="CO2", y="Year", data=[df.index, df["CO2"]])

    '''fig, axarr = plt.subplots(nrows=len(df.columns), ncols=1)
    colors = ['r', 'b', 'g', 'y', 'k']
    for i in range(len(df.columns)):
        axarr[i].bar(df.index, df.iloc[:, i], color=colors[i])
        axarr[i].set_ylabel(df.columns[i])

    fig.tight_layout()
    plt.show()
    # plt.bar(df.index, df.iloc[:,i])
    # plt.show()'''

    # extract color palette, the palette can be changed
    pal = list(sns.color_palette(palette='viridis', n_colors=len(F)).as_hex())

    fig = go.Figure()
    for d, p in zip(ForcingFactors, pal):
        fig.add_trace(go.Scatter(x=Year[1:],
                                 y=df[d],
                                 name=d,
                                 line_color=p,
                                 fill=None))  # tozeroy

    fig.show()

    fig = make_subplots(rows=len(df.columns), cols=1, shared_xaxes=False, subplot_titles=df.columns)
    row = 1
    for trace in df.columns:
        fig.add_trace(go.Bar(x=df.index, y=df[trace], name=trace), row=row, col=1)
        row += 1
    fig.show()

if __name__ == '__main__':
    datamatrix = np.column_stack((dCO2, dSun, dSOx, dOT, dSOI))
    tempdata = dTemp
    ForcingFactors = ['CO2', 'Sun', 'SOx', 'OT', 'SOI']
    MovingLinReg(ForcingFactors, datamatrix, tempdata)
