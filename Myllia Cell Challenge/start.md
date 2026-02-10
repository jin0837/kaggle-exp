# Myllia | Echoes of Silenced Genes（single-cell 特徴量設計）
## 概要
Myllia Cell Challenge に取り組み、表形式データのみでは未知摂動を予測できない理由を整理したうえで、
training_cells.h5ad（single-cell RNA-seq）から perturbation 効果を特徴量として設計する段階に進んだ。

## 今日やったこと
### コンペ仕様の整理
Public LB は 60 摂動、Private LB は別の 60 摂動で評価される
非公開 60 の遺伝子シンボルは終了 1 週間前に公開
したがって、公開データで 汎化性能の高い写像を学習し、公開後に同一パイプラインを適用する戦略が正解

### AnnData（training_cells.h5ad）の構造確認
n_obs × n_vars = 17882 × 19226
obs に sgrna_symbol（摂動遺伝子）、channel（バッチ）が存在
control は non-targeting と判明（細胞数も十分）

### single-cell → perturbation 特徴量の構築
channel（バッチ）内で non-targeting を引いた log fold change（logFC） を計算
摂動ごとにバッチ平均を取り、perturbation × 遺伝子 の特徴行列 X_sc を作成
これにより、train / val のどちらにも 同一手法で X を構築可能になった

### 学習・提出パイプラインへの接続
提出対象である 5127 遺伝子に y を揃えて学習
出力側 PCA（n_components=10）＋ Ridge（alpha=300）で回帰
Public 用の 60 摂動のみ予測を上書きし、残り 60 は baseline を保持（仕様どおり）
NaN の無い提出用 CSV を生成
