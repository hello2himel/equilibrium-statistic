
# 🧮 Equilibrium Statistic

> A recursive statistical model for central tendency convergence  
> Developed by **Himel Das** | 🇧🇩 Bangladesh | `hello2himel@proton.me`

---

## 📖 Overview

**Equilibrium Statistic** is a novel approach to central tendency estimation that recursively applies the classical statistical measures — **mean**, **median**, and **mode** — until they converge to a unified value. This converged value, called the **Equilibrium Statistic**, captures a balanced and harmonized center of a dataset, synthesizing sensitivity, robustness, and frequency.

The project is implemented in **Python** as a command-line tool. It accepts numeric input from the user and iteratively refines the dataset using its own central statistic until all values fall within a specified threshold (`epsilon`).

---

## 🧠 The Idea

### Classical Measures of Central Tendency:

- **Mean**: Sensitive to all values; skewed by outliers.
- **Median**: Resistant to outliers; ignores distribution weight.
- **Mode**: Reflects the most frequent value(s); often undefined in continuous data.

These three are often used separately to describe different aspects of data. However, in real-world analysis, it's useful to find a **single unified value** that represents the dataset robustly and consistently.

---

### 🧪 Definition of the Equilibrium Statistic

Let the initial dataset be:

```

D₀ = \[x₁, x₂, ..., xₙ]

```

For each iteration *k*, compute:

```

meanₖ = mean(Dₖ)
medianₖ = median(Dₖ)
modeₖ = mode(Dₖ)

```

Then form the new dataset:

```

Dₖ₊₁ = \[meanₖ, medianₖ, modeₖ]

```

Repeat the process until:

```

max(|meanₖ - medianₖ|, |medianₖ - modeₖ|, |modeₖ - meanₖ|) < ε

````

Where **ε (epsilon)** is a convergence threshold, e.g., `0.001`.

The final stabilized value — the average of the last three — is called the **Equilibrium Statistic**.

---

## 🛠️ How It Works in Python

This tool is implemented with:

- `statistic` — for mean and median
- `collections.Counter` — for robust mode detection
- Custom convergence logic with adjustable precision
- Exception handling for multimodal and unique-value scenarios
- CLI-based interaction, designed for clarity and usability

The logic is split into functions:
- `calculate_mean`, `calculate_median`, `calculate_mode`
- `check_convergence` — determines whether values are close enough
- `equilibrium_statistic` — main recursive engine
- `get_user_input` — interactive CLI prompt

Each iteration is printed to the console for transparency and traceability.

---

## 🚀 How to Run

### 📦 Requirements

- Python 3.7+
- No external packages required

### ▶️ Run the App

Clone the repository and run the script:

```bash
git clone https://github.com/hello2himel/equilibrium-statistic.git
cd equilibrium-statistic
python3 main.py
````

### 📥 Input Example:

When prompted:

```
📥 Enter numbers separated by commas: 14, 15, 15, 16, 16, 16, 17, 18
🎯 Enter convergence threshold (default 0.001):
```

### ✅ Output:

```
Iteration 1:
  Mean:   15.875
  Median: 16.0
  Mode:   16.0
  Output: [15.875, 16.0, 16.0]
  Spread: 0.125 (target: ≤ 0.001)

...

✅ CONVERGENCE ACHIEVED after 4 iterations!
🎯 Equilibrium Statistic: 15.958333
```

---

## 📚 Applications

* **Robust statistical summarization**
* **Skew-agnostic center-finding**
* **Signal smoothing and normalization**
* **Data diagnostics (convergence speed reveals skew or outliers)**
* **Teaching tool** — illustrates differences between mean, median, mode

---

## 🧭 Planned Research & Development

The Equilibrium Statistic model presents opportunities for both theoretical exploration and real-world application. Below is a structured roadmap outlining future development goals across mathematical foundations, empirical validation, software tooling, and academic dissemination.

---

### 🧮 1. Mathematical Foundation

- **Convergence Proof** — Establish conditions under which the model converges.
- **Uniqueness and Existence** — Prove whether the result is consistent for a given dataset.
- **Rate of Convergence** — Analyze speed and stability of convergence.
- **Behavioral Analysis** — Study responses to edge cases and pathological data.
- **Robustness & Invariance** — Investigate behavior under scaling, translation, and noisy inputs.

---

### 📊 2. Statistical Validation

- **Distributional Testing** — Assess performance on normal, skewed, uniform, multimodal, and heavy-tailed distributions.
- **Comparative Analysis** — Evaluate against mean, median, mode, trimmed mean, and Winsorized mean.
- **Monte Carlo Simulations** — Test on large random samples to assess generalizability.
- **Noise & Outlier Sensitivity** — Measure resistance to outliers and random fluctuations.
- **Missing Data Handling** — Explore imputation-free resilience.

---

### 🏭 3. Real-World Application Domains

- **Finance** — Stock returns, trading anomalies.
- **Medicine** — Vital statistic, lab measurements.
- **Climate Science** — Sensor time series, anomaly detection.
- **Education & Surveys** — Likert responses and opinion analysis.
- **Manufacturing** — Tolerance analysis and quality control.

---

### 🧪 4. Methodological Extensions

- **Weighted Centrality** — Introduce weight control between mean, median, and mode.
- **Multivariate Generalization** — Extend to multidimensional datasets.
- **Sequential Adaptation** — Apply to time series or streaming data.
- **Confidence Intervals** — Bootstrap-based uncertainty estimation.
- **Bayesian Reformulation** — Explore probabilistic interpretations.

---

### 💻 5. Software & Tooling

- **PyPI Package** — Publish as installable Python library.
- **R Package** — Extend usability to statistical ecosystem.
- **Benchmark Suite** — Include runtime profiling and precision tests.
- **Interactive Demos** — Build a web-based or notebook demo.
- **Documentation & Tutorials** — Provide Jupyter and Colab examples.

---

### 📚 6. Academic Dissemination

- **Formal Paper** — Write and submit to a statistic or applied math journal.
- **Literature Review** — Survey surrounding research for citations and background.
- **Conference Presentation** — Share findings at relevant academic events.
- **arXiv Preprint** — Share early versions with the research community.
- **Collaboration & Peer Review** — Seek academic mentorship and expert feedback.

---

### 🌍 7. Long-Term Vision

- **Curricular Adoption** — Propose for inclusion in academic syllabi.
- **Industry Use Cases** — Encourage adoption in data analysis workflows.
- **Standardization** — Contribute to statistical best practices or libraries.
- **ML & Big Data Integration** — Adapt model for machine learning preprocessing and large-scale systems.

---

## 🎯 Near-Term Priorities

- 🔍 Convergence proof and robustness study
- 🔬 Statistical validation against traditional measures
- 📈 Real-world case studies and Monte Carlo simulations
- 📝 Drafting and structuring academic paper
- 📦 Packaging and preparing for PyPI release


> _This roadmap serves as both a development plan and a research agenda. Contributions and collaborations are welcome._ 🤝


---

## 🧾 License

MIT License.

---

## 👨‍🔬 Author

### **Himel Das**  
President, Bogura Zilla School Science Club  
SSC 2025 · Bogura Zilla School, Bogura, Bangladesh  
📧 [hello2himel@proton.me](mailto:hello2himel@proton.me)  
🌐 [hello2himel.netlify.app](https://hello2himel.netlify.app)


---

## 🌐 Citation

If you use this in research or teaching, please cite as:

```plaintext
Das, H. (2025). Equilibrium Statistic: A Recursive Convergence Model for Central Tendency. GitHub Repository. https://github.com/hello2himel/equilibrium-statistic
```

---