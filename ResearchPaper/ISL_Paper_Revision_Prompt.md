# Revision prompt: "Indian Sign Language Recognition: A Machine Learning Approach"

Use this as a working checklist, or paste it whole into an AI writing tool along with the paper text to get section-by-section rewrites. Each item names the exact problem, where it is, and the fix to apply.

---

## Priority 1 — Must fix before any submission (arXiv, journal, or conference)

### 1. Fake/placeholder author names in references
**Problem:** References [1] and [4] list the author as "R. Author" and "A. Author" — literal placeholder text never replaced with real names.
**Where:** Reference list, entries [1] and [4].
**Fix:** Go back to wherever these sources were found (search "INCLUDE-50 dataset Indian Sign Language" and "lightweight framework sign language pose estimation" on Google Scholar) and replace with the real author names, or remove the citations entirely if they can't be verified. Do not submit with any reference unverified — spot-check every single one against the actual publication (title, venue, year, page numbers) before submission.

### 2. Missing architecture diagram
**Problem:** Section III.A says literally "[System Architecture Diagram]" instead of showing Figure 1.
**Where:** Section III.A, "Overall Architecture."
**Fix:** Insert a real diagram showing: Input Processing Module → Feature Extraction Engine → Classification System → Output Generation Module, with the MediaPipe hand/pose landmark extraction and the three-model comparison (XGBoost/CNN-LSTM/Transformer) visible as sub-stages. (A version of this diagram was generated in this conversation — recreate it as a proper figure in your document, e.g. using PowerPoint, draw.io, or matplotlib/graphviz, saved as a high-res PNG/PDF and embedded with a proper caption.)

### 3. Misleading headline result
**Problem:** Abstract and title emphasize XGBoost's 71% as "the" achievement, but Table II shows Transformer actually scored higher (73.2%). This looks like cherry-picking to an attentive reader.
**Where:** Abstract, and framing throughout Section IV.
**Fix:** Reframe explicitly around the accuracy/efficiency tradeoff. Suggested abstract line: *"While a Transformer model achieved the highest accuracy (73.2%), our XGBoost-based approach reached competitive accuracy (71.0%) at a fraction of the computational cost (15 min vs. 120 min training time), making it the more practical choice for resource-constrained deployment."* Apply the same reframing to the Conclusion and Title if the title over-claims XGBoost as "the" method.

### 4. No author affiliation or contact info
**Problem:** No institution, email, or contact listed for Adarsh Ranjan Nayak or Anurag Sharma.
**Where:** Title page / header.
**Fix:** Add full affiliation (university/institution name, department), city, and at least one corresponding author email address. Standard for any journal or arXiv submission.

### 5. No dataset or code release
**Problem:** The paper's core contribution is a dataset + system, but neither is released. This is a major credibility and citability gap in 2026 ML publishing norms.
**Where:** Applies to the whole paper; most relevant in Section III.B (Dataset) and VII (Conclusion).
**Fix:** Create a GitHub repo with (a) the feature-extraction and training code, and (b) either the full dataset, a representative subset, or a "data card" explaining access conditions if the school's data can't be fully public (e.g. "available upon request for research purposes, contact [email]"). Add the repo link to the abstract and Section III.B.

---

## Priority 2 — Should fix, meaningfully strengthens the paper

### 6. Small dataset not framed as a limitation
**Problem:** 4 signers, 67 words, 1072 videos is a reasonable pilot dataset, but the paper doesn't explicitly flag this as a limitation — which is awkward since the paper itself criticizes prior ISL datasets for lacking diversity (Section II.D).
**Where:** Add to Section VI (Future Work) or a new "Limitations" subsection before the Conclusion.
**Fix:** Add 3–4 sentences: *"Our dataset, while methodologically rigorous, is limited to 4 signers from a single institution, which constrains generalizability across India's regional ISL variations. Future work should expand signer diversity across geographic regions, as discussed in Section VI.B."*

### 7. No quantitative comparison to prior ISL work
**Problem:** Section II reviews INCLUDE-50, ISL-MOD, HMM/SVM/LSTM approaches, but Results (Section IV) never numerically compares your 71%/73.2% against their reported accuracies.
**Where:** Add to Section IV.A or a new subsection "Comparison to Prior Work."
**Fix:** Add a table: Method | Dataset | Vocabulary size | Accuracy — listing your work alongside INCLUDE-50, ISL-MOD, and 2–3 cited papers from your literature review (e.g. references [6], [7], [10]). Even an approximate comparison substantially strengthens your contribution claim.

### 8. Generic, padding-heavy bullet lists in Sections I–III
**Problem:** Many bullets restate generic ML/CV concepts without paper-specific insight (e.g., "Real-time processing requirements," "Diverse signing speeds and styles") — reads like slide notes, not a paper, and reviewers will notice the padding.
**Where:** Section I.B, I.C, I.D throughout.
**Fix:** Cut bullets that don't reference something specific to this paper's methodology or dataset. Convert survivors into 1–2 sentence prose paragraphs. Rule of thumb: if a bullet could appear unchanged in any other SLR paper, cut or specify it.

### 9. No statistical variance reporting
**Problem:** Cross-validation folds range 70.5%–71.4% (Table IV) but no standard deviation or confidence interval is reported.
**Where:** Section IV.C.
**Fix:** Add one line: *"Accuracy across folds showed low variance (σ = 0.32%, 95% CI: 70.6%–71.4%), indicating stable model performance."* (Compute the actual SD from your 5 fold values.)

### 10. No ethics/consent statement
**Problem:** The paper involves human subjects (a school for deaf/blind students) but never mentions informed consent or institutional approval.
**Where:** Add to Section III.B.1 (Data Collection Protocol) or as a new short subsection.
**Fix:** Add 2–3 sentences confirming: consent obtained from participants/guardians, any institutional/ethics review board approval, and data anonymization practices. This is expected by any serious reviewer, especially given the vulnerable population involved.

---

## Priority 3 — Optional but recommended polish

### 11. Figure 2 caption duplicates the plotted content redundantly
**Fix:** Trim the Fig. 2 caption to one sentence; the numbers are already in Table II — no need to repeat them in the caption too.

### 12. Vocabulary/category labels (Section III.B.2, Table I) could show category-wise accuracy
**Fix:** If time permits, break down accuracy by category (Daily Activities, Emotions, Colors, Animals, Numbers, Misc.) — this often reveals which gesture types are hardest to classify and adds a genuinely new insight beyond the aggregate 71%.

### 13. References formatting consistency
**Fix:** Once names are corrected (item 1), do a full pass checking DOI/page number formatting consistency across all 35 references — journals/arXiv moderators do check this.

---

## Suggested order of operations
1. Fix items 1–5 (Priority 1) — these are the ones that would embarrass you if caught post-publication.
2. Fix items 6–10 (Priority 2) — do these if you have 2–3 more days; they meaningfully raise review odds at a real journal.
3. Fix items 11–13 only if time allows — cosmetic, not going to sink or save the paper.

After Priority 1 + 2 fixes, this paper moves from roughly 5.5/10 to a genuinely solid 8/10 submission — worth re-reading once more end-to-end before posting to arXiv or submitting to a journal.
