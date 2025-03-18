# UCC---User-Controlled-Censorship

# User-Controlled Censorship (UCC)

A **Machine Learning-powered text filtering system** that provides user-controlled profanity censorship. Instead of rigid blacklists, this model **scores words based on severity**, allowing dynamic filtering based on user-defined thresholds.

## 🚀 Features
- **ML-based Text Classification** using Naïve Bayes + TF-IDF
- **Weighted Censorship** (Profanity is filtered based on severity scores)
- **User-defined Censorship Thresholds** (0.1 - 0.9)
- **Dynamic Profanity Detection** with an adjustable filtering model

## ⚙️ How It Works
1. **Text is analyzed** using a trained **Naïve Bayes model** to detect vulgarity.
2. If **vulgar**, words are **filtered based on their severity weight** (from `Version_2.py`).
3. Users can **set the censorship level** (e.g., mild filtering at 0.9 vs. strict filtering at 0.1).
4. Final output replaces words **above the threshold** with `[CENSORED]`.

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/UCC-User-Controlled-Censorship.git
   cd UCC-User-Controlled-Censorship
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage
Run the censorship script interactively:
```bash
python Version_2.py
```
Then enter the text and censorship threshold when prompted.

## 🔬 Future Enhancements
- **FastAPI-based API** for real-time censorship.
- **Integration with chat applications** to test live moderation.
- **Fine-tuning with deep learning models** like BERT for improved accuracy.

## 📜 License
This project is open-source. Feel free to contribute!

## Final Thoughts

I am taking a break from this project for now **EXAMS**!

### 💡 Contributors
Developed by **Kinjal Choudhary** 🎯

**Feel free to use or improve it**
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

