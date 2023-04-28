# Define the knowledge base
knowledge_base = {
    'symptoms': {
        'fever': ['malaria', 'typhoid', 'influenza'],
        'cough': ['pneumonia', 'tuberculosis', 'asthma'],
        'headache': ['migraine', 'sinusitis', 'meningitis']
    },
    'treatments': {
        'malaria': 'Antimalarial medication',
        'typhoid': 'Antibiotics',
        'influenza': 'Antiviral medication',
        'pneumonia': 'Antibiotics',
        'tuberculosis': 'Antibiotics',
        'asthma': 'Bronchodilators',
        'migraine': 'Painkillers',
        'sinusitis': 'Decongestants',
        'meningitis': 'Antibiotics'
    }
}

# Define the inference engine
def infer(symptoms):
    diagnoses = []
    treatments = []
    for symptom in symptoms:
        if symptom in knowledge_base['symptoms']:
            diagnoses += knowledge_base['symptoms'][symptom]
    diagnoses = list(set(diagnoses))
    for diagnosis in diagnoses:
        if diagnosis in knowledge_base['treatments']:
            treatments.append(knowledge_base['treatments'][diagnosis])
    treatments = list(set(treatments))
    return diagnoses, treatments

# Example usage
symptoms = ['fever', 'headache']
diagnoses, treatments = infer(symptoms)
print('Diagnoses:', diagnoses)
print('Treatments:', treatments)
