
# 🧮 Absolute Statistics

> A recursive statistical model for central tendency convergence  
> Developed by **Himel Das** | 🇧🇩 Bangladesh | `hello2himel@outlook.com`

---

## 📖 Overview

**Absolute Statistics** is a novel approach to central tendency estimation that recursively applies the classical statistical measures — **mean**, **median**, and **mode** — until they converge to a unified value. This converged value, called the **Absolute Statistic**, captures a balanced and harmonized center of a dataset, synthesizing sensitivity, robustness, and frequency.

The project is implemented in **Python** as a command-line tool. It accepts numeric input from the user and iteratively refines the dataset using its own central statistics until all values fall within a specified threshold (`epsilon`).

---

## 🧠 The Idea

### Classical Measures of Central Tendency:

- **Mean**: Sensitive to all values; skewed by outliers.
- **Median**: Resistant to outliers; ignores distribution weight.
- **Mode**: Reflects the most frequent value(s); often undefined in continuous data.

These three are often used separately to describe different aspects of data. However, in real-world analysis, it's useful to find a **single unified value** that represents the dataset robustly and consistently.

---

### 🧪 Definition of the Absolute Statistic

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

The final stabilized value — the average of the last three — is called the **Absolute Statistic**.

---

## 🛠️ How It Works in Python

This tool is implemented with:

- `statistics` — for mean and median
- `collections.Counter` — for robust mode detection
- Custom convergence logic with adjustable precision
- Exception handling for multimodal and unique-value scenarios
- CLI-based interaction, designed for clarity and usability

The logic is split into functions:
- `calculate_mean`, `calculate_median`, `calculate_mode`
- `check_convergence` — determines whether values are close enough
- `absolute_statistics` — main recursive engine
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
git clone https://github.com/yourusername/absolute-statistics.git
cd absolute-statistics
python3 absolute_statistics.py
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
🎯 Absolute Statistic: 15.958333
```

---

## 📚 Applications

* **Robust statistical summarization**
* **Skew-agnostic center-finding**
* **Signal smoothing and normalization**
* **Data diagnostics (convergence speed reveals skew or outliers)**
* **Teaching tool** — illustrates differences between mean, median, mode

---

## 🔬 Future Work

* Mathematical proof of convergence for all dataset types
* Visualization (matplotlib graph of convergence path)
* PyPI packaging and CLI tool installation
* Support for CSV/JSON input
* Web version with interactive graphs

---

## 🧾 License

MIT License. Maybe I'll change later.

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
Das, H. (2025). Absolute Statistics: A Recursive Convergence Model for Central Tendency. GitHub Repository. https://github.com/hello2himel/equilibrium-statistic
```

---

Enjoy finding the *true center* of your data — not just statistically, but absolutely. ✨
