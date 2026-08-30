# Indian Sign Language Recognition with Landmark Features

Code accompanying the paper *"Indian Sign Language Recognition with Landmark Features: Accuracy–Efficiency Tradeoffs Across Classical and Deep Models"* (Anurag Sharma, JK Lakshmipat University, Jaipur).

We study isolated Indian Sign Language (ISL) word recognition on a school-collected dataset of 67 signs and 1,072 videos. Hand and upper-body landmarks extracted with MediaPipe are converted into spatial and temporal features and classified with three models: XGBoost, a CNN–LSTM, and a compact Transformer. The paper's central finding is an accuracy–efficiency tradeoff: the Transformer reaches 73.2% accuracy, while XGBoost reaches 71.0% at roughly 8x lower training cost and 4x faster inference.

- **Paper:** [Zenodo (Version 1.0)](https://doi.org/10.5281/zenodo.21956082) — [Record](https://zenodo.org/records/21956082)
- **Dataset:** https://www.kaggle.com/datasets/bugruster/isl-buggy-arn089

## 📄 Published Paper

> **Sharma, A. (2026).** *Indian Sign Language Recognition with Landmark Features: Accuracy–Efficiency Tradeoffs Across Classical and Deep Models* (Version 1.0). Zenodo. [https://doi.org/10.5281/zenodo.21956082](https://doi.org/10.5281/zenodo.21956082)

The full paper (LaTeX source and PDF) is available in the [`ResearchPaper/`](ResearchPaper/) directory.

## Repository contents

> Note: file names below are mapped to their likely role based on the paper's methodology section. Please correct any mismatches against what's actually in each notebook.

| File | Purpose |
|---|---|
| `testprep.ipynb` | Data preparation: loads raw video/landmark data, builds train/validation/test splits (70/15/15, stratified by gloss) |
| `folder.py` | Helper utilities (e.g. file/folder handling for the dataset directory structure) |
| `code.ipynb` | MediaPipe landmark extraction and feature engineering (pairwise distances, joint angles, motion trajectories) |
| `code2.ipynb` | Model training: XGBoost, CNN–LSTM, and Transformer classifiers (Table II, Table III) |
| `testcode.ipynb` | Evaluation and metrics: accuracy/precision/recall/F1 on the test split, 5-fold cross-validation for XGBoost (Table V) |
| `test.ipynb` | Ablation studies on engineered features (Table VI) |
| `ResearchPaper/` | Published paper (LaTeX source, PDF, architecture diagrams) |

## Setup

```bash
git clone https://github.com/BugRuster/MJRIDK.git
cd MJRIDK
pip install -r requirements.txt
```

Requires Python 3.9+. Key dependencies: `mediapipe`, `xgboost`, `torch` (or `tensorflow`, depending on your CNN–LSTM/Transformer implementation), `scikit-learn`, `numpy`, `pandas`.

## Reproducing the paper's results

1. Download the dataset from Kaggle and place it in a local `data/` directory (see `testprep.ipynb` for the expected folder structure).
2. Run `testprep.ipynb` to generate the train/validation/test splits.
3. Run `code.ipynb` to extract MediaPipe landmarks and engineer features for all clips.
4. Run `code2.ipynb` to train all three classifiers (XGBoost, CNN–LSTM, Transformer).
5. Run `testcode.ipynb` to reproduce Table II (test-set performance), Table III (training/inference cost), and Table V (XGBoost 5-fold cross-validation).
6. Run `test.ipynb` to reproduce Table VI (XGBoost feature ablations).

## Dataset

67 ISL words across six semantic categories (daily activities, emotions, colors, animals, numbers, miscellaneous), collected with four native signers (two male, two female, ages 18–25) at Seth Anandi Lal Poddar Deaf, Dumb and Blind School, Jaipur. Videos: 1920x1080, 30 FPS, H.264 MP4. Full details in the paper, Section III.B.

Informed consent was obtained from all participants (and guardians where required) prior to recording. Identifiers were removed from released filenames. The dataset is shared for research use under the Kaggle dataset terms.

## Limitations

This is a pilot-scale dataset: four signers from a single institution cannot represent the full range of regional ISL variation. Splits are gloss-stratified rather than strictly signer-independent. The models here handle isolated word recognition only, not continuous signing. See the paper's Limitations section for full details.

## Citation

If you use this code or dataset, please cite:

```bibtex
@misc{sharma2026isl,
  title={Indian Sign Language Recognition with Landmark Features: Accuracy--Efficiency Tradeoffs Across Classical and Deep Models},
  author={Sharma, Anurag},
  year={2026},
  publisher={Zenodo},
  version={1.0},
  doi={10.5281/zenodo.21956082},
  url={https://zenodo.org/records/21956082}
}
```

## Acknowledgments

We thank Seth Anandi Lal Poddar Deaf, Dumb and Blind School, Jaipur, and the student participants who contributed recordings.

## License

Code is released under the MIT License (see [LICENSE](LICENSE)). The dataset is governed separately by the Kaggle dataset terms linked above.

## Contact

Anurag Sharma — bugruster@gmail.com
