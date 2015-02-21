# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Name:        NewralNetwork_04.py
# Purpose:      First NewralNetwork Algorizm
#
# Author:     Tomoyuki Nohara
# Created:     08/02/2015
#-------------------------------------------------------------------------

# 演算用にNumPyを、プロット用にmatplotlibをimport
'''
概要
y= 2*x1 + 3*x2
を機会学習で係数を予測する
'''
import os
import numpy as np

'''
前提
+ ベクトルは列ベクトルが基本とする
'''


def predict(Uvec):
	'''
	活性化関数
	@Uvec:	結合された出力ユニット
	'''
	Z=Uvec

	return Z

def combine(X,W):
	'''
	内積関数
	入力ベクトルXと重みベクトルWとを結合する
	@X:	入力ベクトル
	@W:	重みベクトル
	'''
	# ベクトルXとベクトルYとの内積をとる
	Uvec = np.dot(X,W)

	return Uvec

def sqLoss(Y, Z):
	'''
	二乗誤差関数
	@Y:	教師値
	@Z:	出力値
	'''
	R = np.sum( (Y-Z)^2 )
	return R

def deltaWvec(Y,Z,X):
	'''
	デルタルール
	重みベクトルWを更新するための変化量を算出
	'''
	# すべての学習データ対のデルタを二乗加算
	delta = Y-Z	
	dW = lc*delta*X

	return dW

def training():
	'''
	学習要関数
	教師データと、出力結果ZからWの変化値を求め、Wを更新する。
	'''
	# Nは教師データ数、pはユニット数
	N = 10
	for i in range(N):

		deffW[p] = deffW[p] + dW[p][i]
	
	W[p] = w[p] + deffW[p]


def dataModel(X, W0):
	_Y = np.dot(W0, X)
	return _Y


if __name__ == "__main__":
	'''
	ケーススタディ
	y = 2*x1 + 3*x2を考える。
	x1, x2をランダムに選び、yを生成する。
	前提条件
	配列は宣言時にnp.array型で生成
	'''
	os.system("clear")

	# 入力ユニット数
	N = 2
	# 入力ユニット
	# 第一要素はバイアスのため1とするが今回はなし。
	# X = 1
	# 重みベクトル
	# W
	# 教師データ数
	M = 100
	# 学習係数
	lc = 0.00001
	# 学習回数
	Nl = 100

	# データセットの作成
	W0 = np.array((2,3))
	# W0 = np.arange(1,N+1)
	# _X1 = [60,100,80,70,90,0,100,90,10,70]
	# _X2 = [80,10,90,60,70,40,90,10,40,80]
	# _X1 = np.random.random(1,N)
	# _X2 = np.random.random(1,N)
	# X1 = np.array(_X1)
	# X2 = np.array(_X2)
	# X = np.array((X1,X2))
	X = np.random.rand(N,M)
	# print 'X =',X
	# Y = dataModel(X,W0)
	Y = np.dot(W0,X)

	# 重みベクトルの定義
	# _W = [1,1]	# 初期値
	# W = np.array(_W)
	W = np.random.rand(N)

	dd = np.empty([1])
	# print dd


	for lp in range(Nl):
		print '================================='
		print 'lp =', lp

		# 出力データ
		Z = np.dot(W,X)
		# print 'X =', X
		# print 'W =', W
		# print 'Z =', Z
		# print 'Y =', Y

		# デルタ
		d = Y - Z
		# print 'd =', d
		
		# 二乗誤差関数
		_dd = np.sum(d*d)
		dd = np.append(dd,_dd)
		# print 'd^2 =', dd

		# 更新のための重み係数
		_dW = np.ones((N,M))
		# 
		for i in range(N):
			for j in range(M):
				_dW[i,j] = lc * d[j] * X[i,j]
			# dW[i] = np.sum(dW[i])
			# print '_dW[i]', _dW


		# 重みベクトルの更新
		# print 'W =',W
		# W1 = W[0] + np.sum(dW1)
		# W2 = W[1] + np.sum(dW2)
		W = W + np.sum(_dW,1)
		# print 'W =', W
		# print 'W1 =', W1
		# print 'W2 =', W2
		# print 'W =', W

	print '*** 確認 ***'
	print 'W0 =', W0
	print 'W  =', W

	# プロット
	# print dd
	dd = dd[1:len(dd)]
	# print dd(len(dd)-1)
	print dd[dd.size-1]
	# print 'dd =', dd[end]
	# print W

	# import matplotlib.pyplot as plt

	# plt.scatter(dd, marker='o', color='g', s=10)
	# plt.scatter(x2[:, 0], x2[:, 1], marker='o', color='r', s=100)
	# plt.plot(dd)
	# plt.show()


	# fig, (ax1, ax2) = plt.subplots(1, 2)
	# ax1.set_xscale("log")
	# ax1.set_yscale("log")
	# ax1.set_xlim(1e1, 1e3)
	# ax1.set_ylim(1e2, 1e3)
	# ax1.set_aspect(1)
	# ax1.set_title("adjustable = box")
	# ax1.plot(dd)

	# ax2.plot(dd)
	# ax2.plot(np.dot(W,X))
	# ax2.plot(X1,X2)
	# ax2.set_xlim(0,60)
	# plt.draw()
	# plt.show()




