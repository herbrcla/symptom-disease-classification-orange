import pandas as pd

df = pd.read_csv("DiseaseAndSymptoms.csv")
print(len(df))
df["Symptoms"] = df[["Symptom_1", "Symptom_2", "Symptom_3", "Symptom_4", "Symptom_5", "Symptom_6", "Symptom_7", "Symptom_8", "Symptom_9", "Symptom_10", "Symptom_11", "Symptom_12", "Symptom_13", "Symptom_14", "Symptom_15", "Symptom_16", "Symptom_17"]].fillna("").agg(" ".join, axis=1)
df[["Disease", "Symptoms"]].to_csv("orange_ready_dataset.csv", index=False)
