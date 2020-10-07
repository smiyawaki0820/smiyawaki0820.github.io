# DeepGBM
> KDD 2019において発表された，LightGBMからNNへの蒸留とCategorical NNを用いたGBDT+NNのモデル
GBDTとNNのいいとこ取りしたモデルとなっており，Kaggle competitionで使われたdatasetを用いた予測問題では既存手法(LightGBM)よりスコアが改善したとのこと

## GBDT
* [x] dense data (tabular numerical features) に強い
* [_] sparse data (categorical features) に弱い
gainベースで分岐を行うため，0-1のカテゴリカルデータは過学習しやすい．
kaggler界隈ではsparseなデータを特徴抽出してdenseなデータにしたり，stacking等の手法を使って特徴選択することが多い．
* [_] オンライン学習に不利
GBDTなどの加法モデルは学習データが増えてくると，都度新たなtreeを追加してロス関数を下げていく手法である．
そのためオンライン学習では新しいデータに過学習しやすくなり，バッチ処理でのオフライン学習に比べて精度が劣る．

## DNN
* [x] categorical data に強い
embedding層を用いることでcategorical dataに対応できる
* [x] オンライン学習に強い
back propagationによってロス関数を下げる手法であることから，例え1つのデータでも過学習は起きにくい
* [_] dense data に弱い
dense data には FCNN(fully connected neural network) が用いられるが，複雑な最適化となることから局所解に陥りやすい

## DeepGBM
[x] dense data には GBDT，sparse data には NN(CatNN) を用いる．
[x] GBDTはNNへと蒸留され，このモデルはGBDT2NNと呼ばれる．
[x] 更に，蒸留によって全体の構造がNNとなることで，オンライン学習が可能となる．
<img src="https://cdn-ak.f.st-hatena.com/images/fotolife/b/behemoth03/20191109/20191109031617.jpg" alt="" title="">
<img src="https://cdn-ak.f.st-hatena.com/images/fotolife/b/behemoth03/20191109/20191109031650.jpg" alt="" title="">


### GBDT2NN

#NGBoost

# 参考
* [DeepGBM GitHub](https://github.com/motefly/DeepGBM/blob/master/README.md)
* [DeepGBMの論文まとめ](http://yh0sh.hateblo.jp/)
* [DeepGBM: A Deep Learning Framework Distilled by GBDT for Online Prediction Tasks](https://www.kdd.org/kdd2019/accepted-papers/view/deepgbm-a-deep-learning-framework-distilled-by-gbdt-for-online-prediction-t)
