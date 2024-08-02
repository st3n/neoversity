from faker import Faker
import os


def generate_files(output_dir):
    fake = Faker()
    os.makedirs(output_dir, exist_ok=True)

    # Генерація 20 файлів з випадковим текстом
    for i in range(20):
        file_path = os.path.join(output_dir, f"file_{i+1}.txt")
        with open(file_path, "w") as f:
            f.write(fake.text(max_nb_chars=1000))
