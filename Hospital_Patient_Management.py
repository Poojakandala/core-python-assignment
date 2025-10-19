class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease
patients = [
    Patient("Alice", 30, "Flu"),
    Patient("Bob", 45, "Diabetes"),
    Patient("Charlie", 35, "Flu")
]
def search_patients_by_disease(patients, disease):
    return [patient.name for patient in patients if patient.disease == disease]

search_disease = "Flu"
matched_patients = search_patients_by_disease(patients, search_disease)
print(f"Patients with {search_disease}: {matched_patients}")
