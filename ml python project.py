import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# -----------------------------
# 1. Load dataset
# -----------------------------
df = pd.read_json(
    "c:/Users/aniru/Downloads/News_Category_Dataset_v3.json/News_Category_Dataset_v3.json",
    lines=True
)

# Keep headline, category, and text for display + recommendation
df["text"] = df["headline"].fillna("") + " " + df["short_description"].fillna("")
df = df[["headline", "category", "text"]]

print(df.head())
print(df.columns)

# -----------------------------
# 2. Vectorize text
# -----------------------------
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_df=0.7,
    min_df=5,
    max_features=5000
)

X = vectorizer.fit_transform(df["text"])
print(X.shape)

# -----------------------------
# 3. Simple CLI to pick an article
# -----------------------------
print("\nPick an article you like:\n")
sample = df.sample(10, random_state=42)
for idx in sample.index:
    print(f"{idx}: [{df.loc[idx,'category']}] {df.loc[idx,'headline']}")

liked_idx = int(input("\nEnter article index: "))
liked_category = df.loc[liked_idx, "category"]

# -----------------------------
# 4. Compute similarity within the same category
# -----------------------------
same_cat_indices = df[df["category"] == liked_category].index
similarities = cosine_similarity(
    X[liked_idx],
    X[same_cat_indices]
).flatten()

top_indices = same_cat_indices[
    similarities.argsort()[-6:-1][::-1]
]

# -----------------------------
# 5. Display results
# -----------------------------
print("\nBecause you liked:\n")
print(f"[{df.loc[liked_idx,'category']}] {df.loc[liked_idx,'headline']}\n")

print("You might also like:\n")
for i in top_indices:
    print(f"- [{df.loc[i,'category']}] {df.loc[i,'headline']}")
