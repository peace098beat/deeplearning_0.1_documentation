# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Name:        NewralNetwork_02.py
# Purpose:      First NewralNetwork Algorizm
#
# Author:     Tomoyuki Nohara
#
# Created:     27/01/2015
# URL:          http://tjo.hatenablog.com/entry/2013/05/01/190247
#-------------------------------------------------------------------------

# 演算用にNumPyを、プロット用にmatplotlibをimport
import numpy as np
import matplotlib.pyplot as plt
import time


def predict(wvec, xvec):
    '''
    活性化関数・アクティベーション関数
    識別関数の本体：y=W'xを計算している
    function: 0 or 1
    '''
    out = np.dot(wvec, xvec)
    if out >= 0:
        res = 1
    else:
        res = -1
    return [res, out]


def train(wvec, xvec, label):
    '''
    学習部：識別関数に学習データを順繰りに入れて、
    重みベクトルを更新する
    '''
    [res, out] = predict(wvec, xvec)
    c = 0.5  # 学習係数
    if out * label < 0:
        wtmp = wvec + c * label * xvec
        return wtmp
    else:
        return wvec


def createDatasets(item_num):

    # 学習データ
    # 第一象限と第三象限に50個ずつ
    x1_1 = np.ones(int(item_num / 2)) + 10 * \
        np.random.random(int(item_num / 2))
    x1_2 = np.ones(int(item_num / 2)) + 10 * \
        np.random.random(int(item_num / 2))
    x2_1 = np.ones(int(item_num / 2)) - 10 * \
        np.random.random(int(item_num / 2))
    x2_2 = np.ones(int(item_num / 2)) - 10 * \
        np.random.random(int(item_num / 2))
    z = np.ones(int(item_num / 2))  # バイアス項

    # 学習データを1つのマトリクスにまとめる
    # x1 = np.c_[x1_1, x1_2, z]
    # x2 = np.c_[x2_1, x2_2, z]
    class_1 = np.c_[x1_1, x1_2, z]
    class_2 = np.c_[x2_1, x2_2, z]
    class_x = np.array(np.r_[class_1, class_2])

    # 教師ラベルを1 or -1で振って1つのベクトルにまとめる
    label1 = np.ones(int(item_num / 2))
    label2 = -1 * np.ones(int(item_num / 2))
    label_x = np.array(np.r_[label1, label2])
    # print label_x

    return [class_x, label_x, class_1, class_2]


if __name__ == '__main__':

    item_num = 10  # 学習データは100個
    loop = 10  # 収束判定はしてない。エイヤでループ
    init_wvec = [1, -1, 1]  # 重み関数の初期値

    # データセットの生成
    [class_x, label_x, class_1, class_2] = createDatasets(item_num)

    # 重みベクトルの生成
    wvec = np.vstack((init_wvec, init_wvec))

    plt.ion()
    plt.figure()

    # ループの回数分だけ繰り返しつつ、重みベクトルを学習させる
    for j in range(loop):
        for i in range(item_num):
            wvec_new = train(wvec[-1], class_x[i, :], label_x[i])
            wvec = np.vstack((wvec, wvec_new))

    w = wvec[-1]

    # 分離直線を引く
    x_fig = range(-15, 16)
    y_fig = [- (w[1] / w[0]) * xi - (w[2] / w[1]) for xi in x_fig]

    # プロット
    plt.scatter(class_1[:, 0], class_1[:, 1], marker='o', color='g', s=100)
    plt.scatter(class_2[:, 0], class_2[:, 1], marker='o', color='r', s=100)
    plt.plot(x_fig, y_fig)
    plt.show()







