# Deep Learning Tutorials ディープラーニングチュートリアル

Deep Learning is a new area of Machine Learning research, which has been introduced with the objective of moving Machine Learning closer to one of its original goals: Artificial Intelligence. See these course notes for a brief introduction to Machine Learning for AI and an introduction to Deep Learning algorithms.
>人工知能：深層学習近い元の目標の一つに機械学習を移動することを目的に導入されている機械学習研究の新しい領域です。これらのコースノートを参照してくださいAIための機械学習を簡単に紹介 し、ディープ学習アルゴリズムを紹介。

Deep Learning is about learning multiple levels of representation and abstraction that help to make sense of data such as images, sound, and text. For more about deep learning algorithms, see for example:
>深層学習は、画像、音声、テキストなどのデータの意味を理解するのに役立つ表現や抽象化の複数のレベルの学習についてです。深い学習アルゴリズムの詳細については、例えば以下を参照してください。

- The monograph or review paper Learning Deep Architectures for AI (Foundations & Trends in Machine Learning, 2009).
>モノグラフやレビュー紙のAIのためのディープアーキテクチャの学習（機械学習、2009年に財団＆トレンドを）。

- The ICML 2009 Workshop on Learning Feature Hierarchies webpage has a list of references.
>フィーチャー階層学習上のICML 2009ワークショップのウェブページはあります参照のリストを。

- The LISA public wiki has a reading list and a bibliography.
Geoff Hinton has readings from 2009’s NIPS tutorial.
>LISA 公共wikiは持って読書リストと参考文献を。ジェフヒントンは持って読み値 2009年代のNIPSチュートリアルを。


The tutorials presented here will introduce you to some of the most important deep learning algorithms and will also show you how to run them using Theano. Theano is a python library that makes writing deep learning models easy, and gives the option of training them on a GPU.
>ここで紹介するチュートリアルは、最も重要な深い学習アルゴリズムのいくつかをご紹介しますし、また使用してそれらを実行する方法を説明しますテアーノーを。テアーノーは深い学習モデルを記述を容易にするPythonライブラリで、GPU上でそれらを訓練するオプションを提供します。

The algorithm tutorials have some prerequisites. You should know some python, and be familiar with numpy. Since this tutorial is about using Theano, you should read over the Theano basic tutorial first. Once you’ve done that, read through our Getting Started chapter – it introduces the notation, and [downloadable] datasets used in the algorithm tutorials, and the way we do optimization by stochastic gradient descent.
>アルゴリズムのチュートリアルは、いくつかの前提条件を持っている。あなたは、いくつかのPythonを知っている、とnumpyの精通している必要があります。このチュートリアルでは、テアーノーの使用についてであるので、あなたは上読んでくださいテアーノー基本的なチュートリアルを最初に。あなたはそれをやった後は、私たちの目を通し入門章-それは表記法、およびアルゴリズムのチュートリアルで使用される[ダウンロード可能]のデータセット、および我々は確率的勾配降下による最適化を行う方法を紹介します。

The purely supervised learning algorithms are meant to be read in order:
>純粋教師あり学習アルゴリズムが順に読み込まれることを意味する。

1. Logistic Regression - using Theano for something simple
>ロジスティック回帰 -シンプルな何かのためにテアーノーを使用して

2. Multilayer perceptron - introduction to layers
>多層パーセプトロン -層への導入

3. Deep Convolutional Network - a simplified version of LeNet5
>ディープ畳み込みネットワーク - LeNet5の簡易版

The unsupervised and semi-supervised learning algorithms can be read in any order (the auto-encoders can be read independently of the RBM/DBN thread):
>教師なし及び準教師付き学習アルゴリズムは、任意の順序で読み取ることができます（オートエンコーダーは独立RBM / DBNスレッドの読むことができます）。

 - Auto Encoders, Denoising Autoencoders - description of autoencoders
>オートエンコーダ、ノイズ除去Autoencoders - autoencodersの説明

 - Stacked Denoising Auto-Encoders - easy steps into unsupervised pre-training for deep nets
>スタックノイズ除去オートエンコーダー -深いネットの教師なし事前研修への簡単なステップ

 - Restricted Boltzmann Machines - single layer generative RBM model
>制限付きボルツマンマシン -単一層生成的RBMモデル

 - Deep Belief Networks - unsupervised generative pre-training of stacked RBMs followed by supervised fine-tuning
>ディープ信念ネットワーク -監視付きの微調整が続く積み重ねRBMのの教師なし生成的な事前研修

Building towards including the mcRBM model, we have a new tutorial on sampling from energy models:
>mcRBMモデルを含め向けての構築、我々はエネルギーモデルからのサンプリングの新しいチュートリアルがあります。

- HMC Sampling - hybrid (aka Hamiltonian) Monte-Carlo sampling with scan()
>HMCサンプリング -スキャンとのハイブリッド（別名ハミルトニアン）モンテカルロサンプリング（）

Building towards including the Contractive auto-encoders tutorial, we have the code for now:
>ない縮小オートエンコーダーのチュートリアルを含め向けての構築、我々は今のコードを持っている：

Contractive auto-encoders code - There is some basic doc in the code.
>収縮オートエンコーダーのコード-コード内のいくつかの基本的なドキュメントがあります。

Recurrent neural networks with word embeddings and context window:
>ワード埋め込み、コンテキストウィンドウリカレントニューラルネットワーク：

- Semantic Parsing of Speech using Recurrent Net
>再発ネットを用いた音声の意味解析

LSTM network for sentiment analysis:
>センチメント分析のためのLSTMネットワーク：

- LSTM network
>LSTMネットワーク

Energy-based recurrent neural network (RNN-RBM):
>エネルギーベースのリカレントニューラルネットワーク（RNN-RBM）：

- Modeling and generating sequences of polyphonic music
>ポリフォニー音楽のモデリングと生成シーケンス