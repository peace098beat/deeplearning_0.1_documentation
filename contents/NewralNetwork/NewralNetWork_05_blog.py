# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Name:        NewralNetwork_04.py
# Purpose:      First NewralNetwork Algorizm
#
# Author:     Tomoyuki Nohara
# Created:     08/02/2015
#-------------------------------------------------------------------------
# ipython notebook --pylab inline
import numpy as np

if __name__ == "__main__":
	'''
	ケーススタディ
	y = 2*x1 + 3*x2を考える。
	x1, x2をランダムに選び、yを生成する。
	前提条件
	配列は宣言時にnp.array型で生成
	'''

	# 入力ユニット数
	N = 2
	# 教師データ数
	M = 20
	# 学習係数
	lc = 0.0001
	# 学習回数
	Nl = 10000

	# データセットの作成(正解データの係数はランダムに選ばれる)
	# W0 = np.arange(1,N+1)
	W0 = np.array((2,3))
	# 適当に選ばれたXiの値から、教師データYを作成する
	X = np.random.rand(N,M) * 10
	Y = np.dot(W0,X)

	# 重みベクトルの初期値
	W = np.random.rand(N)

	# プロット用に誤差関数の値を格納するため空配列を定義
	dd = np.empty([1])

	for lp in range(Nl):
		# print '================================='
		# print 'lp =', lp

		# 出力データ
		Z = np.dot(W,X)

		# デルタ
		d = Y - Z
		
		# 二乗誤差関数
		_dd = np.sum(d*d)
		dd = np.append(dd,_dd)

		# 更新のための重み係数
		_dW = np.empty((N,M))
		dW = np.empty_like(W0)

		# バックプロパゲーション
		for i in range(N):
			for j in range(M):
				_dW[i,j] = lc * d[j] * X[i,j]
			
		dW = np.sum(_dW,1)

		# 重みベクトルの更新
		W = W + np.sum(_dW,1)
		# W = W + dW
		lmin = 0.1
		if dd[dd.size-1] < lmin:
			print 'iteration stop'
			print 'lmin =',lmin
			print 'lp =', lp
			break

	print '*** 確認 ***'
	print 'W0 =', W0
	print 'W  =', W
	print 'dd =', dd[dd.size-1]

	# プロット
	# print dd
	dd = dd[1:len(dd)]
	# print dd(len(dd)-1)
	# print 'dd =', dd[end]
	# print W

	import matplotlib.pyplot as plt

	# 二乗誤差のプロット
	plt.plot(dd)
	plt.show()


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



