import os


def save_uploaded_file(uploaded_file):
    os.makedirs("audio", exist_ok=True)
    file_path = os.path.join("audio", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path
